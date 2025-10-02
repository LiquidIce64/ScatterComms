import os
import hashlib
from typing import TYPE_CHECKING, cast
from uuid import UUID
from datetime import datetime, timezone
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from .base import BaseBackend
from .multithreading import multithreaded
from .cached_object import CachedObject
from .storage import StorageBackend
from database import Database, Message, Attachment

if TYPE_CHECKING:
    from .profile import ProfileBackend


class MessageBackend(BaseBackend):
    class Attachment(CachedObject):
        def __init__(self, attachment, **kwargs):
            if hasattr(self, '_initialized'):
                return
            super().__init__()
            self._initialized = True
            self.__uuid: UUID = attachment.uuid
            self.__filehash: str = attachment.filehash
            self.__filename: str = attachment.filename

        def update(self, attachment, **kwargs):
            self.__uuid: UUID = attachment.uuid
            self.__filehash: str = attachment.filehash
            self.__filename: str = attachment.filename
            self.changed.emit()

        @property
        def uuid(self): return self.__uuid
        @property
        def filehash(self): return self.__filehash
        @property
        def filename(self): return self.__filename

        @property
        def filepath(self): return (
            StorageBackend.Attachment.get_attachment_file(self.__uuid, self.__filename)
            or StorageBackend.Attachment.get_attachment_file(self.__uuid, self.__filename, use_cache=True)
        )

    class Message(CachedObject):
        def __init__(self, message, **kwargs):
            if hasattr(self, '_initialized'):
                return
            super().__init__()
            self._initialized = True

            self.__uuid: UUID = message.uuid
            self.__text: str = message.text

            backend = BaseBackend.get_backend('ProfileBackend')
            if TYPE_CHECKING:
                backend = cast(ProfileBackend, backend)
            self.__author = backend.Profile(message.author)

            self.__attachments = [MessageBackend.Attachment(attachment) for attachment in message.attachments]
            self.__replying_to: MessageBackend.Message | None = None
            if message.replying_to is not None:
                self.__replying_to = MessageBackend.Message(message.replying_to)

            self.__created_at: datetime = message.created_at
            # Convert from UTC to local timezone
            self.__created_at = self.__created_at.replace(tzinfo=timezone.utc).astimezone()

        def update(self, message, **kwargs):
            self.__uuid: UUID = message.uuid
            self.__text: str = message.text

            backend = BaseBackend.get_backend('ProfileBackend')
            if TYPE_CHECKING:
                backend = cast(ProfileBackend, backend)
            self.__author = backend.Profile(message.author)

            self.__attachments = [MessageBackend.Attachment(attachment) for attachment in message.attachments]
            self.__replying_to: MessageBackend.Message | None = None
            if message.replying_to is not None:
                self.__replying_to = MessageBackend.Message(message.replying_to)

            self.__created_at: datetime = message.created_at
            # Convert from UTC to local timezone
            self.__created_at = self.__created_at.replace(tzinfo=timezone.utc).astimezone()
            self.changed.emit()

        @property
        def uuid(self): return self.__uuid
        @property
        def text(self): return self.__text
        @property
        def author(self): return self.__author
        @property
        def replying_to(self): return self.__replying_to
        @property
        def created_at(self): return self.__created_at

        @property
        def attachments(self):
            for attachment in self.__attachments:
                yield attachment

        @text.setter
        def text(self, new_value: str):
            self.__text = new_value
            MessageBackend.edit_message(self.__uuid, text=new_value)
            self.changed.emit()

    @staticmethod
    def get_messages(chat_uuid: UUID, offset=0, limit=50):
        with Database.create_session() as session:
            messages = session.scalars(
                select(Message).options(selectinload(Message.attachments))
                .where(Message.chat_uuid == chat_uuid)
                .order_by(Message.created_at.desc())
                .offset(offset)
                .limit(limit)
            ).all()
            messages_list = [MessageBackend.Message(message) for message in messages]
        return messages_list

    @staticmethod
    @multithreaded
    def edit_message(uuid: UUID, **kwargs):
        with Database.create_session() as session:
            message = session.get(Message, uuid)
            for kw, value in kwargs.items():
                setattr(message, kw, value)
            session.add(message)
            session.commit()

    @staticmethod
    def create_message(chat_uuid: UUID, author_uuid: UUID, text: str, attachment_filepaths: list[str]):
        if text == '':
            text = None
        with Database.create_session() as session:
            _attachments = [
                Attachment(
                    filename=os.path.basename(filepath),
                    filehash=hashlib.file_digest(open(filepath, 'rb'), 'md5').hexdigest(),
                    sort_order=i
                ) for i, filepath in enumerate(attachment_filepaths)
            ]

            session.add_all(_attachments)
            _message = Message(
                chat_uuid=chat_uuid,
                author_uuid=author_uuid,
                text=text,
                attachments=_attachments
            )
            session.add(_message)
            session.flush()

            for attachment, filepath in zip(_attachments, attachment_filepaths):
                session.refresh(attachment)
                if StorageBackend.Attachment.add_attachment_file(attachment.uuid, filepath) is None:
                    raise FileNotFoundError('Could not copy attached file to appdata')

            session.commit()
            message = MessageBackend.Message(_message)
        return message

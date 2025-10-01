import os
import hashlib
from uuid import UUID

from sqlalchemy import select

from .cached_object import CachedObject
from .storage import StorageBackend
from database import Database, Attachment


class AttachmentBackend:
    class Attachment(CachedObject):
        def __init__(self, attachment):
            if hasattr(self, '_initialized'):
                return
            super().__init__()
            self._initialized = True
            self.__uuid: UUID = attachment.uuid
            self.__filehash: str = attachment.filehash
            self.__filename: str = attachment.filename

        def update(self, attachment):
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

    @staticmethod
    def get_attachments(message_uuid: UUID):
        with Database.create_session() as session:
            attachments = session.scalars(
                select(Attachment)
                .where(Attachment.message_uuid == message_uuid)
                .order_by(Attachment.sort_order)
            ).all()
            attachments_list = [AttachmentBackend.Attachment(attachment) for attachment in attachments]
        return attachments_list

    @staticmethod
    def add_attachments(message_uuid: UUID, filepaths: list[str]):
        with Database.create_session() as session:
            attachments: list[AttachmentBackend.Attachment] = []
            for filepath in filepaths:
                _attachment = Attachment(
                    message_uuid=message_uuid,
                    filename=os.path.basename(filepath),
                    filehash=hashlib.file_digest(open(filepath, 'rb'), 'md5').hexdigest()
                )
                session.add(_attachment)
                session.flush()
                session.refresh(_attachment)
                if StorageBackend.Attachment.add_attachment_file(_attachment.uuid, filepath) is None:
                    raise FileNotFoundError('Could not copy attached file to appdata')
            session.commit()
            attachments.append(AttachmentBackend.Attachment(_attachment))
        return attachments

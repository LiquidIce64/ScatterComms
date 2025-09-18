from uuid import UUID
from sqlalchemy import select

from .multithreading import multithreaded
from .cached_object import CachedObject
from .profile import ProfileBackend
from database import Database, Message


class MessageBackend:
    class Message(CachedObject):
        def __init__(self, message):
            if hasattr(self, '_initialized'):
                return
            super().__init__()
            self.__uuid: UUID = message.uuid
            self.__text: str = message.text
            self.__author = ProfileBackend.Profile(message.author)
            self._initialized = True

        def update(self, message):
            self.__uuid: UUID = message.uuid
            self.__text: str = message.text
            self.__author = ProfileBackend.Profile(message.author)
            self.changed.emit()

        @property
        def uuid(self): return self.__uuid
        @property
        def text(self): return self.__text
        @property
        def author(self): return self.__author

        @text.setter
        def text(self, new_value: str):
            self.__text = new_value
            MessageBackend.edit_message(self.__uuid, text=new_value)
            self.changed.emit()

    @staticmethod
    def get_messages(chat_uuid: UUID, offset=0, limit=50):
        with Database.create_session() as session:
            messages = session.scalars(
                select(Message)
                .where(Message.chat_uuid == chat_uuid)
                .order_by(Message.created_at)
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
    def create_message(chat_uuid: UUID, author_uuid: UUID, text: str):
        with Database.create_session() as session:
            _message = Message(chat_uuid=chat_uuid, author_uuid=author_uuid, text=text)
            session.add(_message)
            session.commit()
            message = MessageBackend.Message(_message)
        return message

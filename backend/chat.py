from uuid import UUID
from sqlalchemy import select, func

from .multithreading import multithreaded
from .cached_object import CachedObject
from database import Database, ChatCategory, Chat, Role, chat_category_roles, User


def select_with_whitelist(model, profile_uuid: UUID):
    return (
        select(model).distinct()
        .join(Role, model.whitelisted_roles)
        .join(User, Role.users)
        .where(User.uuid == profile_uuid)
    )


class ChatBackend:
    class Category(CachedObject):
        def __init__(self, category):
            if hasattr(self, '_initialized'):
                return
            super().__init__()
            self._initialized = True

            self.__uuid: UUID = category.uuid
            self.__name: str = category.name
            self.__collapsed: bool = category.collapsed

        def update(self, category):
            self.__uuid: UUID = category.uuid
            self.__name: str = category.name
            self.__collapsed: bool = category.collapsed
            self.changed.emit()

        @property
        def uuid(self): return self.__uuid
        @property
        def name(self): return self.__name
        @property
        def collapsed(self): return self.__collapsed

        @name.setter
        def name(self, new_value: str):
            self.__name = new_value
            ChatBackend.edit_category(self.__uuid, name=new_value)
            self.changed.emit()

        @collapsed.setter
        def collapsed(self, new_value: bool):
            if self.__collapsed == new_value:
                return
            self.__collapsed = new_value
            ChatBackend.edit_category(self.__uuid, collapsed=new_value)
            self.changed.emit()

    class Chat(CachedObject):
        def __init__(self, chat):
            if hasattr(self, '_initialized'):
                return
            super().__init__()
            self._initialized = True

            self.__uuid: UUID = chat.uuid
            self.__name: str = chat.name
            self.__voice_enabled: bool = chat.voice_enabled

        def update(self, chat):
            self.__uuid: UUID = chat.uuid
            self.__name: str = chat.name
            self.__voice_enabled: bool = chat.voice_enabled
            self.changed.emit()

        @property
        def uuid(self): return self.__uuid
        @property
        def name(self): return self.__name
        @property
        def voice_enabled(self): return self.__voice_enabled

        @name.setter
        def name(self, new_value: str):
            self.__name = new_value
            ChatBackend.edit_chat(self.__uuid, name=new_value)
            self.changed.emit()

    @staticmethod
    def get_categories(profile_uuid: UUID, server_uuid: UUID):
        with Database.create_session() as session:
            categories = session.scalars(
                select_with_whitelist(ChatCategory, profile_uuid)
                .where(ChatCategory.server_uuid == server_uuid)
                .order_by(ChatCategory.sort_order)
            ).all()
            category_list = [ChatBackend.Category(category) for category in categories]
        return category_list

    @staticmethod
    def get_chats(profile_uuid: UUID, category_uuid: UUID):
        with Database.create_session() as session:
            chats = session.scalars(
                select_with_whitelist(Chat, profile_uuid)
                .where(Chat.category_uuid == category_uuid)
                .order_by(Chat.sort_order)
            ).all()
            chat_list = [ChatBackend.Chat(chat) for chat in chats]
        return chat_list

    @staticmethod
    def get_chat(profile_uuid: UUID, chat_uuid):
        if not isinstance(chat_uuid, UUID):
            try:
                chat_uuid = UUID(str(chat_uuid))
            except ValueError:
                return None
        with Database.create_session() as session:
            _chat = session.scalar(
                select_with_whitelist(Chat, profile_uuid)
                .where(Chat.uuid == chat_uuid)
            )
            if _chat is None:
                return None
            chat = ChatBackend.Chat(_chat)
        return chat

    @staticmethod
    def get_first_chat(profile_uuid: UUID, server_uuid: UUID):
        with Database.create_session() as session:
            _chat = session.scalars(
                select_with_whitelist(Chat, profile_uuid)
                .join(Chat.category)
                .where(ChatCategory.server_uuid == server_uuid)
                .order_by(ChatCategory.sort_order, Chat.sort_order)
            ).first()
            chat = ChatBackend.Chat(_chat)
        return chat

    @staticmethod
    @multithreaded
    def edit_category(uuid: UUID, **kwargs):
        with Database.create_session() as session:
            category = session.get(ChatCategory, uuid)
            for kw, value in kwargs.items():
                setattr(category, kw, value)
            session.add(category)
            session.commit()

    @staticmethod
    @multithreaded
    def edit_chat(uuid: UUID, **kwargs):
        with Database.create_session() as session:
            chat = session.get(Chat, uuid)
            for kw, value in kwargs.items():
                setattr(chat, kw, value)
            session.add(chat)
            session.commit()

    @staticmethod
    @multithreaded
    def reorder_category_list(server_uuid: UUID, new_order: list[UUID]):
        with Database.create_session() as session:
            categories = session.scalars(
                select(ChatCategory)
                .where(ChatCategory.server_uuid == server_uuid)
            ).all()
            category_map = {category.uuid: category for category in categories}
            for i, uuid in enumerate(new_order, start=1):
                category_map.pop(uuid).sort_order = i
            session.add_all(categories)
            session.commit()

    @staticmethod
    @multithreaded
    def reorder_chat_list(category_uuid: UUID, new_order: list[UUID]):
        with Database.create_session() as session:
            chats = session.scalars(
                select(Chat).where(Chat.uuid.in_(new_order))
            ).all()
            chat_map = {chat.uuid: chat for chat in chats}
            for i, uuid in enumerate(new_order, start=1):
                chat = chat_map.pop(uuid)
                chat.category_uuid = category_uuid
                chat.sort_order = i
            session.add_all(chats)
            session.commit()

    @staticmethod
    def create_category(server_uuid: UUID, name: str):
        with Database.create_session() as session:
            sort_order = (session.scalar(
                select(func.max(ChatCategory.sort_order))
                .where(ChatCategory.server_uuid == server_uuid)
            ) or 0) + 1
            whitelisted_roles = session.scalars(
                select(Role)
                .where(Role.server_uuid == server_uuid)
                .where(
                    (Role.sort_order == 0) | (Role.sort_order == (
                        select(func.max(Role.sort_order))
                        .where(Role.server_uuid == server_uuid)
                        .scalar_subquery()
                    ))
                )
            ).all()
            _category = ChatCategory(
                server_uuid=server_uuid,
                name=name, sort_order=sort_order,
                whitelisted_roles=whitelisted_roles
            )
            session.add(_category)
            session.commit()
            category = ChatBackend.Category(_category)
        return category

    @staticmethod
    def create_chat(category_uuid: UUID, name: str, voice_enabled=False):
        with Database.create_session() as session:
            sort_order = (session.scalar(
                select(func.max(Chat.sort_order))
                .where(Chat.category_uuid == category_uuid)
            ) or 0) + 1
            # noinspection PyTypeChecker
            whitelisted_roles = session.scalars(
                select(Role)
                .join(chat_category_roles, (
                    (chat_category_roles.c.role_uuid == Role.uuid)
                    & (chat_category_roles.c.category_uuid == category_uuid)
                ))
            ).all()
            _chat = Chat(
                category_uuid=category_uuid,
                name=name, sort_order=sort_order,
                voice_enabled=voice_enabled,
                whitelisted_roles=whitelisted_roles
            )
            session.add(_chat)
            session.commit()
            chat = ChatBackend.Chat(_chat)
        return chat

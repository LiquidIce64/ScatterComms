from uuid import UUID, uuid4
from datetime import datetime
from typing import List, Optional
from sqlalchemy import DateTime, ForeignKey, Table, Column
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class UUIDMixin:
    uuid: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)


class SortMixin:
    sort_order: Mapped[int] = mapped_column(nullable=False)


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class User(UUIDMixin, TimestampMixin, Base):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(nullable=False)
    about: Mapped[str] = mapped_column(nullable=True)
    owned_by_me: Mapped[bool] = mapped_column(nullable=False, default=False)

    member_of: Mapped[List['ServerMember']] = relationship(back_populates='user')


class Server(UUIDMixin, TimestampMixin, Base):
    __tablename__ = 'servers'

    name: Mapped[str] = mapped_column(nullable=False)
    selected_chat_uuid: Mapped[Optional['UUID']] = mapped_column(ForeignKey('chats.uuid'))

    members: Mapped[List['ServerMember']] = relationship(back_populates='server')
    roles: Mapped[List['Role']] = relationship(back_populates='server', cascade='all, delete-orphan')
    chat_categories: Mapped[List['ChatCategory']] = relationship(back_populates='server', cascade='all, delete-orphan')


class ServerSortOrder(SortMixin, Base):
    __tablename__ = 'server_sort_orders'

    server_uuid: Mapped[UUID] = mapped_column(ForeignKey('servers.uuid'), primary_key=True)
    user_uuid: Mapped[UUID] = mapped_column(ForeignKey('users.uuid'), primary_key=True)


class ServerMember(TimestampMixin, Base):
    __tablename__ = 'server_members'

    server_uuid: Mapped[UUID] = mapped_column(ForeignKey('servers.uuid'), primary_key=True)
    server: Mapped['Server'] = relationship(back_populates='members')

    user_uuid: Mapped[UUID] = mapped_column(ForeignKey('users.uuid'), primary_key=True)
    user: Mapped['User'] = relationship(back_populates='member_of')


user_roles = Table(
    'user_roles',
    Base.metadata,
    Column('user_uuid', ForeignKey('users.uuid'), primary_key=True, nullable=False),
    Column('role_uuid', ForeignKey('roles.uuid'), primary_key=True, nullable=False),
)


chat_category_roles = Table(
    'chat_category_roles',
    Base.metadata,
    Column('category_uuid', ForeignKey('chat_categories.uuid'), primary_key=True, nullable=False),
    Column('role_uuid', ForeignKey('roles.uuid'), primary_key=True, nullable=False),
)


chat_roles = Table(
    'chat_roles',
    Base.metadata,
    Column('chat_uuid', ForeignKey('chats.uuid'), primary_key=True, nullable=False),
    Column('role_uuid', ForeignKey('roles.uuid'), primary_key=True, nullable=False),
)


class Role(UUIDMixin, SortMixin, Base):
    __tablename__ = 'roles'

    name: Mapped[str] = mapped_column(nullable=False)
    color: Mapped[int] = mapped_column(nullable=False)
    public: Mapped[bool] = mapped_column(nullable=False, default=True)
    pingable: Mapped[bool] = mapped_column(nullable=False, default=False)

    server_uuid: Mapped[UUID] = mapped_column(ForeignKey('servers.uuid'))
    server: Mapped['Server'] = relationship(back_populates='roles')
    users: Mapped[List['User']] = relationship(secondary=user_roles)
    role_permissions: Mapped[List['RolePermission']] = relationship(back_populates='role', cascade='all, delete-orphan')


class RolePermission(Base):
    __tablename__ = 'role_permissions'

    role_uuid: Mapped[UUID] = mapped_column(ForeignKey('roles.uuid'), primary_key=True)
    role: Mapped['Role'] = relationship(back_populates='role_permissions')

    permission_uuid: Mapped[UUID] = mapped_column(ForeignKey('permissions.uuid'), primary_key=True)
    permission: Mapped['Permission'] = relationship()

    allowed: Mapped[bool] = mapped_column(nullable=False, default=True)
    forced: Mapped[bool] = mapped_column(nullable=False, default=False)


class Permission(UUIDMixin, SortMixin, Base):
    __tablename__ = 'permissions'

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)

    category_uuid: Mapped[UUID] = mapped_column(ForeignKey('permission_categories.uuid'))
    category: Mapped['PermissionCategory'] = relationship(back_populates='permissions')


class PermissionCategory(UUIDMixin, SortMixin, Base):
    __tablename__ = 'permission_categories'

    name: Mapped[str] = mapped_column(nullable=False)

    permissions: Mapped[List['Permission']] = relationship(back_populates='category')


class Chat(UUIDMixin, SortMixin, Base):
    __tablename__ = 'chats'

    name: Mapped[str] = mapped_column(nullable=False)
    voice_enabled: Mapped[bool] = mapped_column(nullable=False, default=False)

    category_uuid: Mapped[UUID] = mapped_column(ForeignKey('chat_categories.uuid'))
    category: Mapped['ChatCategory'] = relationship(back_populates='chats')
    whitelisted_roles: Mapped[List['Role']] = relationship(secondary=chat_roles)
    messages: Mapped[List['Message']] = relationship(back_populates='chat', cascade='all, delete-orphan')


class ChatCategory(UUIDMixin, SortMixin, Base):
    __tablename__ = 'chat_categories'

    name: Mapped[str] = mapped_column(nullable=False)
    collapsed: Mapped[bool] = mapped_column(nullable=False, default=False)

    server_uuid: Mapped[UUID] = mapped_column(ForeignKey('servers.uuid'))
    server: Mapped['Server'] = relationship(back_populates='chat_categories')
    whitelisted_roles: Mapped[List['Role']] = relationship(secondary=chat_category_roles)
    chats: Mapped[List['Chat']] = relationship(back_populates='category', cascade='all, delete-orphan')


class Message(UUIDMixin, TimestampMixin, Base):
    __tablename__ = 'messages'

    text: Mapped[str] = mapped_column(nullable=True)

    chat_uuid: Mapped[UUID] = mapped_column(ForeignKey('chats.uuid'))
    chat: Mapped['Chat'] = relationship(back_populates='messages')
    attachments: Mapped[List['Attachment']] = relationship(back_populates='message', cascade='all, delete-orphan')


class Attachment(UUIDMixin, SortMixin, Base):
    __tablename__ = 'attachments'

    uri: Mapped[str] = mapped_column(nullable=False)
    filename: Mapped[str] = mapped_column(nullable=False)

    message_uuid: Mapped[UUID] = mapped_column(ForeignKey('messages.uuid'))
    message: Mapped['Message'] = relationship(back_populates='attachments')

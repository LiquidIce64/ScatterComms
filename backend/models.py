from uuid import UUID, uuid4
from datetime import datetime
from typing import List
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase, declarative_base, Mapped, mapped_column, relationship


EmptyBase = declarative_base()


class Base(DeclarativeBase):
    uuid: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)


class SortMixin:
    sort_order: Mapped[int] = mapped_column(nullable=False)


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class Profile(EmptyBase):
    __tablename__ = 'profiles'

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped['User']


class User(TimestampMixin, Base):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(nullable=False)
    avatar_path: Mapped[str] = mapped_column(nullable=True)
    about: Mapped[str] = mapped_column(nullable=True)


class Server(TimestampMixin, Base):
    __tablename__ = 'servers'

    name: Mapped[str] = mapped_column(nullable=False)
    icon_path: Mapped[str] = mapped_column(nullable=False)

    members: Mapped[List['User']]
    roles: Mapped[List['Role']] = relationship(back_populates='server', cascade='all, delete-orphan')
    chat_categories: Mapped[List['ChatCategory']] = relationship(back_populates='server', cascade='all, delete-orphan')


class Role(SortMixin, Base):
    __tablename__ = 'roles'

    name: Mapped[str] = mapped_column(nullable=False)
    color: Mapped[int] = mapped_column(nullable=False)
    public: Mapped[bool] = mapped_column(nullable=False, default=True)

    server: Mapped['Server'] = relationship(back_populates='roles')
    members: Mapped[List['User']]
    role_permissions: Mapped[List['RolePermission']] = relationship(back_populates='role', cascade='all, delete-orphan')


class RolePermission(Base):
    __tablename__ = 'role_permissions'

    permission: Mapped['Permission']
    allowed: Mapped[bool] = mapped_column(nullable=False, default=True)
    forced: Mapped[bool] = mapped_column(nullable=False, default=False)

    role: Mapped['Role'] = relationship(back_populates='role_permissions')


class Permission(SortMixin, Base):
    __tablename__ = 'permissions'

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    category: Mapped['PermissionCategory']


class PermissionCategory(SortMixin, Base):
    __tablename__ = 'permission_categories'

    name: Mapped[str] = mapped_column(nullable=False)


class Chat(SortMixin, Base):
    __tablename__ = 'chats'

    name: Mapped[str] = mapped_column(nullable=False)
    voice_enabled: Mapped[bool] = mapped_column(nullable=False, default=False)

    category: Mapped['ChatCategory'] = relationship(back_populates='chats')
    whitelisted_roles: Mapped[List['Role']]
    messages: Mapped[List['Message']] = relationship(back_populates='chat', cascade='all, delete-orphan')


class ChatCategory(SortMixin, Base):
    __tablename__ = 'chat_categories'

    name: Mapped[str] = mapped_column(nullable=False)

    server: Mapped['Server'] = relationship(back_populates='chat_categories')
    whitelisted_roles: Mapped[List['Role']]
    chats: Mapped[List['ChatCategory']] = relationship(back_populates='category', cascade='all, delete-orphan')


class Message(TimestampMixin, Base):
    __tablename__ = 'messages'

    text: Mapped[str] = mapped_column(nullable=True)

    chat: Mapped['Chat'] = relationship(back_populates='messages')
    attachments: Mapped[List['Attachment']] = relationship(back_populates='message', cascade='all, delete-orphan')


class Attachment(SortMixin, Base):
    __tablename__ = 'attachments'

    uri: Mapped[str] = mapped_column(nullable=False)
    path: Mapped[str] = mapped_column(nullable=True)

    message: Mapped['Message'] = relationship(back_populates='attachments')

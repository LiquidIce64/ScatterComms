from typing import Union
from uuid import UUID
from sqlalchemy import select

from PySide6.QtGui import QImage, QPixmap

from .multithreading import multithreaded
from .storage import StorageBackend
from .cached_object import CachedObject
from database import Database, Server


class ServerBackend:
    class Server(CachedObject):
        def __init__(self, server):
            if hasattr(self, '_Server__uuid'):
                return  # already initialized
            super().__init__()
            self.__uuid: UUID = server.uuid
            self.__name: str = server.name
            self.__icon = StorageBackend.Server.get_icon(self.uuid)

        def update(self, server):
            self.__uuid: UUID = server.uuid
            self.__name: str = server.name
            self.__icon = StorageBackend.Server.get_icon(self.uuid)
            self.changed.emit()

        @property
        def uuid(self): return self.__uuid
        @property
        def name(self): return self.__name
        @property
        def icon(self): return self.__icon

        @name.setter
        def name(self, new_value: str):
            self.__name = new_value
            ServerBackend.edit_server(self.__uuid, name=new_value)
            self.changed.emit()

        @icon.setter
        def icon(self, new_value: Union[QImage, QPixmap]):
            if isinstance(new_value, QPixmap):
                new_value = new_value.toImage()
            self.__icon = new_value
            StorageBackend.Server.set_icon(self.__uuid, new_value)
            self.changed.emit()

    @staticmethod
    def get_server_list_pinned():
        with Database.create_session() as session:
            servers = session.scalars(
                select(Server)
                .where(Server.sort_order > 0)
                .order_by(Server.sort_order)
            ).all()
            server_list = [ServerBackend.Server(server) for server in servers]
        return server_list

    @staticmethod
    def get_server_list_unpinned():
        with Database.create_session() as session:
            servers = session.scalars(
                select(Server)
                .where(Server.sort_order == 0)
                .order_by(Server.created_at)
            ).all()
            server_list = [ServerBackend.Server(server) for server in servers]
        return server_list

    @staticmethod
    @multithreaded
    def edit_server(uuid: UUID, **kwargs):
        with Database.create_session() as session:
            server = session.get(Server, uuid)
            for kw, value in kwargs.items():
                setattr(server, kw, value)
            session.add(server)
            session.commit()

    @staticmethod
    @multithreaded
    def reorder_server_list(new_order: list[UUID]):
        with Database.create_session() as session:
            servers = session.scalars(select(Server).where(Server.uuid.in_(new_order))).all()
            server_map = {server.uuid: server for server in servers}
            for i, uuid in enumerate(new_order, start=1):
                server_map[uuid].sort_order = i
            session.add_all(servers)
            session.commit()

    @staticmethod
    def create_server(name: str):
        with Database.create_session() as session:
            _server = Server(name=name, sort_order=0)
            session.add(_server)
            server = ServerBackend.Server(_server)
            session.commit()
        return server

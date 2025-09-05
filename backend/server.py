from uuid import UUID
from sqlalchemy import select
from database import Database, Server


class ServerBackend:
    class Server:
        def __init__(self, server):
            self.uuid: UUID = server.uuid
            self.name: str = server.name

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
    def reorder_server(uuid: UUID, new_sort_order: int):
        with Database.create_session() as session:
            server = session.scalar(select(Server).where(Server.uuid == uuid))
            server.sort_order = new_sort_order
            session.add(server)
            session.commit()

    @staticmethod
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

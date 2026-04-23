from typing import cast, TYPE_CHECKING, Optional

from backend.base import BaseBackend
from .multi_socket import MultiSocket


if TYPE_CHECKING:
    from backend.config import ConfigBackend


class NetBackend(BaseBackend):
    socket: Optional[MultiSocket] = None

    @classmethod
    def init(cls):
        backend = BaseBackend.get_backend('ConfigBackend')
        if TYPE_CHECKING:
            backend = cast(ConfigBackend, backend)
        if cls.socket is not None:
            cls.socket.deleteLater()
            cls.socket = None
        if backend.session.profile is not None:
            cls.socket = MultiSocket(backend.session.listen_port)
            cls.socket.setParent(backend.session)

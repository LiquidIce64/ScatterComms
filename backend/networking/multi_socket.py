from typing import cast
from PySide6.QtCore import QObject
from PySide6.QtNetwork import QSslSocket, QSslServer, QHostAddress


class MultiSocket(QObject):
    def __init__(self, listen_port: int):
        super().__init__()

        self.server = QSslServer(parent=self)
        self.clients: list[QSslSocket] = []

        self.server.newConnection.connect(self.__on_new_connection)
        if not self.server.listen(address=QHostAddress.SpecialAddress.Any, port=listen_port):
            raise RuntimeError(f'[DEBUG] Server failed to start listening: {self.server.errorString()}')

        print(f'[DEBUG] Server listening on port {self.server.serverPort()}')

    def __on_new_connection(self):
        socket = cast(QSslSocket, self.server.nextPendingConnection())
        if not socket: return

        socket.sslErrors.connect(self.__on_ssl_errors)
        socket.errorOccurred.connect(self.__on_connection_error)
        socket.encrypted.connect(self.__on_successful_connect)
        socket.disconnected.connect(socket.deleteLater)

        socket.startServerEncryption()

    def try_connect(self, hostname: str, port: int):
        socket = QSslSocket(parent=self)

        socket.sslErrors.connect(self.__on_ssl_errors)
        socket.errorOccurred.connect(self.__on_connection_error)
        socket.encrypted.connect(self.__on_successful_connect)
        socket.disconnected.connect(socket.deleteLater)

        socket.connectToHostEncrypted(hostname, port)

    def __on_successful_connect(self):
        socket = cast(QSslSocket, self.sender())
        self.clients.append(socket)
        print(f'[DEBUG] {socket.peerAddress()} connected')

    def __on_ssl_errors(self, errors):
        socket = cast(QSslSocket, self.sender())
        for error in errors:
            print(f'[DEBUG] SSL Error: {error.errorString()}')

        socket.ignoreSslErrors()

    @staticmethod
    def __on_connection_error(error):
        print(f'[DEBUG] Connection Error: {error.errorString()}')

    def deleteLater(self):
        print(f'[DEBUG] Server closing')
        for client in self.clients:
            client.close()
            client.deleteLater()
        self.server.close()
        self.server.deleteLater()
        super().deleteLater()

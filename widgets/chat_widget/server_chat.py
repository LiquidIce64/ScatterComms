from PySide6.QtWidgets import QWidget

from .ui_server_chat import Ui_server_chat


class ServerChat(QWidget, Ui_server_chat):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

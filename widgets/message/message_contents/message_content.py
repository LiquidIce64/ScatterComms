from PySide6.QtWidgets import QWidget, QVBoxLayout

from backend import MessageBackend


class MessageContent(QWidget):
    def __init__(self, message: MessageBackend.Message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

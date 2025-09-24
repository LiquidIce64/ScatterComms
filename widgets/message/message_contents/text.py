from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel

from backend import MessageBackend
from .message_content import MessageContent


class TextContent(MessageContent):
    def __init__(self, message: MessageBackend.Message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        label = QLabel(text=message.text, parent=self)
        label.setObjectName('label_text')
        label.setAlignment(Qt.AlignmentFlag.AlignTop and Qt.AlignmentFlag.AlignLeft)
        label.setOpenExternalLinks(True)
        label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.layout.addWidget(label)

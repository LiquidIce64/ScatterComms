from PySide6.QtWidgets import QWidget

from .ui_chat_widget import Ui_chat_widget
from resources import Icons


class ChatWidget(QWidget, Ui_chat_widget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.max_textbox_height = self.textbox.maximumHeight()
        self.textbox.document().documentLayout().documentSizeChanged.connect(self.update_textbox_height)
        self.textbox.textChanged.connect(lambda: (
            self.btn_send.setEnabled(not self.textbox.document().isEmpty())
        ))

        self.btn_attachment.setIcon(Icons.plus)
        self.btn_emoji.setIcon(Icons.emoji)
        self.btn_send.setIcon(Icons.send)

    def update_textbox_height(self):
        new_height = self.textbox.document().size().height()
        new_height = min(new_height, self.max_textbox_height)
        new_height = max(new_height, self.textbox.minimumHeight())
        self.textbox.setMaximumHeight(new_height)

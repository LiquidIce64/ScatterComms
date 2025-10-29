from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGraphicsColorizeEffect, QLabel
from PySide6.QtGui import QColor

from .ui_message_widget import Ui_message_widget
from widgets.message.reply_widget import ReplyWidget
from widgets.message.attachment import get_attachment_widget
from resources import Icons
from backend import MessageBackend


class MessageWidget(QWidget, Ui_message_widget):
    def __init__(self, message: MessageBackend.Message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.icon_avatar.painter_mask = self.icon_avatar.CircleMask()
        self.role_color_effect = QGraphicsColorizeEffect(parent=self.label_username, color=QColor.fromRgba(0xFF808080))
        self.label_username.setGraphicsEffect(self.role_color_effect)

        self.message = message
        self.profile = message.author
        self.update_profile_info()
        self.profile.changed.connect(self.update_profile_info)
        self.update_role_info()
        self.profile.top_role_changed.connect(self.update_role_info)
        self.reload_contents()
        self.message.changed.connect(self.reload_contents)
        self.label_timestamp.setText(message.created_at.strftime('%H:%M %d.%m.%Y'))
        if (replying_to := message.replying_to) is not None:
            self.layout_reply.addWidget(ReplyWidget(replying_to))

    def update_profile_info(self):
        self.icon_avatar.setPixmap(self.profile.avatar or Icons.Profile.Avatar)
        self.label_username.setText(self.profile.username)

    def update_role_info(self):
        if self.profile.top_role is None:
            self.role_color_effect.setColor(QColor.fromRgba(0xFF808080))
        else:
            self.role_color_effect.setColor(self.profile.top_role.color)

    def reload_contents(self):
        for i in range(self.layout_contents.count() - 1, -1, -1):
            w = self.layout_contents.itemAt(i).widget()
            if w is not None:
                w.deleteLater()

        text = self.message.text
        if text is not None:
            label_text = QLabel(
                text=self.message.text,
                parent=self,
                wordWrap=True,
                openExternalLinks=True,
                textInteractionFlags=Qt.TextInteractionFlag.TextBrowserInteraction
            )
            label_text.setObjectName('label_text')
            self.layout_contents.addWidget(label_text)
        else:
            self.layout_contents.setContentsMargins(0, 6, 0, 0)

        for attachment in self.message.attachments:
            widget = get_attachment_widget(attachment)
            widget.setParent(self)
            self.layout_contents.addWidget(widget)

    def deleteLater(self):
        for i in range(self.layout_contents.count() - 1, -1, -1):
            w = self.layout_contents.itemAt(i).widget()
            if w is not None:
                w.deleteLater()
        super().deleteLater()

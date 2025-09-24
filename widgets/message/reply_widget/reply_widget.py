from PySide6.QtWidgets import QWidget, QGraphicsColorizeEffect
from PySide6.QtGui import QColor

from .ui_reply_widget import Ui_reply_widget
from resources import Icons
from backend import MessageBackend, RoleBackend, ConfigBackend


class ReplyWidget(QWidget, Ui_reply_widget):
    def __init__(self, message: MessageBackend.Message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.icon_avatar.painter_mask = self.icon_avatar.CircleMask()
        self.role_color_effect = QGraphicsColorizeEffect(parent=self.label_username, color=QColor.fromRgba(0xFF808080))
        self.label_username.setGraphicsEffect(self.role_color_effect)
        self.btn.focused.connect(self.update_highlight)
        self.btn.focusLost.connect(self.update_highlight)
        self.btn.hovered.connect(self.update_highlight)
        self.btn.hoverEnd.connect(self.update_highlight)

        self.message = message
        self.profile = message.author
        self.update_profile_info()
        self.profile.changed.connect(self.update_profile_info)
        self.update_message_info()
        self.message.changed.connect(self.update_message_info)

        self.role: RoleBackend.Role | None = None
        self.__connect_role(RoleBackend.get_top_role(self.profile.uuid, ConfigBackend.session.selected_server.uuid))

    def update_highlight(self):
        highlight = self.btn.hasFocus() or self.btn.underMouse()
        self.line.setProperty('highlight', highlight)
        self.line.style().polish(self.line)
        self.label_message.setProperty('highlight', highlight)
        self.label_message.style().polish(self.label_message)

    def __connect_role(self, role: RoleBackend.Role | None):
        if role is None:
            return
        self.role = role
        self.update_role_info()
        role.changed.connect(self.update_role_info)

    def update_profile_info(self):
        self.icon_avatar.setPixmap(self.profile.avatar or Icons.Avatar)
        self.label_username.setText(self.profile.username)

    def update_role_info(self):
        self.role_color_effect.setColor(self.role.color)

    def update_message_info(self):
        text = self.message.text
        if text is not None:
            self.label_message.setText(text)

from PySide6.QtWidgets import QWidget, QGraphicsColorizeEffect
from PySide6.QtGui import QColor

from .ui_message_widget import Ui_message_widget
from widgets.message.reply_widget import ReplyWidget
from resources import Icons
from backend import ProfileBackend, RoleBackend, ConfigBackend


class MessageWidget(QWidget, Ui_message_widget):
    def __init__(self, profile: ProfileBackend.Profile, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.icon_avatar.painter_mask = self.icon_avatar.CircleMask()
        self.role_color_effect = QGraphicsColorizeEffect(parent=self.label_username, color=QColor.fromRgba(0xFF808080))
        self.label_username.setGraphicsEffect(self.role_color_effect)

        self.profile = profile
        self.update_profile_info()
        profile.changed.connect(self.update_profile_info)

        self.role: RoleBackend.Role | None = None
        self.__connect_role(RoleBackend.get_top_role(profile.uuid, ConfigBackend.session.selected_server.uuid))

        # Debug
        self.layout_reply.addWidget(ReplyWidget(profile))

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

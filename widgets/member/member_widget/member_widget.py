from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QGraphicsColorizeEffect

from .ui_member_widget import Ui_member_widget
from resources import Icons
from backend import ProfileBackend


class MemberWidget(QWidget, Ui_member_widget):
    def __init__(self, profile: ProfileBackend.Profile, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.icon_avatar.painter_mask = self.icon_avatar.AvatarMask(self.icon_status.size())
        self.icon_status.setIcon(Icons.Status.Online)
        self.role_color_effect = QGraphicsColorizeEffect(parent=self.label_username, color=QColor.fromRgba(0xFF808080))
        self.label_username.setGraphicsEffect(self.role_color_effect)

        self.profile = profile
        self.update_profile_info()
        profile.changed.connect(self.update_profile_info)
        self.update_role_info()
        self.profile.top_role_changed.connect(self.update_role_info)

        # Debug
        self.label_status.hide()

    def update_profile_info(self):
        self.icon_avatar.setPixmap(self.profile.avatar or Icons.Profile.Avatar)
        self.label_username.setText(self.profile.username)

    def update_role_info(self):
        if self.profile.top_role is None:
            self.role_color_effect.setColor(QColor.fromRgba(0xFF808080))
        else:
            self.role_color_effect.setColor(self.profile.top_role.color)

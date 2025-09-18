from PySide6.QtWidgets import QWidget

from .ui_member_widget import Ui_member_widget
from resources import Icons
from backend import ProfileBackend


class MemberWidget(QWidget, Ui_member_widget):
    def __init__(self, profile: ProfileBackend.Profile, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.icon_avatar.painter_mask = self.icon_avatar.AvatarMask(self.icon_status.size())
        self.icon_status.setIcon(Icons.Status.Online)

        self.profile = profile
        self.update_profile_info()
        profile.changed.connect(self.update_profile_info)

        # Debug
        self.label_status.hide()

    def update_profile_info(self):
        self.icon_avatar.setPixmap(self.profile.avatar or Icons.Avatar)
        self.label_username.setText(self.profile.username)

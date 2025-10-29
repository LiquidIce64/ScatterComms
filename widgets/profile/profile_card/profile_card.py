from PySide6.QtWidgets import QWidget

from .ui_profile_card import Ui_profile_card
from resources import Icons
from backend import ProfileBackend


class ProfileCard(QWidget, Ui_profile_card):
    def __init__(self, profile: ProfileBackend.Profile, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.icon_avatar.painter_mask = self.icon_avatar.CircleMask()
        self.icon_avatar.setPixmap(profile.avatar or Icons.Profile.Avatar)
        self.label_username.setText(profile.username)

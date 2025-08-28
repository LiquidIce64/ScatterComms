from PySide6.QtWidgets import QWidget

from .ui_profile_card import Ui_profile_card


class ProfileCard(QWidget, Ui_profile_card):
    def __init__(self, profile, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.label_username.setText(profile.username)

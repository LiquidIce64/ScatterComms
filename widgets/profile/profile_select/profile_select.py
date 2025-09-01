from PySide6.QtWidgets import QWidget, QInputDialog

from .ui_profile_select import Ui_profile_select
from widgets.profile.profile_card import ProfileCard
from resources import Icons
from backend import ProfileBackend


class ProfileSelect(QWidget, Ui_profile_select):
    def __init__(self, main_window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.main_window = main_window

        self.icon_create.setIcon(Icons.plus)
        self.btn_create.clicked.connect(self.create_profile)

        for profile in ProfileBackend.get_profiles():
            self.add_profile_card(profile)

    def add_profile_card(self, profile: ProfileBackend.Profile):
        card = ProfileCard(profile)
        self.layout_profiles.insertWidget(self.layout_profiles.count() - 2, card)
        card.btn.clicked.connect(lambda: self.select_profile(profile))

    def create_profile(self):
        while True:
            username, ok = QInputDialog.getText(self, 'Create new profile', 'Username:')
            if not ok:
                return
            if username:
                break
        profile = ProfileBackend.create_profile(username)
        self.add_profile_card(profile)

    def select_profile(self, profile):
        self.main_window.switch_to(self.main_window.Page.Main)

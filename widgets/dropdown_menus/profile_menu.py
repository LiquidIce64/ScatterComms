from PySide6.QtWidgets import QFrame

from .menu_widget import MenuWidget
from resources import Icons
from backend import ProfileBackend, ConfigBackend


class ProfileMenu(MenuWidget):
    grid_layout_args = (1, 3, 1, 1)
    _left_side_icons = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.btn_online = self.add_button('Online', Icons.Status.Online, 6)
        self.btn_away = self.add_button('Away', Icons.Status.Away, 6)
        self.btn_do_not_disturb = self.add_button('Do Not Disturb', Icons.Status.DoNotDisturb, 6)
        self.btn_invisible = self.add_button('Invisible', Icons.Status.Offline, 6)

        self.divider = QFrame(frameShape=QFrame.Shape.HLine)
        self.divider.setStyleSheet('color: #353535;')
        self.layout_menu.addWidget(self.divider)

        self.btn_edit_profile = self.add_button('Edit Profile', Icons.Edit)
        self.btn_change_profile = self.add_button('Change Profile', Icons.User)

    def connect_button_signals(self, main_page):
        self.btn_change_profile.clicked.connect(
            lambda: main_page.main_window.switch_to(main_page.main_window.Page.Profiles))

        def set_status(status):
            ConfigBackend.session.status = status

        self.btn_online.clicked.connect(
            lambda: set_status(ProfileBackend.Status.Online))
        self.btn_away.clicked.connect(
            lambda: set_status(ProfileBackend.Status.Away))
        self.btn_do_not_disturb.clicked.connect(
            lambda: set_status(ProfileBackend.Status.DoNotDisturb))
        self.btn_invisible.clicked.connect(
            lambda: set_status(ProfileBackend.Status.Offline))

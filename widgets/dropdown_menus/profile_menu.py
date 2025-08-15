from PySide6.QtWidgets import QFrame

from .menu_widget import MenuWidget
from resources import Icons


class ProfileMenu(MenuWidget):
    def setupButtons(self):
        self.btn_online = self.add_button('Online', Icons.Status.online, 6)
        self.btn_away = self.add_button('Away', Icons.Status.away, 6)
        self.btn_do_not_disturb = self.add_button('Do Not Disturb', Icons.Status.do_not_disturb, 6)
        self.btn_invisible = self.add_button('Invisible', Icons.Status.offline, 6)

        self.divider = QFrame(frameShape=QFrame.Shape.HLine)
        self.divider.setStyleSheet('color: #353535;')
        self.layout_menu.addWidget(self.divider)

        self.btn_edit_profile = self.add_button('Edit Profile', Icons.edit, 2)
        self.btn_change_user = self.add_button('Change User', Icons.user, 2)

        # debug
        self.btn_online.clicked.connect(
            lambda: self.main_page.icon_userstatus.setIcon(Icons.Status.online))
        self.btn_away.clicked.connect(
            lambda: self.main_page.icon_userstatus.setIcon(Icons.Status.away))
        self.btn_do_not_disturb.clicked.connect(
            lambda: self.main_page.icon_userstatus.setIcon(Icons.Status.do_not_disturb))
        self.btn_invisible.clicked.connect(
            lambda: self.main_page.icon_userstatus.setIcon(Icons.Status.offline))

    def attach(self):
        self.main_page.layout_main_page.addWidget(self, 1, 3, 1, 1)
        self.main_page.btn_profile.setFocusProxy(self)

    def focusOutEvent(self, event):
        self.main_page.btn_profile.setChecked(False)

from PySide6.QtWidgets import QFrame

from .menu_widget import MenuButton, MenuWidget
from resources import Icons


class ProfileMenu(MenuWidget):
    def setupButtons(self):
        self.btn_online = self._add_button('Online', Icons.Status.online, 6)
        self.btn_away = self._add_button('Away', Icons.Status.away, 6)
        self.btn_do_not_disturb = self._add_button('Do Not Disturb', Icons.Status.do_not_disturb, 6)
        self.btn_invisible = self._add_button('Invisible', Icons.Status.offline, 6)

        self.divider = QFrame(frameShape=QFrame.Shape.HLine)
        self.divider.setStyleSheet('color: #353535;')
        self.layout_menu.addWidget(self.divider)

        self.btn_edit_profile = self._add_button('Edit Profile', Icons.edit, 2)
        self.btn_change_user = self._add_button('Change User', Icons.user, 2)

    def _add_button(self, label=None, icon=None, margin=0):
        btn = MenuButton(label, icon, invert_layout=True)
        if margin > 0:
            btn.icon.setStyleSheet(f'margin:{margin}px;')
        self.layout_menu.addWidget(btn)
        return btn

    def attach(self):
        self.main_page.layout_main_page.addWidget(self, 1, 3, 1, 1)
        self.main_page.btn_profile.setFocusProxy(self)

    def focusOutEvent(self, event):
        self.main_page.btn_profile.btn.setChecked(False)

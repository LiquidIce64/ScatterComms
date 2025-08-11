from PySide6.QtWidgets import QFrame

from .menu_widget import MenuButton, MenuWidget


class ProfileMenu(MenuWidget):
    def setupButtons(self):
        self.btn_online = self._add_button("Online")
        self.btn_away = self._add_button("Away")
        self.btn_do_not_disturb = self._add_button("Do Not Disturb")
        self.btn_invisible = self._add_button("Invisible")

        self.divider = QFrame(frameShape=QFrame.Shape.HLine)
        self.divider.setStyleSheet("color: #353535;")
        self.layout_menu.addWidget(self.divider)

        self.btn_edit_profile = self._add_button("Edit Profile")
        self.btn_change_user = self._add_button("Change User")

    def _add_button(self, label=None, icon=None):
        btn = MenuButton(label, icon, invert_layout=True)
        self.layout_menu.addWidget(btn)
        return btn

    def attach(self):
        self.main_page.layout_main_page.addWidget(self, 1, 3, 1, 1)

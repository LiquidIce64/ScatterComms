from PySide6.QtWidgets import QWidget

from .ui_member_category import Ui_member_category
from widgets.member.member_widget import MemberWidget
from backend import RoleBackend, ProfileBackend


class MemberCategoryWidget(QWidget, Ui_member_category):
    def __init__(self, role: RoleBackend.Role = None, members: list[ProfileBackend.Profile] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.role = role
        if role is not None:
            self.update_role_info()
            role.changed.connect(self.update_role_info)
        if members is not None:
            for member in members:
                self.add_member(member)

    def update_role_info(self):
        self.label_name.setText(self.role.name)

    def add_member(self, profile: ProfileBackend.Profile):
        username = profile.username
        uuid = profile.uuid
        i = 0
        for i in range(self.layout_members.count()):
            w = self.layout_members.itemAt(i).widget()
            if isinstance(w, MemberWidget) and (w.profile.username > username or w.profile.uuid > uuid):
                break
        self.layout_members.insertWidget(i, MemberWidget(profile, parent=self))
        self.label_count.setText(str(self.layout_members.count()))

from typing import TYPE_CHECKING

from PySide6.QtWidgets import QWidget

from .ui_vc_info import Ui_vc_info

if TYPE_CHECKING:
    from widgets.main_page import MainPage


class VCInfo(QWidget, Ui_vc_info):
    def __init__(self, main_page: 'MainPage', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.main_page = main_page
        main_page.layout_main_page.addWidget(self, 2, 0, 1, 2)

        self.__modify_margins(main_page.frame_servers.layout(), self.height())
        self.__modify_margins(main_page.frame_side_panel.layout(), self.height())

        self.btn_disconnect.clicked.connect(self.leave_vc)

    @staticmethod
    def __modify_margins(layout, dy):
        margins = layout.contentsMargins()
        margins.setBottom(margins.bottom() + dy)
        layout.setContentsMargins(margins)

    def leave_vc(self):
        self.__modify_margins(self.main_page.frame_servers.layout(), -self.height())
        self.__modify_margins(self.main_page.frame_side_panel.layout(), -self.height())

        self.deleteLater()

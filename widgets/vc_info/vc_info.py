from PySide6.QtWidgets import QWidget

from .ui_vc_info import Ui_vc_info


class VCInfo(QWidget, Ui_vc_info):
    def __init__(self, main_page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.main_page = main_page
        main_page.layout_main_page.addWidget(self, 2, 0, 1, 2)
        main_page.spacer_servers_offset.changeSize(0, self.height())
        main_page.spacer_side_panel.changeSize(0, self.height())

        self.btn_disconnect.clicked.connect(self.deleteLater)

    def deleteLater(self):
        self.main_page.spacer_servers_offset.changeSize(0, 0)
        self.main_page.spacer_side_panel.changeSize(0, 0)
        super().deleteLater()

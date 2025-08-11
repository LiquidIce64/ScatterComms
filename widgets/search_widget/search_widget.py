from PySide6.QtWidgets import QWidget

from .ui_search_widget import Ui_search_widget


class SearchWidget(QWidget, Ui_search_widget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.hide()

    def toggle(self):
        self.setHidden(not self.isHidden())

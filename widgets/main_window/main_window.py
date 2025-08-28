from enum import Enum

from PySide6.QtWidgets import QMainWindow

from widgets.main_page import MainPage
from widgets.profile import ProfileSelect


class MainWindow(QMainWindow):
    class Page(Enum):
        Main = MainPage
        Profiles = ProfileSelect

    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenComms")

        self.switch_to(self.Page.Main)

    def switch_to(self, page: Page):
        current_page = self.centralWidget()
        if current_page is not None:
            current_page.deleteLater()
        self.setCentralWidget(page.value(self))

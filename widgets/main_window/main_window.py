from enum import Enum

from PySide6.QtWidgets import QMainWindow

from widgets.main_page import MainPage
from widgets.profile import ProfileSelect
from backend import ConfigBackend


class MainWindow(QMainWindow):
    class Page(Enum):
        Main = MainPage
        Profiles = ProfileSelect

    def __init__(self):
        super().__init__()
        self.setWindowTitle('OpenComms')

        self.session = ConfigBackend.Session()

        if self.session.geometry is not None:
            self.restoreGeometry(self.session.geometry)
        if self.session.state is not None:
            self.restoreState(self.session.state)

        self.switch_to(self.Page.Profiles if self.session.profile is None else self.Page.Main)

    def switch_to(self, page: Page):
        current_page = self.centralWidget()
        if current_page is not None:
            current_page.deleteLater()
        self.setCentralWidget(page.value(self))

    def closeEvent(self, event):
        self.session.geometry = self.saveGeometry()
        self.session.state = self.saveState()
        self.session.save()

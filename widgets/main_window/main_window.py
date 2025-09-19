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
        self.setWindowTitle('ScatterComms')

        ConfigBackend.session = ConfigBackend.Session()
        ConfigBackend.session.setParent(self)

        if ConfigBackend.session.geometry is not None:
            self.restoreGeometry(ConfigBackend.session.geometry)
        if ConfigBackend.session.state is not None:
            self.restoreState(ConfigBackend.session.state)

        self.switch_to(self.Page.Profiles if ConfigBackend.session.profile is None else self.Page.Main)

    def switch_to(self, page: Page):
        current_page = self.centralWidget()
        if current_page is not None:
            current_page.deleteLater()
        self.setCentralWidget(page.value(self))

    def closeEvent(self, event):
        ConfigBackend.session.geometry = self.saveGeometry()
        ConfigBackend.session.state = self.saveState()
        ConfigBackend.session.save()
        ConfigBackend.session.setParent(None)
        ConfigBackend.session = None

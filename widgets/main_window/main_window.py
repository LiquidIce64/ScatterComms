from PySide6.QtWidgets import QMainWindow

from widgets.main_page import MainPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenComms")

        self.current_page = MainPage()
        self.setCentralWidget(self.current_page)

import sys
from PySide6.QtWidgets import QApplication

from backend import StorageBackend
from database import Database
from widgets import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName('OpenComms')

    StorageBackend.init(test_mode='--test-appdata' in sys.argv)
    Database.init(StorageBackend.locate_appdata_file('app_database.db', allow_empty=False))

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

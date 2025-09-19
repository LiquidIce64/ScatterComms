import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QLockFile

from backend import StorageBackend
from database import Database
from widgets import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName('ScatterComms')

    StorageBackend.init(test_mode='--test-appdata' in sys.argv)
    lockfile = QLockFile(StorageBackend.locate_appdata('.lock', allow_empty=False))
    if not lockfile.tryLock(0):
        pid = lockfile.getLockInfo()[0]
        print(f'Lockfile in use by process {pid}')
        exit(1)
    Database.init(StorageBackend.locate_appdata('app_database.db', allow_empty=False))

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

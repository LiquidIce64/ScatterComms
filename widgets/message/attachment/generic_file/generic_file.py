import os
import math

from PySide6.QtWidgets import QFrame, QFileDialog, QApplication
from PySide6.QtCore import QFile, QStandardPaths, Qt

from .ui_generic_file import Ui_generic_file_widget
from widgets.message.attachment.attachment_widget import AttachmentWidget, register
from backend import MessageBackend
from resources import Icons


def format_file_size(size: int):
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    unit_ind = min(
        int(math.log(size, 1024)),
        len(units)-1
    ) if size > 0 else 0
    value = size / (1024 ** unit_ind)
    unit = QApplication.translate('file_size', units[unit_ind])
    return f'{value:.{0 if unit_ind == 0 else 1}f}\xa0{unit}'


@register('*')
class GenericFileWidget(QFrame, AttachmentWidget, Ui_generic_file_widget):
    def __init__(self, attachment: MessageBackend.Attachment):
        super().__init__(attachment=attachment)
        self.setupUi(self)
        self.btn_download.setIcon(Icons.Generic.Download)
        filename = attachment.filename
        self.btn_file.setText(filename)
        self.btn_file.setToolTip(filename)
        self.icon.setIcon(self.get_thumbnail(filename))
        self.label.setText(format_file_size(attachment.filesize))
        path = self.attachment.filepath
        if path is not None:
            self.on_downloaded(path)
        else:
            self.btn_download.clicked.connect(self.download)

    def on_downloaded(self, filepath: str):
        self.btn_download.deleteLater()
        del self.btn_download
        file_size = os.path.getsize(filepath)
        self.label.setText(format_file_size(file_size))
        self.btn_file.setEnabled(True)
        self.btn_file.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_file.clicked.connect(self.save_file)

    def save_file(self):
        downloads_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DownloadLocation)
        new_filepath = QFileDialog.getSaveFileName(
            parent=self,
            caption=QApplication.translate('file_dialog', 'Save file'),
            dir=f'{downloads_dir}/{self.attachment.filename}'
        )[0]
        if new_filepath:
            QFile.copy(self.attachment.filepath, new_filepath)

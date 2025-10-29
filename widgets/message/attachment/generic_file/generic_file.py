import os

from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Qt

from .ui_generic_file import Ui_generic_file_widget
from widgets.message.attachment.attachment_widget import AttachmentWidget, register
from widgets.internal import format_file_size
from backend import MessageBackend
from resources import Icons


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
        self.btn_file.clicked.connect(self.save_attachment)

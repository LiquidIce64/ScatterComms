from PySide6.QtWidgets import QLabel, QSizePolicy
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap

from .attachment_widget import AttachmentWidget, register
from backend.attachment import AttachmentBackend


@register(
    '.tif', '.tiff',
    '.bmp', '.png', '.webp',
    '.jpg', '.jpeg', '.jpe', '.jif', '.jfif', '.jfi',
)
class ImageWidget(QLabel, AttachmentWidget):
    MAX_IMAGE_SIZE = QSize(1024, 400)

    def __init__(self, attachment: AttachmentBackend.Attachment):
        super().__init__(attachment=attachment)
        self.setScaledContents(True)
        policy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        policy.setHeightForWidth(True)
        self.setSizePolicy(policy)
        self.load_file()

    def on_load(self, filepath: str):
        pixmap = QPixmap(filepath)
        new_size = pixmap.size()
        if new_size.width() > self.MAX_IMAGE_SIZE.width() or new_size.height() > self.MAX_IMAGE_SIZE.height():
            new_size.scale(self.MAX_IMAGE_SIZE, Qt.AspectRatioMode.KeepAspectRatio)
        self.setMaximumSize(new_size)
        self.setPixmap(pixmap)

    def heightForWidth(self, width):
        width = min(width, self.maximumWidth())
        pixmap = self.pixmap()
        if pixmap.width() == 0:
            return 0
        height = int(width * pixmap.height() / pixmap.width())
        return height

    def sizeHint(self): return self.maximumSize()
    def minimumSizeHint(self): return self.minimumSize()

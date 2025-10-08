from PySide6.QtWidgets import QLabel, QSizePolicy
from PySide6.QtCore import Qt, QSize, QPoint
from PySide6.QtGui import QPixmap, QPainter, QImage

from .attachment_widget import AttachmentWidget, register
from backend import MessageBackend, run_task


def crop_pixmap(pixmap: QPixmap):
    square_size = min(pixmap.width(), pixmap.height())
    cropped_pixmap = QPixmap(square_size, square_size)
    cropped_pixmap.fill(Qt.GlobalColor.transparent)
    source_rect = cropped_pixmap.rect()
    source_rect.moveCenter(pixmap.rect().center())
    QPainter(cropped_pixmap).drawPixmap(QPoint(0, 0), pixmap, source_rect)
    return cropped_pixmap


@register(
    '.tif', '.tiff',
    '.bmp', '.png', '.webp',
    '.jpg', '.jpeg', '.jpe', '.jif', '.jfif', '.jfi',
)
class ImageWidget(QLabel, AttachmentWidget):
    MAX_SIZE = QSize(1024, 400)

    def __init__(self, attachment: MessageBackend.Attachment):
        super().__init__(attachment=attachment)
        self.setScaledContents(True)
        self.setObjectName('image_widget')
        policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        policy.setHeightForWidth(True)
        self.setSizePolicy(policy)
        self.download()

    @staticmethod
    def get_thumbnail(filepath: str) -> QPixmap:
        return crop_pixmap(QPixmap(filepath))

    def on_downloaded(self, filepath: str):
        run_task(
            self.load_image,
            filepath,
            result_slot=self.on_image_loaded,
            error_slot=self.on_load_failed
        )

    @staticmethod
    def load_image(filepath: str):
        return QImage(filepath)

    def on_image_loaded(self, image: QImage):
        pixmap = QPixmap(image)
        new_size = pixmap.size()
        if new_size.width() > self.MAX_SIZE.width() or new_size.height() > self.MAX_SIZE.height():
            new_size.scale(self.MAX_SIZE, Qt.AspectRatioMode.KeepAspectRatio)
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

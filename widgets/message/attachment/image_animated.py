from typing import cast

from PySide6.QtWidgets import QLabel, QSizePolicy, QApplication
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QWindow

from .attachment_widget import AttachmentWidget, register
from .image import crop_pixmap
from widgets.internal import AnimatedImage
from backend import MessageBackend


@register('.gif', '.webp')
class AnimatedImageWidget(QLabel, AttachmentWidget):
    MAX_IMAGE_SIZE = QSize(350, 256)

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
        movie = AnimatedImage(filepath, parent=self)
        new_size = movie.frameRect().size()
        if new_size.width() > self.MAX_IMAGE_SIZE.width() or new_size.height() > self.MAX_IMAGE_SIZE.height():
            new_size.scale(self.MAX_IMAGE_SIZE, Qt.AspectRatioMode.KeepAspectRatio)
        self.setMaximumSize(new_size)
        self.setMovie(movie)
        app = cast(QApplication, QApplication.instance())
        app.focusWindowChanged.connect(self.on_window_focus_change)
        movie.start()

    def on_window_focus_change(self, new_window: QWindow):
        self.movie().setPaused(new_window is None)

    def heightForWidth(self, width):
        width = min(width, self.maximumWidth())
        movie = self.movie()
        if movie is None:
            return 0
        size = movie.frameRect().size()
        if size.width() == 0:
            return 0
        height = int(width * size.height() / size.width())
        return height

    def sizeHint(self): return self.maximumSize()
    def minimumSizeHint(self): return self.minimumSize()

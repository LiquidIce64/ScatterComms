from typing import cast

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QMovie, QWindow

from .attachment_widget import register
from .image import ImageWidget


@register('.gif', '.webp')
class AnimatedImageWidget(ImageWidget):
    MAX_IMAGE_SIZE = QSize(350, 256)

    def load_image(self, filepath: str):
        return QMovie(filepath)

    def on_downloaded(self, filepath: str):
        self.on_image_loaded(self.load_image(filepath))

    def on_image_loaded(self, movie: QMovie):
        movie.jumpToFrame(0)
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

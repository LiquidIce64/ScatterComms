from PySide6.QtWidgets import QSizePolicy
from PySide6.QtMultimedia import QMediaPlayer, QMediaFormat
from PySide6.QtCore import Qt, QSize, QCoreApplication
from PySide6.QtGui import QPixmap

from .attachment_widget import AttachmentWidget, register
from .image import crop_pixmap
from widgets.common import VideoPlayer
from backend import MessageBackend


@register(
    '.mp4', '.m4v', '.mp4v',
    '.mkv', '.mk3d', '.mka', '.mks',
    '.webm', '.avi', '.ogv', '.mov', '.wmv'
)
class VideoWidget(VideoPlayer, AttachmentWidget):
    MAX_SIZE = QSize(1024, 400)

    def __init__(self, attachment: MessageBackend.Attachment = None):
        super().__init__()
        self.attachment = attachment
        self.setObjectName('video_widget')
        policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        policy.setHeightForWidth(True)
        self.setSizePolicy(policy)
        self.setEnabled(False)
        self.download()

    @staticmethod
    def get_thumbnail(filepath: str) -> QPixmap:
        player = QMediaPlayer()
        player.setSource(filepath)
        player.play()
        player.pause()
        QCoreApplication.processEvents()

        frame = player.videoSink().videoFrame().toImage()
        return crop_pixmap(QPixmap(frame))

    def on_downloaded(self, filepath: str):
        self.player.setSource(filepath)
        self.jump_to_first_frame()
        self.player.videoSink().videoSizeChanged.connect(
            self.__video_size_changed, type=Qt.ConnectionType.SingleShotConnection)
        self.setEnabled(True)

    def __video_size_changed(self):
        new_size = self.player.videoSink().videoSize()
        if new_size.width() == 0 or new_size.height() == 0:
            self.setMaximumSize(self.minimumSize())
            return
        if new_size.width() > self.MAX_SIZE.width() or new_size.height() > self.MAX_SIZE.height():
            new_size.scale(self.MAX_SIZE, Qt.AspectRatioMode.KeepAspectRatio)
        elif new_size.width() < self.minimumWidth() or new_size.height() < self.minimumHeight():
            new_size.scale(self.MAX_SIZE, Qt.AspectRatioMode.KeepAspectRatio)
        new_size.setHeight(new_size.height() + self.frame_player_controls.height())
        self.setMaximumSize(new_size)

    def heightForWidth(self, width):
        width = min(width, self.maximumWidth())
        video_size = self.player.videoSink().videoSize()
        if video_size.width() == 0:
            return self.minimumHeight()
        height = int(width * video_size.height() / video_size.width())
        height += self.frame_player_controls.height()
        return height

    def sizeHint(self): return self.maximumSize()
    def minimumSizeHint(self): return self.minimumSize()

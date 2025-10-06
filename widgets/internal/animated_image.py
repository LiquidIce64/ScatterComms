from PySide6.QtCore import QObject, QCoreApplication, QTimer
from PySide6.QtGui import QMovie

from .custom_events import MovieUpdateEvent


class AnimatedImage(QMovie):
    """A subclass of QMovie that uses low-priority events for loading frames to not lag the GUI thread"""
    def __init__(self, filename: str, /, parent: QObject = None):
        super().__init__(filename, parent=parent)
        self.__paused = False
        self.__frame_timer = QTimer(parent=self, singleShot=True)
        self.__frame_timer.timeout.connect(self.__queue_next_frame)
        self.jumpToFrame(0)

    def __queue_next_frame(self):
        QCoreApplication.postEvent(self, MovieUpdateEvent(), priority=-10)

    def start(self):
        self.__paused = False
        self.__queue_next_frame()

    def stop(self):
        self.__paused = True

    def setPaused(self, paused):
        self.__paused = paused
        if not paused:
            self.__queue_next_frame()

    def customEvent(self, event):
        if isinstance(event, MovieUpdateEvent):
            if self.__paused:
                return
            self.jumpToNextFrame()
            self.__frame_timer.start(self.nextFrameDelay())

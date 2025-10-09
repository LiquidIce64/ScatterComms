from PySide6.QtWidgets import QWidget, QMainWindow
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent

from backend import ConfigBackend
from .ui_video_player import Ui_video_player
from widgets.internal import HoverEventFilter, MouseClickEventFilter, KeyEventFilter


class VideoPlayer(QWidget, Ui_video_player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setVideoOutput(self.video)
        self.player.positionChanged.connect(self.__position_changed)
        self.player.durationChanged.connect(self.__duration_changed)

        self.btn_play.clicked.connect(self.toggle_play)
        self.__mouse_filter = MouseClickEventFilter(parent=self)
        self.__mouse_filter.released.connect(self.toggle_play)
        self.video.installEventFilter(self.__mouse_filter)

        self.__was_playing = False
        self.slider_playback.sliderMoved.connect(self.player.setPosition)
        self.slider_playback.sliderPressed.connect(self.__slider_pressed)
        self.slider_playback.sliderReleased.connect(self.__slider_released)

        self.__skip_volume_save = False
        self.slider_volume.valueChanged.connect(self.set_volume)
        self.slider_volume.setValue(ConfigBackend.session.media_volume)
        self.slider_volume.hide()

        self.__hover_filter = HoverEventFilter(parent=self)
        self.__hover_filter.hoverEnter.connect(lambda _: self.slider_volume.show())
        self.__hover_filter.hoverLeave.connect(lambda _: self.slider_volume.hide())
        self.frame_volume.installEventFilter(self.__hover_filter)
        self.btn_volume.clicked.connect(self.toggle_mute)

        self.__fullscreen_window: QMainWindow | None = None
        self.btn_fullscreen.clicked.connect(self.toggle_fullscreen)

    def jump_to_first_frame(self):
        self.player.setPosition(0)
        self.player.play()
        self.player.pause()

    def toggle_play(self):
        if self.player.isPlaying():
            self.player.pause()
        else:
            pos = self.slider_playback.value()
            if self.player.position() != pos:
                self.player.setPosition(pos)
            self.player.play()

    def __position_changed(self, position: int):
        self.slider_playback.setValue(position)

    def __duration_changed(self, duration: int):
        self.slider_playback.setRange(0, duration)
        step = max(60, self.player.duration() // 60)
        self.slider_playback.setSingleStep(step)
        self.slider_playback.setPageStep(step * 10)

    def __slider_pressed(self):
        self.__was_playing = self.player.isPlaying()
        self.player.pause()

    def __slider_released(self):
        self.player.setPosition(self.slider_playback.sliderPosition())
        if self.__was_playing:
            self.player.play()

    def toggle_mute(self):
        if self.slider_volume.value() > 0:
            self.__skip_volume_save = True
            self.slider_volume.setValue(0)
        else:
            self.slider_volume.setValue(ConfigBackend.session.media_volume)

    def set_volume(self, volume_percent: int):
        self.audio_output.setVolume(volume_percent / 100)
        if self.__skip_volume_save:
            self.__skip_volume_save = False
        else:
            ConfigBackend.session.media_volume = volume_percent

    def toggle_fullscreen(self):
        if self.__fullscreen_window is None:
            self.__fullscreen_window = QMainWindow(parent=self)
            self.__fullscreen_window.setCentralWidget(self.container)
            event_filter = KeyEventFilter(parent=self.__fullscreen_window)
            event_filter.keyReleased.connect(self.__fullscreen_keypress)
            self.__fullscreen_window.installEventFilter(event_filter)
            self.__fullscreen_window.showFullScreen()
        else:
            self.container.setParent(self)
            self.layout_widget.addWidget(self.container)
            self.__fullscreen_window.close()
            self.__fullscreen_window = None

    def __fullscreen_keypress(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Escape:
            if self.__fullscreen_window is not None:
                self.toggle_fullscreen()

from PySide6.QtCore import QStandardPaths, QFile
from PySide6.QtWidgets import QWidget, QFileDialog, QApplication
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

from backend import ConfigBackend
from .ui_audio_player import Ui_audio_player
from widgets.internal import HoverEventFilter, ms_to_timestamp


class AudioPlayer(QWidget, Ui_audio_player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self._duration_repr = '0:00'

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.positionChanged.connect(self.__position_changed)
        self.player.durationChanged.connect(self.__duration_changed)

        self.btn_play.clicked.connect(self.toggle_play)
        self.__was_playing = False
        self.slider_playback.sliderMoved.connect(self.player.setPosition)
        self.slider_playback.sliderPressed.connect(self.__slider_pressed)
        self.slider_playback.sliderReleased.connect(self.__slider_released)
        self.slider_playback.valueChanged.connect(self.__slider_value_changed)

        self.__skip_volume_save = False
        self.slider_volume.valueChanged.connect(self.set_volume)
        self.slider_volume.setValue(ConfigBackend.session.audio_volume)
        self.slider_volume.hide()

        hover_filter = HoverEventFilter(parent=self)
        hover_filter.hoverEnter.connect(lambda _: self.slider_volume.show())
        hover_filter.hoverLeave.connect(lambda _: self.slider_volume.hide())
        self.frame_volume.installEventFilter(hover_filter)
        self.btn_volume.clicked.connect(self.toggle_mute)

        self.btn_file.clicked.connect(self.save_file)
        self.btn_file.setEnabled(False)

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
        self.label_time.setText(f'{ms_to_timestamp(self.player.position())} / {self._duration_repr}')

    def __duration_changed(self, duration: int):
        self.slider_playback.setRange(0, duration)
        self.slider_playback.setSingleStep(1000 / QApplication.wheelScrollLines())
        self.slider_playback.setPageStep(max(10000, duration // 10))
        self._duration_repr = ms_to_timestamp(duration)
        self.label_time.setText(f'{ms_to_timestamp(self.player.position())} / {self._duration_repr}')

    def __slider_value_changed(self, position: int):
        if self.player.isPlaying():
            return
        self.player.setPosition(position)

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
            self.slider_volume.setValue(ConfigBackend.session.audio_volume)

    def set_volume(self, volume_percent: int):
        volume = volume_percent / 100
        volume *= volume  # Squared for better volume control
        self.audio_output.setVolume(volume)
        if self.__skip_volume_save:
            self.__skip_volume_save = False
        else:
            ConfigBackend.session.audio_volume = volume_percent

    def set_source(self, filepath: str):
        self.player.setSource(filepath)
        self.btn_file.setEnabled(True)

    def save_file(self):
        if self.player.source() is None:
            return
        downloads_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DownloadLocation)
        new_filepath = QFileDialog.getSaveFileName(
            parent=self,
            caption=QApplication.translate('file_dialog', 'Save file'),
            dir=f'{downloads_dir}/{self.btn_file.text()}'
        )[0]
        if new_filepath:
            QFile.copy(self.player.source().path(), new_filepath)

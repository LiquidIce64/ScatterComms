from typing import Optional

from PySide6.QtCore import QSettings, QByteArray, QObject, Signal

from .profile import ProfileBackend
from .storage import StorageBackend


class ConfigBackend:
    class Session(QObject):
        changed = Signal()

        def __init__(self):
            super().__init__()
            settings = ConfigBackend.get_settings('session.ini')

            profile_uuid = settings.value('profile/uuid', defaultValue='', type=str)
            status = settings.value('profile/status', defaultValue=ProfileBackend.Status.Online, type=str)

            self.geometry = settings.value('window/geometry', defaultValue=None, type=QByteArray)
            self.state = settings.value('window/state', defaultValue=None, type=QByteArray)
            self.__profile = ProfileBackend.get_profile(profile_uuid)
            try:
                self.__status = ProfileBackend.Status(status)
            except ValueError:
                self.__status = ProfileBackend.Status.Online

        @property
        def profile(self): return self.__profile
        @property
        def status(self): return self.__status

        @profile.setter
        def profile(self, new_value: ProfileBackend.Profile):
            self.__profile = new_value
            self.changed.emit()

        @status.setter
        def status(self, new_value: ProfileBackend.Status):
            self.__status = new_value
            self.changed.emit()

        def save(self):
            settings = ConfigBackend.get_settings('session.ini')
            settings.setValue('window/geometry', self.geometry)
            settings.setValue('window/state', self.state)
            settings.setValue('profile/uuid', self.__profile and str(self.__profile.uuid) or '')
            settings.setValue('profile/status', self.__status.value)

    session: Optional[Session] = None

    @classmethod
    def get_settings(cls, filename: str):
        filepath = StorageBackend.locate_config(filename, allow_empty=False)
        return QSettings(filepath, QSettings.Format.IniFormat)

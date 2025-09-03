from typing import Union

from PySide6.QtCore import QSettings, QByteArray, Signal, QObject

from .profile import ProfileBackend
from .storage import StorageBackend


class ConfigBackend:
    class Session(QObject):
        status_changed = Signal()

        def __init__(self):
            super().__init__()
            settings = ConfigBackend.get_settings('session.ini')

            profile_uuid = settings.value('profile/uuid', defaultValue='', type=str)
            status = settings.value('profile/status', defaultValue=ProfileBackend.Status.online, type=str)

            self.geometry = settings.value('window/geometry', defaultValue=None, type=QByteArray)
            self.state = settings.value('window/state', defaultValue=None, type=QByteArray)
            self.profile: Union[ProfileBackend.Profile, object, None] = ProfileBackend.get_profile(profile_uuid)
            self.__status: ProfileBackend.Status = ProfileBackend.Status(status)

        @property
        def status(self): return self.__status

        @status.setter
        def status(self, new_value: ProfileBackend.Status):
            self.__status = new_value
            self.status_changed.emit()

        def save(self):
            settings = ConfigBackend.get_settings('session.ini')
            settings.setValue('window/geometry', self.geometry)
            settings.setValue('window/state', self.state)
            settings.setValue('profile/uuid', self.profile and str(self.profile.uuid) or '')
            settings.setValue('profile/status', self.__status.value)

    @classmethod
    def get_settings(cls, filename: str):
        filepath = StorageBackend.locate_config_file(filename, allow_empty=False)
        return QSettings(filepath, QSettings.Format.IniFormat)

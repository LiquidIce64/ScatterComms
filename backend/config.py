from typing import Optional

from PySide6.QtCore import QSettings, QByteArray, QObject, Signal

from .profile import ProfileBackend
from .server import ServerBackend
from .storage import StorageBackend


class ConfigBackend:
    class Session(QObject):
        profile_changed = Signal()
        server_changed = Signal()

        def __init__(self):
            super().__init__()
            settings = ConfigBackend.get_settings('session.ini')

            profile_uuid = settings.value('profile/uuid', defaultValue='', type=str)
            server_uuid = settings.value('server/uuid', defaultValue='', type=str)
            status = settings.value('profile/status', defaultValue=ProfileBackend.Status.Online, type=str)

            self.geometry = settings.value('window/geometry', defaultValue=None, type=QByteArray)
            self.state = settings.value('window/state', defaultValue=None, type=QByteArray)

            self.__profile = ProfileBackend.get_profile(profile_uuid)

            try:
                self.__status = ProfileBackend.Status(status)
            except ValueError:
                self.__status = ProfileBackend.Status.Online

            if self.__profile is not None:
                self.__selected_server = ServerBackend.get_server(self.__profile.uuid, server_uuid)
            else:
                self.__selected_server = None

        @property
        def profile(self): return self.__profile
        @property
        def status(self): return self.__status
        @property
        def selected_server(self): return self.__selected_server

        @profile.setter
        def profile(self, new_value: ProfileBackend.Profile):
            self.__profile = new_value
            self.profile_changed.emit()

        @status.setter
        def status(self, new_value: ProfileBackend.Status):
            self.__status = new_value
            self.profile_changed.emit()

        @selected_server.setter
        def selected_server(self, new_value: ServerBackend.Server):
            self.__selected_server = new_value
            self.server_changed.emit()

        def save(self):
            settings = ConfigBackend.get_settings('session.ini')
            settings.setValue('window/geometry', self.geometry)
            settings.setValue('window/state', self.state)
            settings.setValue('profile/uuid', self.__profile and str(self.__profile.uuid) or '')
            settings.setValue('profile/status', self.__status.value)
            settings.setValue('server/uuid', self.__selected_server and str(self.__selected_server.uuid) or '')

    session: Optional[Session] = None

    @classmethod
    def get_settings(cls, filename: str):
        filepath = StorageBackend.locate_config(filename, allow_empty=False)
        return QSettings(filepath, QSettings.Format.IniFormat)

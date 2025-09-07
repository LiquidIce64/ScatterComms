import os
from uuid import UUID
from PySide6.QtCore import QStandardPaths
from PySide6.QtGui import QImage


def get_dir(location: QStandardPaths.StandardLocation):
    path = QStandardPaths.writableLocation(location)
    os.makedirs(path, exist_ok=True)
    return path


class StorageBackend:
    cache_dir = ''
    appdata_dir = ''
    config_dir = ''

    @classmethod
    def __init_image_dirs(cls, path: str):
        appdata = cls.appdata_dir + path
        cache = cls.cache_dir + path
        os.makedirs(appdata, exist_ok=True)
        os.makedirs(cache, exist_ok=True)
        return appdata, cache

    @classmethod
    def init(cls, test_mode=False):
        QStandardPaths.setTestModeEnabled(test_mode)
        cls.cache_dir = get_dir(QStandardPaths.StandardLocation.CacheLocation)
        cls.appdata_dir = get_dir(QStandardPaths.StandardLocation.AppDataLocation)
        cls.config_dir = get_dir(QStandardPaths.StandardLocation.AppConfigLocation)

        cls.Server.icon_dir, cls.Server.icon_cache = cls.__init_image_dirs('/server/icons')
        cls.Profile.avatar_dir, cls.Profile.avatar_cache = cls.__init_image_dirs('/profile/avatars')

    @classmethod
    def locate_cache(cls, path: str, allow_empty=True):
        result = QStandardPaths.locate(QStandardPaths.StandardLocation.CacheLocation, path)
        if allow_empty or result != '':
            return result
        return cls.cache_dir + '/' + path

    @classmethod
    def locate_appdata(cls, path: str, allow_empty=True):
        result = QStandardPaths.locate(QStandardPaths.StandardLocation.AppDataLocation, path)
        if allow_empty or result != '':
            return result
        return cls.appdata_dir + '/' + path

    @classmethod
    def locate_config(cls, path: str, allow_empty=True):
        result = QStandardPaths.locate(QStandardPaths.StandardLocation.AppConfigLocation, path)
        if allow_empty or result != '':
            return result
        return cls.config_dir + '/' + path

    @staticmethod
    def _get_image(dir_path: str, uuid: UUID):
        filepath = dir_path + f'/{uuid}.png'
        return QImage(filepath) if os.path.exists(filepath) else None

    @staticmethod
    def _set_image(dir_path: str, uuid: UUID, image: QImage):
        filepath = dir_path + f'/{uuid}.png'
        image.save(filepath)

    class Server:
        icon_dir = ''
        icon_cache = ''

        @classmethod
        def get_icon(cls, server_uuid: UUID, use_cache=False):
            return StorageBackend._get_image(cls.icon_cache if use_cache else cls.icon_dir, server_uuid)

        @classmethod
        def set_icon(cls, server_uuid: UUID, icon: QImage, use_cache=False):
            return StorageBackend._set_image(cls.icon_cache if use_cache else cls.icon_dir, server_uuid, icon)

    class Profile:
        avatar_dir = ''
        avatar_cache = ''

        @classmethod
        def get_avatar(cls, user_uuid: UUID, use_cache=False):
            return StorageBackend._get_image(cls.avatar_cache if use_cache else cls.avatar_dir, user_uuid)

        @classmethod
        def set_avatar(cls, user_uuid: UUID, avatar: QImage, use_cache=False):
            return StorageBackend._set_image(cls.avatar_cache if use_cache else cls.avatar_dir, user_uuid, avatar)

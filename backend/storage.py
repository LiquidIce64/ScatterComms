import os
from PySide6.QtCore import QStandardPaths


def get_dir(location: QStandardPaths.StandardLocation):
    path = QStandardPaths.writableLocation(location)
    os.makedirs(path, exist_ok=True)
    return path


class StorageBackend:
    cache_dir = ''
    appdata_dir = ''
    config_dir = ''

    @classmethod
    def init(cls, test_mode=False):
        QStandardPaths.setTestModeEnabled(test_mode)
        cls.cache_dir = get_dir(QStandardPaths.StandardLocation.CacheLocation)
        cls.appdata_dir = get_dir(QStandardPaths.StandardLocation.AppDataLocation)
        cls.config_dir = get_dir(QStandardPaths.StandardLocation.AppConfigLocation)

    @classmethod
    def locate_cached_file(cls, path: str, allow_empty=True):
        result = QStandardPaths.locate(QStandardPaths.StandardLocation.CacheLocation, path)
        if allow_empty or result != '':
            return result
        return cls.cache_dir + '/' + path

    @classmethod
    def locate_appdata_file(cls, path: str, allow_empty=True):
        result = QStandardPaths.locate(QStandardPaths.StandardLocation.AppDataLocation, path)
        if allow_empty or result != '':
            return result
        return cls.appdata_dir + '/' + path

    @classmethod
    def locate_config_file(cls, path: str, allow_empty=True):
        result = QStandardPaths.locate(QStandardPaths.StandardLocation.AppConfigLocation, path)
        if allow_empty or result != '':
            return result
        return cls.config_dir + '/' + path

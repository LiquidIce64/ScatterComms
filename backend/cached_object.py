from weakref import ref

from PySide6.QtCore import QObject, Signal


class CachedObject(QObject):
    changed = Signal()

    _cached_instances = {}

    def __new__(cls, obj):
        key = cls.cache_key(obj)
        if key in cls._cached_instances:
            instance = cls._cached_instances[key]()
            instance.update(obj)
            return instance
        else:
            instance = super().__new__(cls)
            cls._cached_instances[key] = ref(instance)
            return instance

    def update(self, obj): pass

    @staticmethod
    def cache_key(obj) -> str: return getattr(obj, 'uuid')

    def deleteLater(self):
        self._cached_instances.pop(self.cache_key(self), None)
        super().deleteLater()

    def __del__(self):
        self._cached_instances.pop(self.cache_key(self), None)

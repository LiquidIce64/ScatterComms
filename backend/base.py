class BaseBackend:
    _registered_backends: dict[str, type['BaseBackend']] = {}

    def __init_subclass__(cls, **kwargs):
        BaseBackend._registered_backends[cls.__name__] = cls

    @staticmethod
    def get_backend(class_name: str):
        return BaseBackend._registered_backends[class_name]

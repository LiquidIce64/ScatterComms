from PySide6.QtCore import QEvent


def custom_event(index=0):
    return QEvent.Type(QEvent.registerEventType(QEvent.Type.User + index))


class CustomEventType:
    MovieUpdateEvent = custom_event(0)
    ScrollBarUpdateEvent = custom_event(1)


class MovieUpdateEvent(QEvent):
    def __init__(self):
        super().__init__(CustomEventType.MovieUpdateEvent)


class ScrollBarUpdateEvent(QEvent):
    def __init__(self):
        super().__init__(CustomEventType.ScrollBarUpdateEvent)

from PySide6.QtGui import QIcon


ICON_DIR = 'resources/icons/'


class Icons:
    ArrowUp = QIcon(ICON_DIR + 'arrow_up.svg')
    ArrowDown = QIcon(ICON_DIR + 'arrow_down.svg')
    Settings = QIcon(ICON_DIR + 'settings.svg')
    Search = QIcon(ICON_DIR + 'search.svg')
    Edit = QIcon(ICON_DIR + 'edit.svg')
    User = QIcon(ICON_DIR + 'user.svg')
    Plus = QIcon(ICON_DIR + 'plus.svg')
    Emoji = QIcon(ICON_DIR + 'emoji.svg')
    Send = QIcon(ICON_DIR + 'send.svg')
    ServerFrame = QIcon(ICON_DIR + 'server_frame.svg')

    class Status:
        Online = QIcon(ICON_DIR + 'status_online.svg')
        Away = QIcon(ICON_DIR + 'status_away.svg')
        DoNotDisturb = QIcon(ICON_DIR + 'status_do_not_disturb.svg')
        Offline = QIcon(ICON_DIR + 'status_offline.svg')

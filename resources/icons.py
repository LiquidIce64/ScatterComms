from PySide6.QtGui import QIcon


ICON_DIR = 'resources/icons/'


class Icons:
    arrow_up = QIcon(ICON_DIR + 'arrow_up.svg')
    arrow_down = QIcon(ICON_DIR + 'arrow_down.svg')
    settings = QIcon(ICON_DIR + 'settings.svg')
    search = QIcon(ICON_DIR + 'search.svg')
    edit = QIcon(ICON_DIR + 'edit.svg')
    user = QIcon(ICON_DIR + 'user.svg')
    plus = QIcon(ICON_DIR + 'plus.svg')
    emoji = QIcon(ICON_DIR + 'emoji.svg')
    send = QIcon(ICON_DIR + 'send.svg')
    send.addFile(ICON_DIR + 'send_disabled.svg', mode=send.Mode.Disabled)

    class Status:
        online = QIcon(ICON_DIR + 'status_online.svg')
        away = QIcon(ICON_DIR + 'status_away.svg')
        do_not_disturb = QIcon(ICON_DIR + 'status_do_not_disturb.svg')
        offline = QIcon(ICON_DIR + 'status_offline.svg')

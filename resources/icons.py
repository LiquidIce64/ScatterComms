from PySide6.QtGui import QIcon


ICON_DIR = "resources/icons/"


class Icons:
    arrow_up = QIcon(ICON_DIR + "arrow_up.svg")
    arrow_down = QIcon(ICON_DIR + "arrow_down.svg")


class StatusIcons:
    online = QIcon(ICON_DIR + "status_online.svg")
    away = QIcon(ICON_DIR + "status_away.svg")
    do_not_disturb = QIcon(ICON_DIR + "status_do_not_disturb.svg")
    offline = QIcon(ICON_DIR + "status_offline.svg")

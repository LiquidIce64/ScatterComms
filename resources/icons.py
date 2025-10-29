from PySide6.QtGui import QIcon


ICON_DIR = 'resources/icons/'


class Icons:
    class Generic:
        ArrowDown = QIcon(ICON_DIR + 'generic/arrow_down.svg')
        ArrowUp = QIcon(ICON_DIR + 'generic/arrow_up.svg')
        Cross = QIcon(ICON_DIR + 'generic/cross.svg')
        Edit = QIcon(ICON_DIR + 'generic/edit.svg')
        Plus = QIcon(ICON_DIR + 'generic/plus.svg')
        Save = QIcon(ICON_DIR + 'generic/save.svg')
        Search = QIcon(ICON_DIR + 'generic/search.svg')
        Settings = QIcon(ICON_DIR + 'generic/settings.svg')

    class Profile:
        User = QIcon(ICON_DIR + 'profile/user.svg')
        Avatar = QIcon(ICON_DIR + 'profile/avatar.svg')

    class Message:
        Emoji = QIcon(ICON_DIR + 'message/emoji.svg')
        Send = QIcon(ICON_DIR + 'message/send.svg')

    class Server:
        Server = QIcon(ICON_DIR + 'server/server.svg')
        Frame = QIcon(ICON_DIR + 'server/frame.svg')
        TextChat = QIcon(ICON_DIR + 'server/text_chat.svg')

    class Status:
        Online = QIcon(ICON_DIR + 'status/online.svg')
        Away = QIcon(ICON_DIR + 'status/away.svg')
        DoNotDisturb = QIcon(ICON_DIR + 'status/do_not_disturb.svg')
        Offline = QIcon(ICON_DIR + 'status/offline.svg')


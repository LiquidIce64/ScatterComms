# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

from widgets.common import (FrameButton, IconWidget, MaskedImage, ScrollableFrame)
from widgets.server import (PinnedServerList, ServerList)
import index_rc

class Ui_main_page(object):
    def setupUi(self, main_page):
        if not main_page.objectName():
            main_page.setObjectName(u"main_page")
        main_page.resize(1000, 600)
        main_page.setMinimumSize(QSize(1000, 600))
        main_page.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        main_page.setStyleSheet(u"#frame_side_panel, #btn_server_title, #frame_chat_title, #frame_controls, #frame_members {\n"
"	background-color: #252525;\n"
"	border-top: 1px solid #303030;\n"
"	border-left: 1px solid #303030;\n"
"	border-bottom: 1px solid #181818;\n"
"	border-right: 1px solid #181818;\n"
"}\n"
"\n"
"#frame_servers {\n"
"	background-color: #151515;\n"
"	border-top: 1px solid #202020;\n"
"	border-left: 1px solid #202020;\n"
"	border-bottom: 1px solid #080808;\n"
"	border-right: 1px solid #080808;\n"
"}\n"
"\n"
"#frame_messagebox {\n"
"	background-color: #353535;\n"
"}\n"
"\n"
"#scroll_chat, #scrollcontent_chat {\n"
"	background-color: #2A2A2A;\n"
"}\n"
"\n"
"#scrollcontent_servers {\n"
"	background-color: #151515;\n"
"}\n"
"\n"
"#divider_servers {\n"
"	background-color: #252525;\n"
"}\n"
"\n"
"#frame_serverlist_pinned {\n"
"	padding-bottom: 6px;\n"
"}\n"
"\n"
"#frame_serverlist {\n"
"	padding-top: 6px;\n"
"	padding-bottom: 6px;\n"
"}\n"
"\n"
"#frame_serverlist[drag=\"true\"] {\n"
"	background-color: #202020;\n"
"	border-radi"
                        "us: 6px;\n"
"}\n"
"\n"
"#frame_serverlist #btn_create_server {\n"
"	background-color: #2A2A2A;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#frame_serverlist #btn_create_server:hover {\n"
"	background-color: #353535;\n"
"}\n"
"\n"
"#label_servername {\n"
"	margin-left: 4px;\n"
"	font-size: 12pt;\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"#icon_userstatus {\n"
"	padding: 2px;\n"
"}\n"
"\n"
"#btn_profile {\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"#label_userstatus {\n"
"	margin-left: 4px;\n"
"	font-size: 7pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"#label_username {\n"
"	margin-left: 1px;\n"
"	font-size: 11pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"#btn_settings, #btn_search, #btn_attachment, #btn_emoji, #btn_send {\n"
"	background: none;\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"#btn_server_title:hover, #btn_server_title:focus, #btn_server_title[checked=\"true\"],\n"
"#btn_profile:hover, #btn_profile:focus, #btn_profile[checked=\"true\"],\n"
"#btn_search:hover, #btn_settings:hover {\n"
"	background-color: #"
                        "303030;\n"
"}\n"
"\n"
"#btn_attachment:hover, #btn_emoji:hover, #btn_send:hover {\n"
"	background-color: #454545;\n"
"}\n"
"\n"
"#btn_search:checked {\n"
"	background-color: #404040;\n"
"}\n"
"\n"
"#btn_emoji:checked {\n"
"	background-color: #555555;\n"
"}\n"
"\n"
"#icon_server_dropdown {\n"
"	margin: 8px;\n"
"}\n"
"\n"
"#textbox {\n"
"	background-color: #353535;\n"
"	font-size: 10pt;\n"
"}")
        self.layout_main_page = QGridLayout(main_page)
        self.layout_main_page.setSpacing(0)
        self.layout_main_page.setObjectName(u"layout_main_page")
        self.layout_main_page.setContentsMargins(0, 0, 0, 0)
        self.frame_chat_title = QFrame(main_page)
        self.frame_chat_title.setObjectName(u"frame_chat_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_chat_title.sizePolicy().hasHeightForWidth())
        self.frame_chat_title.setSizePolicy(sizePolicy)
        self.frame_chat_title.setMinimumSize(QSize(0, 46))
        self.frame_chat_title.setMaximumSize(QSize(16777215, 46))
        self.frame_chat_title.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_chat_title.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_chat_title = QHBoxLayout(self.frame_chat_title)
        self.layout_chat_title.setSpacing(3)
        self.layout_chat_title.setObjectName(u"layout_chat_title")
        self.layout_chat_title.setContentsMargins(6, 6, 6, 6)

        self.layout_main_page.addWidget(self.frame_chat_title, 0, 2, 1, 1)

        self.frame_servers = ScrollableFrame(main_page)
        self.frame_servers.setObjectName(u"frame_servers")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_servers.sizePolicy().hasHeightForWidth())
        self.frame_servers.setSizePolicy(sizePolicy1)
        self.frame_servers.setMinimumSize(QSize(58, 0))
        self.frame_servers.setMaximumSize(QSize(58, 16777215))
        self.frame_servers.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_servers.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_servers_frame = QVBoxLayout(self.frame_servers)
        self.layout_servers_frame.setSpacing(0)
        self.layout_servers_frame.setObjectName(u"layout_servers_frame")
        self.layout_servers_frame.setContentsMargins(2, 6, 2, 6)
        self.scroll_servers = QScrollArea(self.frame_servers)
        self.scroll_servers.setObjectName(u"scroll_servers")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scroll_servers.sizePolicy().hasHeightForWidth())
        self.scroll_servers.setSizePolicy(sizePolicy2)
        self.scroll_servers.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_servers.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_servers.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_servers.setWidgetResizable(True)
        self.scroll_servers.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollcontent_servers = QWidget()
        self.scrollcontent_servers.setObjectName(u"scrollcontent_servers")
        self.scrollcontent_servers.setGeometry(QRect(0, 0, 52, 586))
        self.verticalLayout = QVBoxLayout(self.scrollcontent_servers)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_serverlist_pinned = PinnedServerList(self.scrollcontent_servers)
        self.frame_serverlist_pinned.setObjectName(u"frame_serverlist_pinned")

        self.verticalLayout.addWidget(self.frame_serverlist_pinned)

        self.divider_servers = QFrame(self.scrollcontent_servers)
        self.divider_servers.setObjectName(u"divider_servers")
        self.divider_servers.setMinimumSize(QSize(32, 2))
        self.divider_servers.setMaximumSize(QSize(32, 2))
        self.divider_servers.setFrameShape(QFrame.Shape.HLine)
        self.divider_servers.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.divider_servers, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_serverlist = ServerList(self.scrollcontent_servers)
        self.frame_serverlist.setObjectName(u"frame_serverlist")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_serverlist.sizePolicy().hasHeightForWidth())
        self.frame_serverlist.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.frame_serverlist)

        self.scroll_servers.setWidget(self.scrollcontent_servers)

        self.layout_servers_frame.addWidget(self.scroll_servers)


        self.layout_main_page.addWidget(self.frame_servers, 0, 0, 3, 1)

        self.btn_server_title = FrameButton(main_page)
        self.btn_server_title.setObjectName(u"btn_server_title")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_server_title.sizePolicy().hasHeightForWidth())
        self.btn_server_title.setSizePolicy(sizePolicy4)
        self.btn_server_title.setMinimumSize(QSize(222, 46))
        self.btn_server_title.setMaximumSize(QSize(222, 46))
        self.btn_server_title.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_server_title.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.btn_server_title.setFrameShape(QFrame.Shape.NoFrame)
        self.btn_server_title.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_server_title = QHBoxLayout(self.btn_server_title)
        self.layout_server_title.setSpacing(3)
        self.layout_server_title.setObjectName(u"layout_server_title")
        self.layout_server_title.setContentsMargins(6, 6, 6, 6)
        self.label_servername = QLabel(self.btn_server_title)
        self.label_servername.setObjectName(u"label_servername")
        self.label_servername.setText(u"Server Name")

        self.layout_server_title.addWidget(self.label_servername)

        self.icon_server_dropdown = IconWidget(self.btn_server_title)
        self.icon_server_dropdown.setObjectName(u"icon_server_dropdown")
        self.icon_server_dropdown.setMinimumSize(QSize(32, 32))
        self.icon_server_dropdown.setMaximumSize(QSize(32, 32))
        self.icon_server_dropdown.setText(u"")
        self.icon_server_dropdown.setPixmap(QPixmap(u":/icons/arrow_down"))
        self.icon_server_dropdown.setScaledContents(True)

        self.layout_server_title.addWidget(self.icon_server_dropdown)

        self.layout_server_title.setStretch(0, 1)

        self.layout_main_page.addWidget(self.btn_server_title, 0, 1, 1, 1)

        self.frame_controls = QFrame(main_page)
        self.frame_controls.setObjectName(u"frame_controls")
        sizePolicy4.setHeightForWidth(self.frame_controls.sizePolicy().hasHeightForWidth())
        self.frame_controls.setSizePolicy(sizePolicy4)
        self.frame_controls.setMinimumSize(QSize(260, 46))
        self.frame_controls.setMaximumSize(QSize(260, 46))
        self.frame_controls.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_controls.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_controls = QHBoxLayout(self.frame_controls)
        self.layout_controls.setSpacing(3)
        self.layout_controls.setObjectName(u"layout_controls")
        self.layout_controls.setContentsMargins(3, 3, 6, 3)
        self.btn_profile = FrameButton(self.frame_controls)
        self.btn_profile.setObjectName(u"btn_profile")
        self.btn_profile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_profile.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.layout_profile = QGridLayout(self.btn_profile)
        self.layout_profile.setSpacing(0)
        self.layout_profile.setObjectName(u"layout_profile")
        self.layout_profile.setContentsMargins(3, 3, 3, 3)
        self.icon_userstatus = IconWidget(self.btn_profile)
        self.icon_userstatus.setObjectName(u"icon_userstatus")
        self.icon_userstatus.setMinimumSize(QSize(12, 12))
        self.icon_userstatus.setMaximumSize(QSize(12, 12))
        self.icon_userstatus.setText(u"")
        self.icon_userstatus.setPixmap(QPixmap(u":/status/online"))
        self.icon_userstatus.setScaledContents(True)

        self.layout_profile.addWidget(self.icon_userstatus, 1, 1, 1, 1)

        self.label_username = QLabel(self.btn_profile)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setText(u"Username")

        self.layout_profile.addWidget(self.label_username, 0, 2, 1, 1)

        self.label_userstatus = QLabel(self.btn_profile)
        self.label_userstatus.setObjectName(u"label_userstatus")

        self.layout_profile.addWidget(self.label_userstatus, 1, 2, 1, 1)

        self.icon_useravatar = MaskedImage(self.btn_profile)
        self.icon_useravatar.setObjectName(u"icon_useravatar")
        self.icon_useravatar.setMinimumSize(QSize(32, 32))
        self.icon_useravatar.setMaximumSize(QSize(32, 32))
        self.icon_useravatar.setText(u"")
        self.icon_useravatar.setPixmap(QPixmap(u":/icons/avatar"))
        self.icon_useravatar.setScaledContents(True)

        self.layout_profile.addWidget(self.icon_useravatar, 0, 0, 1, 2)

        self.layout_profile.setRowStretch(0, 1)
        self.layout_profile.setColumnStretch(2, 1)
        self.icon_useravatar.raise_()
        self.label_username.raise_()
        self.icon_userstatus.raise_()
        self.label_userstatus.raise_()

        self.layout_controls.addWidget(self.btn_profile)

        self.btn_search = QPushButton(self.frame_controls)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(38, 38))
        self.btn_search.setMaximumSize(QSize(38, 38))
        self.btn_search.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_search.setText(u"")
        icon = QIcon()
        icon.addFile(u":/icons/search", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_search.setIcon(icon)
        self.btn_search.setIconSize(QSize(24, 24))
        self.btn_search.setCheckable(True)

        self.layout_controls.addWidget(self.btn_search)

        self.btn_settings = QPushButton(self.frame_controls)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(38, 38))
        self.btn_settings.setMaximumSize(QSize(38, 38))
        self.btn_settings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_settings.setText(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/settings", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_settings.setIcon(icon1)
        self.btn_settings.setIconSize(QSize(24, 24))

        self.layout_controls.addWidget(self.btn_settings)


        self.layout_main_page.addWidget(self.frame_controls, 0, 3, 1, 1)

        self.frame_side_panel = QFrame(main_page)
        self.frame_side_panel.setObjectName(u"frame_side_panel")
        sizePolicy1.setHeightForWidth(self.frame_side_panel.sizePolicy().hasHeightForWidth())
        self.frame_side_panel.setSizePolicy(sizePolicy1)
        self.frame_side_panel.setMinimumSize(QSize(222, 0))
        self.frame_side_panel.setMaximumSize(QSize(222, 16777215))
        self.frame_side_panel.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_side_panel.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_side_panel = QVBoxLayout(self.frame_side_panel)
        self.layout_side_panel.setSpacing(0)
        self.layout_side_panel.setObjectName(u"layout_side_panel")
        self.layout_side_panel.setContentsMargins(6, 6, 6, 6)

        self.layout_main_page.addWidget(self.frame_side_panel, 1, 1, 2, 1)

        self.frame_members = QFrame(main_page)
        self.frame_members.setObjectName(u"frame_members")
        sizePolicy1.setHeightForWidth(self.frame_members.sizePolicy().hasHeightForWidth())
        self.frame_members.setSizePolicy(sizePolicy1)
        self.frame_members.setMinimumSize(QSize(260, 0))
        self.frame_members.setMaximumSize(QSize(260, 16777215))
        self.frame_members.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_members.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_members = QVBoxLayout(self.frame_members)
        self.layout_members.setObjectName(u"layout_members")
        self.layout_members.setContentsMargins(6, 6, 6, 6)
        self.spacer_members = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_members.addItem(self.spacer_members)


        self.layout_main_page.addWidget(self.frame_members, 1, 3, 2, 1)

        self.frame_chat = QFrame(main_page)
        self.frame_chat.setObjectName(u"frame_chat")
        self.layout_chat_frame = QVBoxLayout(self.frame_chat)
        self.layout_chat_frame.setSpacing(0)
        self.layout_chat_frame.setObjectName(u"layout_chat_frame")
        self.layout_chat_frame.setContentsMargins(0, 0, 0, 0)
        self.scroll_chat = QScrollArea(self.frame_chat)
        self.scroll_chat.setObjectName(u"scroll_chat")
        self.scroll_chat.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_chat.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_chat.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_chat.setWidgetResizable(True)
        self.scroll_chat.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.scrollcontent_chat = QWidget()
        self.scrollcontent_chat.setObjectName(u"scrollcontent_chat")
        self.scrollcontent_chat.setGeometry(QRect(0, 0, 460, 404))
        self.layout_chat = QVBoxLayout(self.scrollcontent_chat)
        self.layout_chat.setSpacing(0)
        self.layout_chat.setObjectName(u"layout_chat")
        self.layout_chat.setContentsMargins(0, 0, 0, 0)
        self.spacer_chat = QSpacerItem(20, 487, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_chat.addItem(self.spacer_chat)

        self.scroll_chat.setWidget(self.scrollcontent_chat)

        self.layout_chat_frame.addWidget(self.scroll_chat)

        self.frame_messagebox = QFrame(self.frame_chat)
        self.frame_messagebox.setObjectName(u"frame_messagebox")
        self.frame_messagebox.setMinimumSize(QSize(0, 50))
        self.frame_messagebox.setMaximumSize(QSize(16777215, 150))
        self.frame_messagebox.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_messagebox.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_messagebox = QHBoxLayout(self.frame_messagebox)
        self.layout_messagebox.setObjectName(u"layout_messagebox")
        self.btn_attachment = QPushButton(self.frame_messagebox)
        self.btn_attachment.setObjectName(u"btn_attachment")
        self.btn_attachment.setMinimumSize(QSize(32, 32))
        self.btn_attachment.setMaximumSize(QSize(32, 32))
        self.btn_attachment.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_attachment.setText(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/plus", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_attachment.setIcon(icon2)

        self.layout_messagebox.addWidget(self.btn_attachment, 0, Qt.AlignmentFlag.AlignBottom)

        self.textbox = QTextEdit(self.frame_messagebox)
        self.textbox.setObjectName(u"textbox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.textbox.sizePolicy().hasHeightForWidth())
        self.textbox.setSizePolicy(sizePolicy5)
        self.textbox.setMinimumSize(QSize(0, 28))
        self.textbox.setMaximumSize(QSize(16777215, 132))
        self.textbox.setFrameShape(QFrame.Shape.NoFrame)
        self.textbox.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.textbox.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textbox.setTabChangesFocus(True)
        self.textbox.setDocumentTitle(u"")
        self.textbox.setUndoRedoEnabled(False)
        self.textbox.setMarkdown(u"")
        self.textbox.setHtml(u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.textbox.setAcceptRichText(True)

        self.layout_messagebox.addWidget(self.textbox)

        self.btn_emoji = QPushButton(self.frame_messagebox)
        self.btn_emoji.setObjectName(u"btn_emoji")
        self.btn_emoji.setMinimumSize(QSize(32, 32))
        self.btn_emoji.setMaximumSize(QSize(32, 32))
        self.btn_emoji.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_emoji.setText(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/emoji", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_emoji.setIcon(icon3)
        self.btn_emoji.setCheckable(True)

        self.layout_messagebox.addWidget(self.btn_emoji, 0, Qt.AlignmentFlag.AlignBottom)

        self.btn_send = QPushButton(self.frame_messagebox)
        self.btn_send.setObjectName(u"btn_send")
        self.btn_send.setEnabled(False)
        self.btn_send.setMinimumSize(QSize(32, 32))
        self.btn_send.setMaximumSize(QSize(32, 32))
        self.btn_send.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_send.setText(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/send", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_send.setIcon(icon4)

        self.layout_messagebox.addWidget(self.btn_send, 0, Qt.AlignmentFlag.AlignBottom)

        self.layout_messagebox.setStretch(1, 1)

        self.layout_chat_frame.addWidget(self.frame_messagebox)


        self.layout_main_page.addWidget(self.frame_chat, 1, 2, 2, 1)

        self.layout_main_page.setRowStretch(1, 1)
        self.layout_main_page.setColumnStretch(2, 1)
        QWidget.setTabOrder(self.scroll_servers, self.btn_server_title)
        QWidget.setTabOrder(self.btn_server_title, self.btn_profile)
        QWidget.setTabOrder(self.btn_profile, self.btn_search)
        QWidget.setTabOrder(self.btn_search, self.btn_settings)
        QWidget.setTabOrder(self.btn_settings, self.btn_attachment)
        QWidget.setTabOrder(self.btn_attachment, self.textbox)
        QWidget.setTabOrder(self.textbox, self.btn_emoji)
        QWidget.setTabOrder(self.btn_emoji, self.btn_send)
        QWidget.setTabOrder(self.btn_send, self.scroll_chat)

        self.retranslateUi(main_page)

        QMetaObject.connectSlotsByName(main_page)
    # setupUi

    def retranslateUi(self, main_page):
        main_page.setWindowTitle(QCoreApplication.translate("main_page", u"Form", None))
        self.label_userstatus.setText(QCoreApplication.translate("main_page", u"Online", None))
        self.textbox.setPlaceholderText(QCoreApplication.translate("main_page", u"Message #chat-name", None))
    # retranslateUi


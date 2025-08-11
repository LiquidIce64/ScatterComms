# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from widgets.common import (FrameButton, RoundedImage)
import index_rc

class Ui_main_page(object):
    def setupUi(self, main_page):
        if not main_page.objectName():
            main_page.setObjectName(u"main_page")
        main_page.resize(1000, 600)
        main_page.setMinimumSize(QSize(1000, 600))
        main_page.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        main_page.setStyleSheet(u"#frame_side_panel, #btn_server_title, #frame_chat_title, #frame_controls {\n"
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
"#scrollcontent_servers {\n"
"	background-color: #151515;\n"
"}\n"
"\n"
"#divider_servers {\n"
"	background-color: #252525;\n"
"}\n"
"\n"
"#label_servername {\n"
"	margin-left: 4px;\n"
"	font-size: 12pt;\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"#btn_server_dropdown, #btn_settings, #btn_inbox, #btn_search {\n"
"	background: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"#btn_profile {\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"#icon_userstatus {\n"
"	border: 2px solid #252525;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"#label_userstatus {\n"
"	"
                        "margin-left: 4px;\n"
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
"#btn_profile:hover, #btn_server_title:hover {\n"
"	background-color: #303030;\n"
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

        self.frame_servers = QFrame(main_page)
        self.frame_servers.setObjectName(u"frame_servers")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_servers.sizePolicy().hasHeightForWidth())
        self.frame_servers.setSizePolicy(sizePolicy1)
        self.frame_servers.setMinimumSize(QSize(60, 0))
        self.frame_servers.setMaximumSize(QSize(60, 16777215))
        self.frame_servers.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_servers.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_servers_frame = QVBoxLayout(self.frame_servers)
        self.layout_servers_frame.setSpacing(0)
        self.layout_servers_frame.setObjectName(u"layout_servers_frame")
        self.layout_servers_frame.setContentsMargins(3, 6, 1, 6)
        self.scroll_servers = QScrollArea(self.frame_servers)
        self.scroll_servers.setObjectName(u"scroll_servers")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scroll_servers.sizePolicy().hasHeightForWidth())
        self.scroll_servers.setSizePolicy(sizePolicy2)
        self.scroll_servers.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_servers.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_servers.setWidgetResizable(True)
        self.scroll_servers.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollcontent_servers = QWidget()
        self.scrollcontent_servers.setObjectName(u"scrollcontent_servers")
        self.scrollcontent_servers.setGeometry(QRect(0, 0, 54, 586))
        self.verticalLayout = QVBoxLayout(self.scrollcontent_servers)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(3, 0, 0, 0)
        self.divider_servers = QFrame(self.scrollcontent_servers)
        self.divider_servers.setObjectName(u"divider_servers")
        self.divider_servers.setMaximumSize(QSize(48, 16777215))
        self.divider_servers.setFrameShadow(QFrame.Shadow.Sunken)
        self.divider_servers.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.divider_servers)

        self.spacer_servers = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.spacer_servers)

        self.scroll_servers.setWidget(self.scrollcontent_servers)

        self.layout_servers_frame.addWidget(self.scroll_servers)

        self.spacer_servers_offset = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.layout_servers_frame.addItem(self.spacer_servers_offset)


        self.layout_main_page.addWidget(self.frame_servers, 0, 0, 3, 1)

        self.btn_server_title = FrameButton(main_page)
        self.btn_server_title.setObjectName(u"btn_server_title")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_server_title.sizePolicy().hasHeightForWidth())
        self.btn_server_title.setSizePolicy(sizePolicy3)
        self.btn_server_title.setMinimumSize(QSize(220, 46))
        self.btn_server_title.setMaximumSize(QSize(220, 46))
        self.btn_server_title.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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

        self.icon_server_dropdown = QLabel(self.btn_server_title)
        self.icon_server_dropdown.setObjectName(u"icon_server_dropdown")
        self.icon_server_dropdown.setMinimumSize(QSize(32, 32))
        self.icon_server_dropdown.setMaximumSize(QSize(32, 32))
        self.icon_server_dropdown.setText(u"")
        self.icon_server_dropdown.setPixmap(QPixmap(u":/icons/test"))
        self.icon_server_dropdown.setScaledContents(True)

        self.layout_server_title.addWidget(self.icon_server_dropdown)

        self.layout_server_title.setStretch(0, 1)

        self.layout_main_page.addWidget(self.btn_server_title, 0, 1, 1, 1)

        self.frame_controls = QFrame(main_page)
        self.frame_controls.setObjectName(u"frame_controls")
        sizePolicy3.setHeightForWidth(self.frame_controls.sizePolicy().hasHeightForWidth())
        self.frame_controls.setSizePolicy(sizePolicy3)
        self.frame_controls.setMinimumSize(QSize(260, 46))
        self.frame_controls.setMaximumSize(QSize(260, 46))
        self.frame_controls.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_controls.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_controls = QHBoxLayout(self.frame_controls)
        self.layout_controls.setSpacing(6)
        self.layout_controls.setObjectName(u"layout_controls")
        self.layout_controls.setContentsMargins(3, 3, 6, 3)
        self.btn_profile = FrameButton(self.frame_controls)
        self.btn_profile.setObjectName(u"btn_profile")
        self.btn_profile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.layout_profile = QGridLayout(self.btn_profile)
        self.layout_profile.setSpacing(0)
        self.layout_profile.setObjectName(u"layout_profile")
        self.layout_profile.setContentsMargins(3, 3, 3, 3)
        self.icon_userstatus = QLabel(self.btn_profile)
        self.icon_userstatus.setObjectName(u"icon_userstatus")
        self.icon_userstatus.setMinimumSize(QSize(12, 12))
        self.icon_userstatus.setMaximumSize(QSize(12, 12))
        self.icon_userstatus.setStyleSheet(u"background-color: green;")
        self.icon_userstatus.setText(u"")

        self.layout_profile.addWidget(self.icon_userstatus, 1, 1, 1, 1)

        self.label_username = QLabel(self.btn_profile)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setText(u"Username")

        self.layout_profile.addWidget(self.label_username, 0, 2, 1, 1)

        self.label_userstatus = QLabel(self.btn_profile)
        self.label_userstatus.setObjectName(u"label_userstatus")

        self.layout_profile.addWidget(self.label_userstatus, 1, 2, 1, 1)

        self.icon_useravatar = RoundedImage(self.btn_profile)
        self.icon_useravatar.setObjectName(u"icon_useravatar")
        self.icon_useravatar.setMinimumSize(QSize(32, 32))
        self.icon_useravatar.setMaximumSize(QSize(32, 32))
        self.icon_useravatar.setText(u"")
        self.icon_useravatar.setPixmap(QPixmap(u":/icons/test"))
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
        self.btn_search.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_search.setText(u"")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.btn_search.setIcon(icon)
        self.btn_search.setIconSize(QSize(24, 24))

        self.layout_controls.addWidget(self.btn_search)

        self.btn_settings = QPushButton(self.frame_controls)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_settings.setText(u"")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.btn_settings.setIcon(icon1)
        self.btn_settings.setIconSize(QSize(24, 24))

        self.layout_controls.addWidget(self.btn_settings)


        self.layout_main_page.addWidget(self.frame_controls, 0, 3, 1, 1)

        self.frame_side_panel = QFrame(main_page)
        self.frame_side_panel.setObjectName(u"frame_side_panel")
        sizePolicy1.setHeightForWidth(self.frame_side_panel.sizePolicy().hasHeightForWidth())
        self.frame_side_panel.setSizePolicy(sizePolicy1)
        self.frame_side_panel.setMinimumSize(QSize(220, 0))
        self.frame_side_panel.setMaximumSize(QSize(220, 16777215))
        self.frame_side_panel.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_side_panel.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_side_panel = QVBoxLayout(self.frame_side_panel)
        self.layout_side_panel.setSpacing(0)
        self.layout_side_panel.setObjectName(u"layout_side_panel")
        self.layout_side_panel.setContentsMargins(6, 6, 6, 6)
        self.spacer_side_panel = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.layout_side_panel.addItem(self.spacer_side_panel)


        self.layout_main_page.addWidget(self.frame_side_panel, 1, 1, 2, 1)

        self.layout_center_panel = QHBoxLayout()
        self.layout_center_panel.setSpacing(0)
        self.layout_center_panel.setObjectName(u"layout_center_panel")

        self.layout_main_page.addLayout(self.layout_center_panel, 1, 2, 2, 2)

        self.layout_main_page.setRowStretch(1, 1)
        self.layout_main_page.setColumnStretch(2, 1)

        self.retranslateUi(main_page)

        QMetaObject.connectSlotsByName(main_page)
    # setupUi

    def retranslateUi(self, main_page):
        main_page.setWindowTitle(QCoreApplication.translate("main_page", u"Form", None))
        self.label_userstatus.setText(QCoreApplication.translate("main_page", u"Online", None))
    # retranslateUi


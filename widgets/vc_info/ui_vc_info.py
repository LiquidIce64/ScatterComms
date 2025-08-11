# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vc_info.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_vc_info(object):
    def setupUi(self, vc_info):
        if not vc_info.objectName():
            vc_info.setObjectName(u"vc_info")
        vc_info.resize(280, 82)
        vc_info.setMinimumSize(QSize(280, 82))
        vc_info.setMaximumSize(QSize(280, 82))
        vc_info.setWindowTitle(u"Form")
        vc_info.setStyleSheet(u"#panel_vc_info {\n"
"	margin: 2px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: #353535;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"#btn_channel {\n"
"	font-size: 11pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"#btn_channel:hover {\n"
"	background: none;\n"
"	border: none;\n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"#line, #line_2 {\n"
"	background-color: #353535;\n"
"}")
        self.layout_vc_info = QVBoxLayout(vc_info)
        self.layout_vc_info.setObjectName(u"layout_vc_info")
        self.layout_vc_info.setContentsMargins(2, 0, 2, 2)
        self.frame_vc_info = QFrame(vc_info)
        self.frame_vc_info.setObjectName(u"frame_vc_info")
        self.frame_vc_info.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_vc_info.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_vc_info_frame = QVBoxLayout(self.frame_vc_info)
        self.layout_vc_info_frame.setObjectName(u"layout_vc_info_frame")
        self.btn_channel = QPushButton(self.frame_vc_info)
        self.btn_channel.setObjectName(u"btn_channel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_channel.sizePolicy().hasHeightForWidth())
        self.btn_channel.setSizePolicy(sizePolicy)
        self.btn_channel.setText(u"Server Name | channel-name")

        self.layout_vc_info_frame.addWidget(self.btn_channel)

        self.layout_buttons = QHBoxLayout()
        self.layout_buttons.setSpacing(6)
        self.layout_buttons.setObjectName(u"layout_buttons")
        self.layout_ping = QHBoxLayout()
        self.layout_ping.setSpacing(3)
        self.layout_ping.setObjectName(u"layout_ping")
        self.icon_ping = QLabel(self.frame_vc_info)
        self.icon_ping.setObjectName(u"icon_ping")
        self.icon_ping.setMinimumSize(QSize(12, 12))
        self.icon_ping.setMaximumSize(QSize(12, 12))
        self.icon_ping.setStyleSheet(u"QWidget { border: 2px solid green; border-radius: 6px; }\n"
"[status=\"talking\"] { background-color: lightgreen; }\n"
"[status=\"connecting\"] { border: 2px solid orange; }\n"
"[status=\"error\"] { border: 2px solid red; }")
        self.icon_ping.setText(u"")
        self.icon_ping.setScaledContents(True)

        self.layout_ping.addWidget(self.icon_ping)

        self.label_ping = QLabel(self.frame_vc_info)
        self.label_ping.setObjectName(u"label_ping")
        self.label_ping.setMinimumSize(QSize(0, 16))
        self.label_ping.setMaximumSize(QSize(16777215, 16))
        self.label_ping.setStyleSheet(u"[status=\"good\"] { color: green; }\n"
"[status=\"ok\"] { color: orange; }\n"
"[status=\"bad\"] { color: red; }")
        self.label_ping.setText(u"0 ms")

        self.layout_ping.addWidget(self.label_ping)


        self.layout_buttons.addLayout(self.layout_ping)

        self.line = QFrame(self.frame_vc_info)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 24))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.layout_buttons.addWidget(self.line)

        self.btn_camera = QPushButton(self.frame_vc_info)
        self.btn_camera.setObjectName(u"btn_camera")
        sizePolicy.setHeightForWidth(self.btn_camera.sizePolicy().hasHeightForWidth())
        self.btn_camera.setSizePolicy(sizePolicy)
        self.btn_camera.setMinimumSize(QSize(24, 24))
        self.btn_camera.setMaximumSize(QSize(24, 24))
        self.btn_camera.setText(u"")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.CameraVideo))
        self.btn_camera.setIcon(icon)
        self.btn_camera.setIconSize(QSize(16, 16))
        self.btn_camera.setCheckable(True)
        self.btn_camera.setChecked(False)

        self.layout_buttons.addWidget(self.btn_camera)

        self.btn_screenshare = QPushButton(self.frame_vc_info)
        self.btn_screenshare.setObjectName(u"btn_screenshare")
        sizePolicy.setHeightForWidth(self.btn_screenshare.sizePolicy().hasHeightForWidth())
        self.btn_screenshare.setSizePolicy(sizePolicy)
        self.btn_screenshare.setMinimumSize(QSize(24, 24))
        self.btn_screenshare.setMaximumSize(QSize(24, 24))
        self.btn_screenshare.setText(u"")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.Computer))
        self.btn_screenshare.setIcon(icon1)
        self.btn_screenshare.setIconSize(QSize(16, 16))
        self.btn_screenshare.setCheckable(True)
        self.btn_screenshare.setChecked(False)

        self.layout_buttons.addWidget(self.btn_screenshare)

        self.btn_mute = QPushButton(self.frame_vc_info)
        self.btn_mute.setObjectName(u"btn_mute")
        sizePolicy.setHeightForWidth(self.btn_mute.sizePolicy().hasHeightForWidth())
        self.btn_mute.setSizePolicy(sizePolicy)
        self.btn_mute.setMinimumSize(QSize(24, 24))
        self.btn_mute.setMaximumSize(QSize(24, 24))
        self.btn_mute.setText(u"")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AudioInputMicrophone))
        self.btn_mute.setIcon(icon2)
        self.btn_mute.setIconSize(QSize(16, 16))
        self.btn_mute.setCheckable(True)
        self.btn_mute.setChecked(False)

        self.layout_buttons.addWidget(self.btn_mute)

        self.btn_deafen = QPushButton(self.frame_vc_info)
        self.btn_deafen.setObjectName(u"btn_deafen")
        sizePolicy.setHeightForWidth(self.btn_deafen.sizePolicy().hasHeightForWidth())
        self.btn_deafen.setSizePolicy(sizePolicy)
        self.btn_deafen.setMinimumSize(QSize(24, 24))
        self.btn_deafen.setMaximumSize(QSize(24, 24))
        self.btn_deafen.setText(u"")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AudioVolumeHigh))
        self.btn_deafen.setIcon(icon3)
        self.btn_deafen.setIconSize(QSize(16, 16))
        self.btn_deafen.setCheckable(True)
        self.btn_deafen.setChecked(False)

        self.layout_buttons.addWidget(self.btn_deafen)

        self.line_2 = QFrame(self.frame_vc_info)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(16777215, 24))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.layout_buttons.addWidget(self.line_2)

        self.btn_disconnect = QPushButton(self.frame_vc_info)
        self.btn_disconnect.setObjectName(u"btn_disconnect")
        self.btn_disconnect.setMinimumSize(QSize(32, 24))
        self.btn_disconnect.setMaximumSize(QSize(24, 24))
        self.btn_disconnect.setText(u"")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.CallStop))
        self.btn_disconnect.setIcon(icon4)
        self.btn_disconnect.setIconSize(QSize(16, 16))

        self.layout_buttons.addWidget(self.btn_disconnect)

        self.layout_buttons.setStretch(0, 1)

        self.layout_vc_info_frame.addLayout(self.layout_buttons)


        self.layout_vc_info.addWidget(self.frame_vc_info)


        self.retranslateUi(vc_info)

        QMetaObject.connectSlotsByName(vc_info)
    # setupUi

    def retranslateUi(self, vc_info):
        pass
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'server_chat.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from widgets.chat_widget import ChatWidget

class Ui_server_chat(object):
    def setupUi(self, server_chat):
        if not server_chat.objectName():
            server_chat.setObjectName(u"server_chat")
        server_chat.resize(800, 600)
        server_chat.setStyleSheet(u"#frame_members {\n"
"	background-color: #252525;\n"
"	border-top: 1px solid #303030;\n"
"	border-left: 1px solid #303030;\n"
"	border-bottom: 1px solid #181818;\n"
"	border-right: 1px solid #181818;\n"
"}")
        self.layout_server_chat = QHBoxLayout(server_chat)
        self.layout_server_chat.setSpacing(0)
        self.layout_server_chat.setObjectName(u"layout_server_chat")
        self.layout_server_chat.setContentsMargins(0, 0, 0, 0)
        self.chat_widget = ChatWidget(server_chat)
        self.chat_widget.setObjectName(u"chat_widget")

        self.layout_server_chat.addWidget(self.chat_widget)

        self.frame_members = QFrame(server_chat)
        self.frame_members.setObjectName(u"frame_members")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_members.sizePolicy().hasHeightForWidth())
        self.frame_members.setSizePolicy(sizePolicy)
        self.frame_members.setMinimumSize(QSize(260, 0))
        self.frame_members.setMaximumSize(QSize(260, 16777215))
        self.frame_members.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_members.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_members = QVBoxLayout(self.frame_members)
        self.layout_members.setObjectName(u"layout_members")
        self.layout_members.setContentsMargins(6, 6, 6, 6)
        self.spacer_members = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_members.addItem(self.spacer_members)


        self.layout_server_chat.addWidget(self.frame_members)


        self.retranslateUi(server_chat)

        QMetaObject.connectSlotsByName(server_chat)
    # setupUi

    def retranslateUi(self, server_chat):
        server_chat.setWindowTitle(QCoreApplication.translate("server_chat", u"Form", None))
    # retranslateUi


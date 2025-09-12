# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_category.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from widgets.common import (FrameButton, IconWidget)
import index_rc

class Ui_chat_category_widget(object):
    def setupUi(self, chat_category_widget):
        if not chat_category_widget.objectName():
            chat_category_widget.setObjectName(u"chat_category_widget")
        chat_category_widget.resize(208, 127)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chat_category_widget.sizePolicy().hasHeightForWidth())
        chat_category_widget.setSizePolicy(sizePolicy)
        chat_category_widget.setMouseTracking(True)
        chat_category_widget.setAcceptDrops(True)
        chat_category_widget.setWindowTitle(u"Form")
        chat_category_widget.setStyleSheet(u"#icon_dropdown {\n"
"	color: #808080;\n"
"	margin: 2px;\n"
"}\n"
"#icon_dropdown[highlight=\"true\"] {color: white;}\n"
"\n"
"#label {\n"
"	color: #808080;\n"
"	font-size: 10pt;\n"
"	font-weight: 600;\n"
"}\n"
"#label[highlight=\"true\"] {color: white;}\n"
"\n"
"#drop_target {\n"
"	border: 2px solid #2A2A2A;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"#btn_settings, #btn_create_chat {\n"
"	background: none;\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"#btn_settings:hover, #btn_settings:focus, #btn_create_chat:hover, #btn_create_chat:focus {\n"
"	background-color: #2A2A2A;\n"
"}")
        self.layout_chat_category = QVBoxLayout(chat_category_widget)
        self.layout_chat_category.setSpacing(3)
        self.layout_chat_category.setObjectName(u"layout_chat_category")
        self.layout_chat_category.setContentsMargins(0, 0, 0, 0)
        self.btn = FrameButton(chat_category_widget)
        self.btn.setObjectName(u"btn")
        self.btn.setMinimumSize(QSize(0, 24))
        self.btn.setMaximumSize(QSize(16777215, 24))
        self.btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn.setMouseTracking(True)
        self.btn.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.layout_frame = QHBoxLayout(self.btn)
        self.layout_frame.setSpacing(3)
        self.layout_frame.setObjectName(u"layout_frame")
        self.layout_frame.setContentsMargins(6, 0, 3, 0)
        self.icon_dropdown = IconWidget(self.btn)
        self.icon_dropdown.setObjectName(u"icon_dropdown")
        self.icon_dropdown.setMinimumSize(QSize(16, 16))
        self.icon_dropdown.setMaximumSize(QSize(16, 16))
        self.icon_dropdown.setText(u"")
        self.icon_dropdown.setPixmap(QPixmap(u":/icons/arrow_down"))
        self.icon_dropdown.setScaledContents(True)

        self.layout_frame.addWidget(self.icon_dropdown)

        self.label = QLabel(self.btn)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 24))
        self.label.setMaximumSize(QSize(16777215, 24))
        self.label.setText(u"Category")

        self.layout_frame.addWidget(self.label)

        self.frame_buttons = QFrame(self.btn)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.layout_buttons = QHBoxLayout(self.frame_buttons)
        self.layout_buttons.setSpacing(0)
        self.layout_buttons.setObjectName(u"layout_buttons")
        self.layout_buttons.setContentsMargins(0, 0, 0, 0)
        self.btn_create_chat = QPushButton(self.frame_buttons)
        self.btn_create_chat.setObjectName(u"btn_create_chat")
        self.btn_create_chat.setMinimumSize(QSize(24, 24))
        self.btn_create_chat.setMaximumSize(QSize(24, 24))
        self.btn_create_chat.setText(u"")
        icon = QIcon()
        icon.addFile(u":/icons/plus", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_create_chat.setIcon(icon)
        self.btn_create_chat.setIconSize(QSize(12, 12))

        self.layout_buttons.addWidget(self.btn_create_chat)

        self.btn_settings = QPushButton(self.frame_buttons)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(24, 24))
        self.btn_settings.setMaximumSize(QSize(24, 24))
        self.btn_settings.setText(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/settings", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_settings.setIcon(icon1)
        self.btn_settings.setIconSize(QSize(12, 12))

        self.layout_buttons.addWidget(self.btn_settings)


        self.layout_frame.addWidget(self.frame_buttons)

        self.layout_frame.setStretch(1, 1)

        self.layout_chat_category.addWidget(self.btn)

        self.frame_chats = QFrame(chat_category_widget)
        self.frame_chats.setObjectName(u"frame_chats")
        sizePolicy.setHeightForWidth(self.frame_chats.sizePolicy().hasHeightForWidth())
        self.frame_chats.setSizePolicy(sizePolicy)
        self.frame_chats.setMinimumSize(QSize(0, 30))
        self.layout_chats = QVBoxLayout(self.frame_chats)
        self.layout_chats.setSpacing(3)
        self.layout_chats.setObjectName(u"layout_chats")
        self.layout_chats.setContentsMargins(0, 0, 0, 0)

        self.layout_chat_category.addWidget(self.frame_chats)


        self.retranslateUi(chat_category_widget)

        QMetaObject.connectSlotsByName(chat_category_widget)
    # setupUi

    def retranslateUi(self, chat_category_widget):
        pass
    # retranslateUi


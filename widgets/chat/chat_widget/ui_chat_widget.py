# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_widget.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

from widgets.common import (FrameButton, IconButton, IconWidget)
import index_rc

class Ui_chat_widget(object):
    def setupUi(self, chat_widget):
        if not chat_widget.objectName():
            chat_widget.setObjectName(u"chat_widget")
        chat_widget.resize(208, 30)
        chat_widget.setMinimumSize(QSize(0, 30))
        chat_widget.setMaximumSize(QSize(16777215, 30))
        chat_widget.setWindowTitle(u"Form")
        chat_widget.setStyleSheet(u"#btn {border-radius: 6px;}\n"
"#btn:hover, #btn:focus {background-color: #2A2A2A;}\n"
"#btn[checked=\"true\"] {background-color: #353535;}\n"
"\n"
"#icon {\n"
"	margin: 4px;\n"
"	color: #808080;\n"
"}\n"
"\n"
"#label {\n"
"	font-size: 11pt;\n"
"	font-weight: 600;\n"
"	color: #808080;\n"
"}\n"
"\n"
"#btn_settings {\n"
"	color: #808080;\n"
"	background: none;\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"#icon[highlight=\"true\"], #label[highlight=\"true\"], #btn_settings[highlight=\"true\"] {color: white;}")
        self.layout_widget = QVBoxLayout(chat_widget)
        self.layout_widget.setSpacing(0)
        self.layout_widget.setObjectName(u"layout_widget")
        self.layout_widget.setContentsMargins(0, 0, 0, 0)
        self.btn = FrameButton(chat_widget)
        self.btn.setObjectName(u"btn")
        self.btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn.setMouseTracking(True)
        self.btn.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.layout_btn = QHBoxLayout(self.btn)
        self.layout_btn.setSpacing(3)
        self.layout_btn.setObjectName(u"layout_btn")
        self.layout_btn.setContentsMargins(3, 3, 3, 3)
        self.icon = IconWidget(self.btn)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(24, 24))
        self.icon.setMaximumSize(QSize(24, 24))
        self.icon.setText(u"")
        self.icon.setPixmap(QPixmap(u":/icons/text_chat"))
        self.icon.setScaledContents(True)

        self.layout_btn.addWidget(self.icon)

        self.label = QLabel(self.btn)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 24))
        self.label.setMaximumSize(QSize(16777215, 24))
        self.label.setText(u"Chat")

        self.layout_btn.addWidget(self.label)

        self.frame_buttons = QFrame(self.btn)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.layout_buttons = QHBoxLayout(self.frame_buttons)
        self.layout_buttons.setSpacing(0)
        self.layout_buttons.setObjectName(u"layout_buttons")
        self.layout_buttons.setContentsMargins(0, 0, 0, 0)
        self.btn_settings = IconButton(self.frame_buttons)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(24, 24))
        self.btn_settings.setMaximumSize(QSize(24, 24))
        self.btn_settings.setText(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/settings", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_settings.setIcon(icon1)
        self.btn_settings.setIconSize(QSize(12, 12))

        self.layout_buttons.addWidget(self.btn_settings)


        self.layout_btn.addWidget(self.frame_buttons)

        self.layout_btn.setStretch(1, 1)

        self.layout_widget.addWidget(self.btn)


        self.retranslateUi(chat_widget)

        QMetaObject.connectSlotsByName(chat_widget)
    # setupUi

    def retranslateUi(self, chat_widget):
        pass
    # retranslateUi


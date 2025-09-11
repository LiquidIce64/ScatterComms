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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

from widgets.common import (FrameButton, IconWidget)
import index_rc

class Ui_chat_widget(object):
    def setupUi(self, chat_widget):
        if not chat_widget.objectName():
            chat_widget.setObjectName(u"chat_widget")
        chat_widget.resize(208, 30)
        chat_widget.setStyleSheet(u"#btn {border-radius: 6px;}\n"
"#btn:hover, #btn:focus {background-color: #2A2A2A;}\n"
"\n"
"#icon {\n"
"	margin: 4px;\n"
"	color: #808080;\n"
"}\n"
"#icon[highlight=\"true\"] {color: white;}\n"
"\n"
"#label {\n"
"	font-size: 11pt;\n"
"	font-weight: 600;\n"
"	color: #808080;\n"
"}\n"
"#label[highlight=\"true\"] {color: white;}")
        self.layout_widget = QVBoxLayout(chat_widget)
        self.layout_widget.setSpacing(0)
        self.layout_widget.setObjectName(u"layout_widget")
        self.layout_widget.setContentsMargins(0, 0, 0, 0)
        self.btn = FrameButton(chat_widget)
        self.btn.setObjectName(u"btn")
        self.btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn.setMouseTracking(True)
        self.btn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.layout_btn = QHBoxLayout(self.btn)
        self.layout_btn.setSpacing(3)
        self.layout_btn.setObjectName(u"layout_btn")
        self.layout_btn.setContentsMargins(3, 3, 3, 3)
        self.icon = IconWidget(self.btn)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(24, 24))
        self.icon.setMaximumSize(QSize(24, 24))
        self.icon.setPixmap(QPixmap(u":/icons/text_chat"))
        self.icon.setScaledContents(True)

        self.layout_btn.addWidget(self.icon)

        self.label = QLabel(self.btn)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 24))
        self.label.setMaximumSize(QSize(16777215, 24))
        self.label.setText(u"Chat")

        self.layout_btn.addWidget(self.label)


        self.layout_widget.addWidget(self.btn)


        self.retranslateUi(chat_widget)

        QMetaObject.connectSlotsByName(chat_widget)
    # setupUi

    def retranslateUi(self, chat_widget):
        chat_widget.setWindowTitle(QCoreApplication.translate("chat_widget", u"Form", None))
        self.icon.setText("")
    # retranslateUi


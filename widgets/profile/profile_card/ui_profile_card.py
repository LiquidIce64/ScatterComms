# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_card.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

from widgets.common import (FrameButton, RoundedImage)
import index_rc
import index_rc

class Ui_profile_card(object):
    def setupUi(self, profile_card):
        if not profile_card.objectName():
            profile_card.setObjectName(u"profile_card")
        profile_card.resize(172, 130)
        profile_card.setWindowTitle(u"Form")
        profile_card.setStyleSheet(u"#btn:hover, #btn:focus {\n"
"	background-color: #353535;\n"
"	border-radius: 6px;\n"
"}")
        self.layout_widget = QVBoxLayout(profile_card)
        self.layout_widget.setSpacing(0)
        self.layout_widget.setObjectName(u"layout_widget")
        self.layout_widget.setContentsMargins(0, 0, 0, 0)
        self.btn = FrameButton(profile_card)
        self.btn.setObjectName(u"btn")
        self.btn.setMaximumSize(QSize(108, 16777215))
        self.btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.layout_frame = QVBoxLayout(self.btn)
        self.layout_frame.setObjectName(u"layout_frame")
        self.layout_frame.setContentsMargins(6, 6, 6, 6)
        self.icon_avatar = RoundedImage(self.btn)
        self.icon_avatar.setObjectName(u"icon_avatar")
        self.icon_avatar.setMinimumSize(QSize(96, 96))
        self.icon_avatar.setMaximumSize(QSize(96, 96))
        self.icon_avatar.setText(u"")
        self.icon_avatar.setPixmap(QPixmap(u":/icons/test"))
        self.icon_avatar.setScaledContents(True)

        self.layout_frame.addWidget(self.icon_avatar)

        self.label_username = QLabel(self.btn)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setText(u"Username")
        self.label_username.setTextFormat(Qt.TextFormat.PlainText)
        self.label_username.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_frame.addWidget(self.label_username)


        self.layout_widget.addWidget(self.btn)


        self.retranslateUi(profile_card)

        QMetaObject.connectSlotsByName(profile_card)
    # setupUi

    def retranslateUi(self, profile_card):
        pass
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'member_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

from widgets.common import (FrameButton, IconWidget, MaskedImage)
import index_rc
import index_rc

class Ui_member_widget(object):
    def setupUi(self, member_widget):
        if not member_widget.objectName():
            member_widget.setObjectName(u"member_widget")
        member_widget.resize(250, 38)
        member_widget.setMinimumSize(QSize(0, 38))
        member_widget.setMaximumSize(QSize(16777215, 38))
        member_widget.setWindowTitle(u"Form")
        member_widget.setStyleSheet(u"#btn {border-radius: 6px;}\n"
"#btn:hover, #btn:focus, #btn[checked=\"true\"] {background-color: #303030;}\n"
"#icon_status {padding: 2px;}\n"
"\n"
"#label_status {\n"
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
"")
        self.layout_widget = QVBoxLayout(member_widget)
        self.layout_widget.setSpacing(0)
        self.layout_widget.setObjectName(u"layout_widget")
        self.layout_widget.setContentsMargins(0, 0, 0, 0)
        self.btn = FrameButton(member_widget)
        self.btn.setObjectName(u"btn")
        self.btn.setMinimumSize(QSize(0, 38))
        self.btn.setMaximumSize(QSize(16777215, 38))
        self.btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.layout_btn = QGridLayout(self.btn)
        self.layout_btn.setSpacing(0)
        self.layout_btn.setObjectName(u"layout_btn")
        self.layout_btn.setContentsMargins(3, 3, 3, 3)
        self.icon_status = IconWidget(self.btn)
        self.icon_status.setObjectName(u"icon_status")
        self.icon_status.setMinimumSize(QSize(12, 12))
        self.icon_status.setMaximumSize(QSize(12, 12))
        self.icon_status.setText(u"")
        self.icon_status.setPixmap(QPixmap(u":/status/online"))
        self.icon_status.setScaledContents(True)

        self.layout_btn.addWidget(self.icon_status, 1, 1, 1, 1)

        self.icon_avatar = MaskedImage(self.btn)
        self.icon_avatar.setObjectName(u"icon_avatar")
        self.icon_avatar.setMinimumSize(QSize(32, 32))
        self.icon_avatar.setMaximumSize(QSize(32, 32))
        self.icon_avatar.setText(u"")
        self.icon_avatar.setPixmap(QPixmap(u":/icons/avatar"))
        self.icon_avatar.setScaledContents(True)

        self.layout_btn.addWidget(self.icon_avatar, 0, 0, 1, 2)

        self.layout_labels = QVBoxLayout()
        self.layout_labels.setSpacing(0)
        self.layout_labels.setObjectName(u"layout_labels")
        self.label_username = QLabel(self.btn)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setText(u"Username")

        self.layout_labels.addWidget(self.label_username)

        self.label_status = QLabel(self.btn)
        self.label_status.setObjectName(u"label_status")

        self.layout_labels.addWidget(self.label_status)

        self.layout_labels.setStretch(0, 1)

        self.layout_btn.addLayout(self.layout_labels, 0, 2, 2, 1)

        self.layout_btn.setRowStretch(0, 1)
        self.layout_btn.setColumnStretch(2, 1)
        self.icon_avatar.raise_()
        self.icon_status.raise_()

        self.layout_widget.addWidget(self.btn)


        self.retranslateUi(member_widget)

        QMetaObject.connectSlotsByName(member_widget)
    # setupUi

    def retranslateUi(self, member_widget):
        self.label_status.setText(QCoreApplication.translate("member_widget", u"Online", None))
        pass
    # retranslateUi


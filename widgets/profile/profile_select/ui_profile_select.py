# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_select.ui'
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
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from widgets.common import (FrameButton, IconWidget)
import index_rc
import index_rc

class Ui_profile_select(object):
    def setupUi(self, profile_select):
        if not profile_select.objectName():
            profile_select.setObjectName(u"profile_select")
        profile_select.resize(1000, 600)
        profile_select.setMinimumSize(QSize(1000, 600))
        profile_select.setWindowTitle(u"Form")
        profile_select.setStyleSheet(u"#profile_select, ProfileSelect {\n"
"	background-color: #2A2A2A;\n"
"}\n"
"\n"
"#frame {\n"
"	background-color: #252525;\n"
"	border-radius: 16px;\n"
"}\n"
"\n"
"#scroll_profiles, #scrollcontent_profiles {\n"
"	background-color: #252525;\n"
"}\n"
"\n"
"#label {\n"
"	font-size: 18pt;\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"#btn_create:hover, #btn_create:focus {\n"
"	background-color: #353535;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"#icon_create {\n"
"	margin: 16px;\n"
"}")
        self.layout_widget = QVBoxLayout(profile_select)
        self.layout_widget.setObjectName(u"layout_widget")
        self.frame = QFrame(profile_select)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(700, 300))
        self.frame.setMaximumSize(QSize(700, 300))
        self.layout_frame = QVBoxLayout(self.frame)
        self.layout_frame.setSpacing(20)
        self.layout_frame.setObjectName(u"layout_frame")
        self.layout_frame.setContentsMargins(40, 40, 40, 40)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_frame.addWidget(self.label)

        self.scroll_profiles = QScrollArea(self.frame)
        self.scroll_profiles.setObjectName(u"scroll_profiles")
        self.scroll_profiles.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_profiles.setFrameShadow(QFrame.Shadow.Plain)
        self.scroll_profiles.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_profiles.setWidgetResizable(True)
        self.scroll_profiles.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollcontent_profiles = QWidget()
        self.scrollcontent_profiles.setObjectName(u"scrollcontent_profiles")
        self.scrollcontent_profiles.setGeometry(QRect(0, 0, 620, 168))
        self.layout_profiles = QHBoxLayout(self.scrollcontent_profiles)
        self.layout_profiles.setObjectName(u"layout_profiles")
        self.spacer_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_profiles.addItem(self.spacer_left)

        self.btn_create = FrameButton(self.scrollcontent_profiles)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setMaximumSize(QSize(108, 16777215))
        self.btn_create.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_create.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.layout_create = QVBoxLayout(self.btn_create)
        self.layout_create.setObjectName(u"layout_create")
        self.layout_create.setContentsMargins(6, 6, 6, 6)
        self.icon_create = IconWidget(self.btn_create)
        self.icon_create.setObjectName(u"icon_create")
        self.icon_create.setMinimumSize(QSize(96, 96))
        self.icon_create.setMaximumSize(QSize(96, 96))
        self.icon_create.setText(u"")
        self.icon_create.setPixmap(QPixmap(u":/icons/plus"))
        self.icon_create.setScaledContents(True)

        self.layout_create.addWidget(self.icon_create)

        self.label_create = QLabel(self.btn_create)
        self.label_create.setObjectName(u"label_create")
        self.label_create.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_create.addWidget(self.label_create)


        self.layout_profiles.addWidget(self.btn_create)

        self.spacer_right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_profiles.addItem(self.spacer_right)

        self.scroll_profiles.setWidget(self.scrollcontent_profiles)

        self.layout_frame.addWidget(self.scroll_profiles)


        self.layout_widget.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        QWidget.setTabOrder(self.scroll_profiles, self.btn_create)

        self.retranslateUi(profile_select)

        QMetaObject.connectSlotsByName(profile_select)
    # setupUi

    def retranslateUi(self, profile_select):
        self.label.setText(QCoreApplication.translate("profile_select", u"Select profile", None))
        self.label_create.setText(QCoreApplication.translate("profile_select", u"New Profile", None))
        pass
    # retranslateUi


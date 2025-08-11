# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_button.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)
import index_rc

class Ui_menu_button(object):
    def setupUi(self, menu_button):
        if not menu_button.objectName():
            menu_button.setObjectName(u"menu_button")
        menu_button.resize(268, 36)
        menu_button.setWindowTitle(u"Form")
        menu_button.setStyleSheet(u"#btn {\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"#btn:hover {\n"
"	background-color: #353535;\n"
"}\n"
"\n"
"#label {\n"
"	font-size: 11pt;\n"
"	font-weight: 600;\n"
"}")
        self.layout_menu_button_widget = QVBoxLayout(menu_button)
        self.layout_menu_button_widget.setSpacing(0)
        self.layout_menu_button_widget.setObjectName(u"layout_menu_button_widget")
        self.layout_menu_button_widget.setContentsMargins(0, 0, 0, 0)
        self.btn = QFrame(menu_button)
        self.btn.setObjectName(u"btn")
        self.layout_menu_button = QHBoxLayout(self.btn)
        self.layout_menu_button.setSpacing(3)
        self.layout_menu_button.setObjectName(u"layout_menu_button")
        self.layout_menu_button.setContentsMargins(6, 6, 6, 6)
        self.label = QLabel(self.btn)
        self.label.setObjectName(u"label")
        self.label.setText(u"Menu button name")

        self.layout_menu_button.addWidget(self.label)

        self.icon = QLabel(self.btn)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(24, 24))
        self.icon.setMaximumSize(QSize(24, 24))
        self.icon.setText(u"")
        self.icon.setPixmap(QPixmap(u":/icons/test"))
        self.icon.setScaledContents(True)

        self.layout_menu_button.addWidget(self.icon)


        self.layout_menu_button_widget.addWidget(self.btn)


        self.retranslateUi(menu_button)

        QMetaObject.connectSlotsByName(menu_button)
    # setupUi

    def retranslateUi(self, menu_button):
        pass
    # retranslateUi


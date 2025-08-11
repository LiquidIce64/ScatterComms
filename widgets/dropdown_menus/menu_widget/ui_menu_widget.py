# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_menu_widget(object):
    def setupUi(self, menu_widget):
        if not menu_widget.objectName():
            menu_widget.setObjectName(u"menu_widget")
        menu_widget.resize(280, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(menu_widget.sizePolicy().hasHeightForWidth())
        menu_widget.setSizePolicy(sizePolicy)
        menu_widget.setWindowTitle(u"Form")
        self.layout_menu_widget = QVBoxLayout(menu_widget)
        self.layout_menu_widget.setSpacing(0)
        self.layout_menu_widget.setObjectName(u"layout_menu_widget")
        self.layout_menu_widget.setContentsMargins(3, 3, 3, 3)
        self.frame_menu = QFrame(menu_widget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_menu = QVBoxLayout(self.frame_menu)
        self.layout_menu.setSpacing(3)
        self.layout_menu.setObjectName(u"layout_menu")
        self.layout_menu.setContentsMargins(6, 6, 6, 6)

        self.layout_menu_widget.addWidget(self.frame_menu)

        self.spacer_menu = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_menu_widget.addItem(self.spacer_menu)


        self.retranslateUi(menu_widget)

        QMetaObject.connectSlotsByName(menu_widget)
    # setupUi

    def retranslateUi(self, menu_widget):
        pass
    # retranslateUi


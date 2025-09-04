# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'server_widget.ui'
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

from widgets.common import (FrameButton, MaskedImage)
import index_rc
import index_rc

class Ui_widget_server(object):
    def setupUi(self, widget_server):
        if not widget_server.objectName():
            widget_server.setObjectName(u"widget_server")
        widget_server.resize(172, 40)
        widget_server.setMouseTracking(True)
        widget_server.setWindowTitle(u"Form")
        widget_server.setStyleSheet(u"#line {\n"
"	background-color: white;\n"
"	border-radius: 2px;\n"
"}")
        self.layout_widget = QVBoxLayout(widget_server)
        self.layout_widget.setSpacing(0)
        self.layout_widget.setObjectName(u"layout_widget")
        self.layout_widget.setContentsMargins(0, 0, 0, 0)
        self.btn = FrameButton(widget_server)
        self.btn.setObjectName(u"btn")
        self.btn.setMinimumSize(QSize(52, 40))
        self.btn.setMaximumSize(QSize(52, 40))
        self.btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.layout_btn = QHBoxLayout(self.btn)
        self.layout_btn.setSpacing(2)
        self.layout_btn.setObjectName(u"layout_btn")
        self.layout_btn.setContentsMargins(0, 0, 6, 0)
        self.line = QLabel(self.btn)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 4))
        self.line.setMaximumSize(QSize(4, 40))
        self.line.setText(u"")

        self.layout_btn.addWidget(self.line, 0, Qt.AlignmentFlag.AlignVCenter)

        self.icon = MaskedImage(self.btn)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(40, 40))
        self.icon.setMaximumSize(QSize(40, 40))
        self.icon.setText(u"")
        self.icon.setPixmap(QPixmap(u":/icons/test"))
        self.icon.setScaledContents(True)

        self.layout_btn.addWidget(self.icon, 0, Qt.AlignmentFlag.AlignRight)


        self.layout_widget.addWidget(self.btn)


        self.retranslateUi(widget_server)

        QMetaObject.connectSlotsByName(widget_server)
    # setupUi

    def retranslateUi(self, widget_server):
        pass
    # retranslateUi


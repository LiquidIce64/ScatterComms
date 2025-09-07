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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

from widgets.common import MaskedImage
import index_rc

class Ui_widget_server(object):
    def setupUi(self, widget_server):
        if not widget_server.objectName():
            widget_server.setObjectName(u"widget_server")
        widget_server.resize(172, 40)
        widget_server.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        widget_server.setMouseTracking(True)
        widget_server.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        widget_server.setWindowTitle(u"Form")
        widget_server.setStyleSheet(u"#line {\n"
"	background-color: white;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#icon {\n"
"	background-color: #2A2A2A;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#saved_messages #icon {\n"
"	padding: 8px;\n"
"}\n"
"")
        self.layout_widget = QVBoxLayout(widget_server)
        self.layout_widget.setSpacing(0)
        self.layout_widget.setObjectName(u"layout_widget")
        self.layout_widget.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(widget_server)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(52, 40))
        self.frame.setMaximumSize(QSize(52, 40))
        self.layout_frame = QHBoxLayout(self.frame)
        self.layout_frame.setSpacing(2)
        self.layout_frame.setObjectName(u"layout_frame")
        self.layout_frame.setContentsMargins(0, 0, 6, 0)
        self.line = QLabel(self.frame)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 4))
        self.line.setMaximumSize(QSize(4, 40))
        self.line.setText(u"")

        self.layout_frame.addWidget(self.line, 0, Qt.AlignmentFlag.AlignVCenter)

        self.icon = MaskedImage(self.frame)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(40, 40))
        self.icon.setMaximumSize(QSize(40, 40))
        self.icon.setText(u"")
        self.icon.setPixmap(QPixmap(u":/icons/server"))
        self.icon.setScaledContents(True)

        self.layout_frame.addWidget(self.icon, 0, Qt.AlignmentFlag.AlignRight)


        self.layout_widget.addWidget(self.frame)


        self.retranslateUi(widget_server)

        QMetaObject.connectSlotsByName(widget_server)
    # setupUi

    def retranslateUi(self, widget_server):
        pass
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'member_category.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_member_category(object):
    def setupUi(self, member_category):
        if not member_category.objectName():
            member_category.setObjectName(u"member_category")
        member_category.resize(250, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(member_category.sizePolicy().hasHeightForWidth())
        member_category.setSizePolicy(sizePolicy)
        member_category.setWindowTitle(u"Form")
        member_category.setStyleSheet(u"#label_name, #label_count {\n"
"	font-size: 10pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"#label_count {\n"
"	padding-left: 6px;\n"
"	padding-right: 6px;\n"
"	background-color: #353535;\n"
"	border-radius: 9px;\n"
"}")
        self.layout_widget = QGridLayout(member_category)
        self.layout_widget.setSpacing(3)
        self.layout_widget.setObjectName(u"layout_widget")
        self.layout_widget.setContentsMargins(0, 0, 0, 0)
        self.label_count = QLabel(member_category)
        self.label_count.setObjectName(u"label_count")
        self.label_count.setText(u"1")
        self.label_count.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_widget.addWidget(self.label_count, 0, 1, 1, 1)

        self.label_name = QLabel(member_category)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setIndent(3)

        self.layout_widget.addWidget(self.label_name, 0, 0, 1, 1)

        self.frame = QFrame(member_category)
        self.frame.setObjectName(u"frame")
        self.layout_members = QVBoxLayout(self.frame)
        self.layout_members.setSpacing(1)
        self.layout_members.setObjectName(u"layout_members")
        self.layout_members.setContentsMargins(0, 0, 0, 0)

        self.layout_widget.addWidget(self.frame, 1, 0, 1, 3)

        self.layout_widget.setRowStretch(1, 1)
        self.layout_widget.setColumnStretch(2, 1)

        self.retranslateUi(member_category)

        QMetaObject.connectSlotsByName(member_category)
    # setupUi

    def retranslateUi(self, member_category):
        self.label_name.setText(QCoreApplication.translate("member_category", u"Online", None))
        pass
    # retranslateUi


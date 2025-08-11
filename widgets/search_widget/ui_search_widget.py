# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_search_widget(object):
    def setupUi(self, search_widget):
        if not search_widget.objectName():
            search_widget.setObjectName(u"search_widget")
        search_widget.resize(293, 600)
        search_widget.setStyleSheet(u"#scroll_search_results, #scrollcontent_search_results {\n"
"	background-color: transparent;\n"
"}")
        self.layout_search_widget = QVBoxLayout(search_widget)
        self.layout_search_widget.setSpacing(0)
        self.layout_search_widget.setObjectName(u"layout_search_widget")
        self.layout_search_widget.setContentsMargins(3, 3, 3, 3)
        self.frame_search = QFrame(search_widget)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_search.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_search = QVBoxLayout(self.frame_search)
        self.layout_search.setSpacing(6)
        self.layout_search.setObjectName(u"layout_search")
        self.layout_search.setContentsMargins(6, 6, 6, 6)
        self.text_query = QLineEdit(self.frame_search)
        self.text_query.setObjectName(u"text_query")

        self.layout_search.addWidget(self.text_query)

        self.scroll_search_results = QScrollArea(self.frame_search)
        self.scroll_search_results.setObjectName(u"scroll_search_results")
        self.scroll_search_results.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_search_results.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_search_results.setWidgetResizable(True)
        self.scroll_search_results.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollcontent_search_results = QWidget()
        self.scrollcontent_search_results.setObjectName(u"scrollcontent_search_results")
        self.scrollcontent_search_results.setGeometry(QRect(0, 0, 273, 553))
        self.scroll_search_results.setWidget(self.scrollcontent_search_results)

        self.layout_search.addWidget(self.scroll_search_results)


        self.layout_search_widget.addWidget(self.frame_search)


        self.retranslateUi(search_widget)

        QMetaObject.connectSlotsByName(search_widget)
    # setupUi

    def retranslateUi(self, search_widget):
        search_widget.setWindowTitle(QCoreApplication.translate("search_widget", u"Form", None))
        self.text_query.setPlaceholderText(QCoreApplication.translate("search_widget", u"Search", None))
    # retranslateUi


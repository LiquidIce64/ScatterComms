# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_chat_widget(object):
    def setupUi(self, chat_widget):
        if not chat_widget.objectName():
            chat_widget.setObjectName(u"chat_widget")
        chat_widget.resize(800, 600)
        chat_widget.setWindowTitle(u"Form")
        chat_widget.setStyleSheet(u"#scroll_chat, #scrollcontent_chat {background-color: #2A2A2A;}\n"
"\n"
"#frame_messagebox {background-color: #353535;}\n"
"\n"
"#textbox {\n"
"	background-color: #353535;\n"
"	font-size: 10pt;\n"
"}\n"
"\n"
"#btn_attachment, #btn_emoji, #btn_send {\n"
"	background: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"#frame_members {\n"
"	background-color: #252525;\n"
"	border-top: 1px solid #303030;\n"
"	border-left: 1px solid #303030;\n"
"	border-bottom: 1px solid #181818;\n"
"	border-right: 1px solid #181818;\n"
"}")
        self.layout_chat_widget = QVBoxLayout(chat_widget)
        self.layout_chat_widget.setSpacing(0)
        self.layout_chat_widget.setObjectName(u"layout_chat_widget")
        self.layout_chat_widget.setContentsMargins(0, 0, 0, 0)
        self.scroll_chat = QScrollArea(chat_widget)
        self.scroll_chat.setObjectName(u"scroll_chat")
        self.scroll_chat.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_chat.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_chat.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_chat.setWidgetResizable(True)
        self.scroll_chat.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.scrollcontent_chat = QWidget()
        self.scrollcontent_chat.setObjectName(u"scrollcontent_chat")
        self.scrollcontent_chat.setGeometry(QRect(0, 0, 800, 450))
        self.verticalLayout_2 = QVBoxLayout(self.scrollcontent_chat)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.spacer_chat = QSpacerItem(20, 487, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.spacer_chat)

        self.scroll_chat.setWidget(self.scrollcontent_chat)

        self.layout_chat_widget.addWidget(self.scroll_chat)

        self.frame_messagebox = QFrame(chat_widget)
        self.frame_messagebox.setObjectName(u"frame_messagebox")
        self.frame_messagebox.setMinimumSize(QSize(0, 50))
        self.frame_messagebox.setMaximumSize(QSize(16777215, 150))
        self.frame_messagebox.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_messagebox.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_messagebox = QHBoxLayout(self.frame_messagebox)
        self.layout_messagebox.setObjectName(u"layout_messagebox")
        self.btn_attachment = QPushButton(self.frame_messagebox)
        self.btn_attachment.setObjectName(u"btn_attachment")
        self.btn_attachment.setMinimumSize(QSize(32, 32))
        self.btn_attachment.setMaximumSize(QSize(32, 32))
        self.btn_attachment.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.btn_attachment.setIcon(icon)
        self.btn_attachment.setIconSize(QSize(24, 24))

        self.layout_messagebox.addWidget(self.btn_attachment, 0, Qt.AlignmentFlag.AlignBottom)

        self.textbox = QTextEdit(self.frame_messagebox)
        self.textbox.setObjectName(u"textbox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textbox.sizePolicy().hasHeightForWidth())
        self.textbox.setSizePolicy(sizePolicy)
        self.textbox.setMinimumSize(QSize(0, 30))
        self.textbox.setMaximumSize(QSize(16777215, 132))
        self.textbox.setFrameShape(QFrame.Shape.NoFrame)
        self.textbox.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.textbox.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textbox.setDocumentTitle(u"")
        self.textbox.setUndoRedoEnabled(False)
        self.textbox.setMarkdown(u"")
        self.textbox.setHtml(u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.textbox.setTabStopDistance(20.000000000000000)
        self.textbox.setAcceptRichText(True)

        self.layout_messagebox.addWidget(self.textbox)

        self.btn_emoji = QPushButton(self.frame_messagebox)
        self.btn_emoji.setObjectName(u"btn_emoji")
        self.btn_emoji.setMinimumSize(QSize(32, 32))
        self.btn_emoji.setMaximumSize(QSize(32, 32))
        self.btn_emoji.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InsertLink))
        self.btn_emoji.setIcon(icon1)
        self.btn_emoji.setIconSize(QSize(24, 24))

        self.layout_messagebox.addWidget(self.btn_emoji, 0, Qt.AlignmentFlag.AlignBottom)

        self.btn_send = QPushButton(self.frame_messagebox)
        self.btn_send.setObjectName(u"btn_send")
        self.btn_send.setEnabled(False)
        self.btn_send.setMinimumSize(QSize(32, 32))
        self.btn_send.setMaximumSize(QSize(32, 32))
        self.btn_send.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSend))
        self.btn_send.setIcon(icon2)
        self.btn_send.setIconSize(QSize(24, 24))

        self.layout_messagebox.addWidget(self.btn_send, 0, Qt.AlignmentFlag.AlignBottom)

        self.layout_messagebox.setStretch(1, 1)

        self.layout_chat_widget.addWidget(self.frame_messagebox)

        self.layout_chat_widget.setStretch(0, 1)

        self.retranslateUi(chat_widget)

        QMetaObject.connectSlotsByName(chat_widget)
    # setupUi

    def retranslateUi(self, chat_widget):
        self.btn_attachment.setText("")
        self.textbox.setPlaceholderText(QCoreApplication.translate("chat_widget", u"Message #chat-name", None))
        self.btn_emoji.setText("")
        self.btn_send.setText("")
        pass
    # retranslateUi


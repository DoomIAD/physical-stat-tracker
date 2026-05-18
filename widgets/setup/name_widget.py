# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'name_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_name_widget(object):
    def setupUi(self, name_widget):
        if not name_widget.objectName():
            name_widget.setObjectName(u"name_widget")
        name_widget.resize(723, 477)
        self.gridLayout = QGridLayout(name_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.centerLayout = QVBoxLayout()
        self.centerLayout.setObjectName(u"centerLayout")
        self.name_title = QLabel(name_widget)
        self.name_title.setObjectName(u"name_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_title.sizePolicy().hasHeightForWidth())
        self.name_title.setSizePolicy(sizePolicy)
        self.name_title.setScaledContents(False)
        self.name_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_title.setWordWrap(False)

        self.centerLayout.addWidget(self.name_title)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.centerLayout.addItem(self.verticalSpacer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.name_TextEdit = QPlainTextEdit(name_widget)
        self.name_TextEdit.setObjectName(u"name_TextEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name_TextEdit.sizePolicy().hasHeightForWidth())
        self.name_TextEdit.setSizePolicy(sizePolicy1)
        self.name_TextEdit.setMinimumSize(QSize(0, 10))
        self.name_TextEdit.setMaximumSize(QSize(16777215, 50))
        self.name_TextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.name_TextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.gridLayout_2.addWidget(self.name_TextEdit, 0, 1, 1, 1)

        self.continue_button = QPushButton(name_widget)
        self.continue_button.setObjectName(u"continue_button")

        self.gridLayout_2.addWidget(self.continue_button, 1, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 2)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.centerLayout.addLayout(self.gridLayout_2)

        self.centerLayout.setStretch(0, 4)
        self.centerLayout.setStretch(1, 1)
        self.centerLayout.setStretch(2, 2)

        self.gridLayout.addLayout(self.centerLayout, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 10)
        self.gridLayout.setRowStretch(2, 1)

        self.retranslateUi(name_widget)

        QMetaObject.connectSlotsByName(name_widget)
    # setupUi

    def retranslateUi(self, name_widget):
        name_widget.setWindowTitle(QCoreApplication.translate("name_widget", u"Stat Tracker", None))
        self.name_title.setText(QCoreApplication.translate("name_widget", u"What is Your Name?", None))
        self.name_TextEdit.setPlaceholderText(QCoreApplication.translate("name_widget", u"John Doe", None))
        self.continue_button.setText(QCoreApplication.translate("name_widget", u"Continue", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'height_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_height_widget(object):
    def setupUi(self, height_widget):
        if not height_widget.objectName():
            height_widget.setObjectName(u"height_widget")
        height_widget.resize(830, 514)
        self.gridLayout = QGridLayout(height_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.centerLayout = QVBoxLayout()
        self.centerLayout.setObjectName(u"centerLayout")
        self.height_title = QLabel(height_widget)
        self.height_title.setObjectName(u"height_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.height_title.sizePolicy().hasHeightForWidth())
        self.height_title.setSizePolicy(sizePolicy)
        self.height_title.setScaledContents(False)
        self.height_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.height_title.setWordWrap(False)

        self.centerLayout.addWidget(self.height_title)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.centerLayout.addItem(self.verticalSpacer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.in_label = QLabel(height_widget)
        self.in_label.setObjectName(u"in_label")

        self.gridLayout_2.addWidget(self.in_label, 0, 4, 1, 1)

        self.ft_textEdit = QTextEdit(height_widget)
        self.ft_textEdit.setObjectName(u"ft_textEdit")
        self.ft_textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ft_textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ft_textEdit.setOverwriteMode(True)
        self.ft_textEdit.setAcceptRichText(False)

        self.gridLayout_2.addWidget(self.ft_textEdit, 0, 1, 1, 1)

        self.in_textEdit = QTextEdit(height_widget)
        self.in_textEdit.setObjectName(u"in_textEdit")
        self.in_textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.in_textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.in_textEdit.setOverwriteMode(True)
        self.in_textEdit.setAcceptRichText(False)

        self.gridLayout_2.addWidget(self.in_textEdit, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.ft_label = QLabel(height_widget)
        self.ft_label.setObjectName(u"ft_label")

        self.gridLayout_2.addWidget(self.ft_label, 0, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(3, 1)
        self.gridLayout_2.setColumnStretch(5, 2)

        self.centerLayout.addLayout(self.gridLayout_2)

        self.centerLayout.setStretch(0, 5)
        self.centerLayout.setStretch(1, 1)
        self.centerLayout.setStretch(2, 1)

        self.gridLayout.addLayout(self.centerLayout, 1, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.continue_button = QPushButton(height_widget)
        self.continue_button.setObjectName(u"continue_button")

        self.gridLayout_3.addWidget(self.continue_button, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 1)

        self.gridLayout.addLayout(self.gridLayout_3, 2, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 12)
        self.gridLayout.setRowStretch(3, 1)

        self.retranslateUi(height_widget)

        QMetaObject.connectSlotsByName(height_widget)
    # setupUi

    def retranslateUi(self, height_widget):
        height_widget.setWindowTitle(QCoreApplication.translate("height_widget", u"Stat Tracker", None))
        self.height_title.setText(QCoreApplication.translate("height_widget", u"How Tall are You?", None))
        self.in_label.setText(QCoreApplication.translate("height_widget", u"in", None))
        self.ft_textEdit.setPlaceholderText(QCoreApplication.translate("height_widget", u"5", None))
        self.in_textEdit.setPlaceholderText(QCoreApplication.translate("height_widget", u"6", None))
        self.ft_label.setText(QCoreApplication.translate("height_widget", u"ft", None))
        self.continue_button.setText(QCoreApplication.translate("height_widget", u"Continue", None))
    # retranslateUi


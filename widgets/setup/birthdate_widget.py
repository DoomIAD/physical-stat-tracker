# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'birthdate_widget.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateEdit, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_birthdate_widget(object):
    def setupUi(self, birthdate_widget):
        if not birthdate_widget.objectName():
            birthdate_widget.setObjectName(u"birthdate_widget")
        birthdate_widget.resize(723, 477)
        self.gridLayout = QGridLayout(birthdate_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.centerLayout = QVBoxLayout()
        self.centerLayout.setObjectName(u"centerLayout")
        self.birthdate_title = QLabel(birthdate_widget)
        self.birthdate_title.setObjectName(u"birthdate_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.birthdate_title.sizePolicy().hasHeightForWidth())
        self.birthdate_title.setSizePolicy(sizePolicy)
        self.birthdate_title.setScaledContents(False)
        self.birthdate_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.birthdate_title.setWordWrap(False)

        self.centerLayout.addWidget(self.birthdate_title)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.centerLayout.addItem(self.verticalSpacer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.birthdate_dateEdit = QDateEdit(birthdate_widget)
        self.birthdate_dateEdit.setObjectName(u"birthdate_dateEdit")
        self.birthdate_dateEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.birthdate_dateEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.birthdate_dateEdit.setMaximumDate(QDate(2025, 12, 31))
        self.birthdate_dateEdit.setMinimumDate(QDate(1900, 9, 14))
        self.birthdate_dateEdit.setDate(QDate(1999, 9, 1))

        self.gridLayout_2.addWidget(self.birthdate_dateEdit, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.continue_button = QPushButton(birthdate_widget)
        self.continue_button.setObjectName(u"continue_button")

        self.gridLayout_2.addWidget(self.continue_button, 1, 1, 1, 1)

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

        self.retranslateUi(birthdate_widget)

        QMetaObject.connectSlotsByName(birthdate_widget)
    # setupUi

    def retranslateUi(self, birthdate_widget):
        birthdate_widget.setWindowTitle(QCoreApplication.translate("birthdate_widget", u"Stat Tracker", None))
        self.birthdate_title.setText(QCoreApplication.translate("birthdate_widget", u"When is your Birthdate?", None))
        self.birthdate_dateEdit.setDisplayFormat(QCoreApplication.translate("birthdate_widget", u"MM/dd/yyyy", None))
        self.continue_button.setText(QCoreApplication.translate("birthdate_widget", u"Continue", None))
    # retranslateUi


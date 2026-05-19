# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weight_widget.ui'
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

class Ui_weight_widget(object):
    def setupUi(self, weight_widget):
        if not weight_widget.objectName():
            weight_widget.setObjectName(u"weight_widget")
        weight_widget.resize(723, 477)
        self.gridLayout = QGridLayout(weight_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.centerLayout = QVBoxLayout()
        self.centerLayout.setObjectName(u"centerLayout")
        self.weight_title = QLabel(weight_widget)
        self.weight_title.setObjectName(u"weight_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weight_title.sizePolicy().hasHeightForWidth())
        self.weight_title.setSizePolicy(sizePolicy)
        self.weight_title.setScaledContents(False)
        self.weight_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.weight_title.setWordWrap(False)

        self.centerLayout.addWidget(self.weight_title)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.centerLayout.addItem(self.verticalSpacer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.weight_label = QLabel(weight_widget)
        self.weight_label.setObjectName(u"weight_label")

        self.gridLayout_2.addWidget(self.weight_label, 0, 2, 1, 1)

        self.weight_textEdit = QTextEdit(weight_widget)
        self.weight_textEdit.setObjectName(u"weight_textEdit")
        self.weight_textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.weight_textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.weight_textEdit.setOverwriteMode(True)
        self.weight_textEdit.setAcceptRichText(False)

        self.gridLayout_2.addWidget(self.weight_textEdit, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.continue_button = QPushButton(weight_widget)
        self.continue_button.setObjectName(u"continue_button")

        self.gridLayout_2.addWidget(self.continue_button, 1, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(3, 1)

        self.centerLayout.addLayout(self.gridLayout_2)

        self.centerLayout.setStretch(0, 4)
        self.centerLayout.setStretch(1, 1)
        self.centerLayout.setStretch(2, 2)

        self.gridLayout.addLayout(self.centerLayout, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)

        self.retranslateUi(weight_widget)

        QMetaObject.connectSlotsByName(weight_widget)
    # setupUi

    def retranslateUi(self, weight_widget):
        weight_widget.setWindowTitle(QCoreApplication.translate("weight_widget", u"Stat Tracker", None))
        self.weight_title.setText(QCoreApplication.translate("weight_widget", u"How Much do You Weigh?", None))
        self.weight_label.setText(QCoreApplication.translate("weight_widget", u"lb", None))
        self.weight_textEdit.setPlaceholderText(QCoreApplication.translate("weight_widget", u"6", None))
        self.continue_button.setText(QCoreApplication.translate("weight_widget", u"Continue", None))
    # retranslateUi


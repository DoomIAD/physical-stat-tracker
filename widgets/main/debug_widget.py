# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'debug_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_debug_widget(object):
    def setupUi(self, debug_widget):
        if not debug_widget.objectName():
            debug_widget.setObjectName(u"debug_widget")
        debug_widget.resize(723, 477)
        self.gridLayout = QGridLayout(debug_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.centerLayout = QVBoxLayout()
        self.centerLayout.setObjectName(u"centerLayout")
        self.debug_title = QLabel(debug_widget)
        self.debug_title.setObjectName(u"debug_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debug_title.sizePolicy().hasHeightForWidth())
        self.debug_title.setSizePolicy(sizePolicy)
        self.debug_title.setScaledContents(False)
        self.debug_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.debug_title.setWordWrap(False)

        self.centerLayout.addWidget(self.debug_title)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.centerLayout.addItem(self.verticalSpacer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.weight_label = QLabel(debug_widget)
        self.weight_label.setObjectName(u"weight_label")

        self.gridLayout_2.addWidget(self.weight_label, 2, 1, 1, 1)

        self.name_label = QLabel(debug_widget)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout_2.addWidget(self.name_label, 0, 1, 1, 1)

        self.height_label = QLabel(debug_widget)
        self.height_label.setObjectName(u"height_label")

        self.gridLayout_2.addWidget(self.height_label, 3, 1, 1, 1)

        self.birthdate_label = QLabel(debug_widget)
        self.birthdate_label.setObjectName(u"birthdate_label")

        self.gridLayout_2.addWidget(self.birthdate_label, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

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
        self.gridLayout.setRowStretch(1, 10)
        self.gridLayout.setRowStretch(2, 1)

        self.retranslateUi(debug_widget)

        QMetaObject.connectSlotsByName(debug_widget)
    # setupUi

    def retranslateUi(self, debug_widget):
        debug_widget.setWindowTitle(QCoreApplication.translate("debug_widget", u"Stat Tracker", None))
        self.debug_title.setText(QCoreApplication.translate("debug_widget", u"DEBUG", None))
        self.weight_label.setText(QCoreApplication.translate("debug_widget", u"Weight", None))
        self.name_label.setText(QCoreApplication.translate("debug_widget", u"Name", None))
        self.height_label.setText(QCoreApplication.translate("debug_widget", u"Height", None))
        self.birthdate_label.setText(QCoreApplication.translate("debug_widget", u"Birthdata", None))
    # retranslateUi


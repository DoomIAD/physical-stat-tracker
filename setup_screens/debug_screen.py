# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'debug_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QSizePolicy, QSpacerItem, QStatusBar, QWidget)

class Ui_debug_screen(object):
    def setupUi(self, debug_screen):
        if not debug_screen.objectName():
            debug_screen.setObjectName(u"debug_screen")
        debug_screen.resize(708, 637)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AddressBookNew))
        debug_screen.setWindowIcon(icon)
        self.debug_widget = QWidget(debug_screen)
        self.debug_widget.setObjectName(u"debug_widget")
        self.gridLayout = QGridLayout(self.debug_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.name_label = QLabel(self.debug_widget)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout_2.addWidget(self.name_label, 0, 1, 1, 1)

        self.birthdate_label = QLabel(self.debug_widget)
        self.birthdate_label.setObjectName(u"birthdate_label")

        self.gridLayout_2.addWidget(self.birthdate_label, 1, 1, 1, 1)

        self.weight_label = QLabel(self.debug_widget)
        self.weight_label.setObjectName(u"weight_label")

        self.gridLayout_2.addWidget(self.weight_label, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.Height_label = QLabel(self.debug_widget)
        self.Height_label.setObjectName(u"Height_label")

        self.gridLayout_2.addWidget(self.Height_label, 3, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 6)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.gridLayout.addLayout(self.gridLayout_2, 3, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.debug_title = QLabel(self.debug_widget)
        self.debug_title.setObjectName(u"debug_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debug_title.sizePolicy().hasHeightForWidth())
        self.debug_title.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.debug_title, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 6)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 2)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 5)
        self.gridLayout.setColumnStretch(2, 1)
        debug_screen.setCentralWidget(self.debug_widget)
        self.statusbar = QStatusBar(debug_screen)
        self.statusbar.setObjectName(u"statusbar")
        debug_screen.setStatusBar(self.statusbar)

        self.retranslateUi(debug_screen)

        QMetaObject.connectSlotsByName(debug_screen)
    # setupUi

    def retranslateUi(self, debug_screen):
        debug_screen.setWindowTitle(QCoreApplication.translate("debug_screen", u"Stat Tracker", None))
        self.name_label.setText(QCoreApplication.translate("debug_screen", u"Name?", None))
        self.birthdate_label.setText(QCoreApplication.translate("debug_screen", u"Birthdate?", None))
        self.weight_label.setText(QCoreApplication.translate("debug_screen", u"Weight?", None))
        self.Height_label.setText(QCoreApplication.translate("debug_screen", u"Height?", None))
        self.debug_title.setText(QCoreApplication.translate("debug_screen", u"<html><head/><body><p align=\"center\">DEBUG SCREEN</p></body></html>", None))
    # retranslateUi


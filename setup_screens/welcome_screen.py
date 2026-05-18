# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome_screen.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QWidget)

class Ui_welcome_screen(object):
    def setupUi(self, welcome_screen):
        if not welcome_screen.objectName():
            welcome_screen.setObjectName(u"welcome_screen")
        welcome_screen.resize(636, 448)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AddressBookNew))
        welcome_screen.setWindowIcon(icon)
        self.welcome_widget = QWidget(welcome_screen)
        self.welcome_widget.setObjectName(u"welcome_widget")
        self.gridLayout = QGridLayout(self.welcome_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.continue_button = QPushButton(self.welcome_widget)
        self.continue_button.setObjectName(u"continue_button")

        self.gridLayout_2.addWidget(self.continue_button, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.gridLayout.addLayout(self.gridLayout_2, 3, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.welcome_title = QLabel(self.welcome_widget)
        self.welcome_title.setObjectName(u"welcome_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome_title.sizePolicy().hasHeightForWidth())
        self.welcome_title.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.welcome_title, 1, 1, 1, 1)

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
        welcome_screen.setCentralWidget(self.welcome_widget)
        self.statusbar = QStatusBar(welcome_screen)
        self.statusbar.setObjectName(u"statusbar")
        welcome_screen.setStatusBar(self.statusbar)

        self.retranslateUi(welcome_screen)

        QMetaObject.connectSlotsByName(welcome_screen)
    # setupUi

    def retranslateUi(self, welcome_screen):
        welcome_screen.setWindowTitle(QCoreApplication.translate("welcome_screen", u"Stat Tracker", None))
        self.continue_button.setText(QCoreApplication.translate("welcome_screen", u"Continue", None))
        self.welcome_title.setText(QCoreApplication.translate("welcome_screen", u"<html><head/><body><p align=\"center\">Welcome to Stat Tracker</p></body></html>", None))
    # retranslateUi


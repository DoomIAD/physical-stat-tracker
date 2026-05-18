# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'name_setup.ui'
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
    QSizePolicy, QSpacerItem, QStatusBar, QTextEdit,
    QWidget)

class Ui_name_screen(object):
    def setupUi(self, name_screen):
        if not name_screen.objectName():
            name_screen.setObjectName(u"name_screen")
        name_screen.resize(675, 501)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AddressBookNew))
        name_screen.setWindowIcon(icon)
        self.name_widget = QWidget(name_screen)
        self.name_widget.setObjectName(u"name_widget")
        self.gridLayout = QGridLayout(self.name_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.name_textedit = QTextEdit(self.name_widget)
        self.name_textedit.setObjectName(u"name_textedit")

        self.gridLayout_2.addWidget(self.name_textedit, 0, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 5)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.gridLayout.addLayout(self.gridLayout_2, 3, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.name_title = QLabel(self.name_widget)
        self.name_title.setObjectName(u"name_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_title.sizePolicy().hasHeightForWidth())
        self.name_title.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.name_title, 1, 1, 1, 1)

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
        name_screen.setCentralWidget(self.name_widget)
        self.statusbar = QStatusBar(name_screen)
        self.statusbar.setObjectName(u"statusbar")
        name_screen.setStatusBar(self.statusbar)

        self.retranslateUi(name_screen)

        QMetaObject.connectSlotsByName(name_screen)
    # setupUi

    def retranslateUi(self, name_screen):
        name_screen.setWindowTitle(QCoreApplication.translate("name_screen", u"Stat Tracker", None))
        self.name_title.setText(QCoreApplication.translate("name_screen", u"<html><head/><body><p align=\"center\">What's your name?</p></body></html>", None))
    # retranslateUi


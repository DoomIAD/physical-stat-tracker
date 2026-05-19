# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome_widget.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_welcome_screen(object):
    def setupUi(self, welcome_screen):
        if not welcome_screen.objectName():
            welcome_screen.setObjectName(u"welcome_screen")
        welcome_screen.resize(784, 677)
        self.gridLayout = QGridLayout(welcome_screen)
        self.gridLayout.setObjectName(u"gridLayout")
        self.centerLayout = QVBoxLayout()
        self.centerLayout.setObjectName(u"centerLayout")
        self.welcome_title = QLabel(welcome_screen)
        self.welcome_title.setObjectName(u"welcome_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome_title.sizePolicy().hasHeightForWidth())
        self.welcome_title.setSizePolicy(sizePolicy)
        self.welcome_title.setScaledContents(False)
        self.welcome_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcome_title.setWordWrap(False)

        self.centerLayout.addWidget(self.welcome_title)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.centerLayout.addItem(self.verticalSpacer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.continue_button = QPushButton(welcome_screen)
        self.continue_button.setObjectName(u"continue_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.continue_button.sizePolicy().hasHeightForWidth())
        self.continue_button.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.continue_button, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

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

        self.retranslateUi(welcome_screen)

        QMetaObject.connectSlotsByName(welcome_screen)
    # setupUi

    def retranslateUi(self, welcome_screen):
        welcome_screen.setWindowTitle(QCoreApplication.translate("welcome_screen", u"Stat Tracker", None))
        self.welcome_title.setText(QCoreApplication.translate("welcome_screen", u"Welcome to Stat Tracker", None))
        self.continue_button.setText(QCoreApplication.translate("welcome_screen", u"Continue", None))
    # retranslateUi


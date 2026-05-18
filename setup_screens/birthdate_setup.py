# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'birthdate_setup.ui'
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
    QLabel, QMainWindow, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)

class Ui_birthdate_screen(object):
    def setupUi(self, birthdate_screen):
        if not birthdate_screen.objectName():
            birthdate_screen.setObjectName(u"birthdate_screen")
        birthdate_screen.resize(686, 480)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AddressBookNew))
        birthdate_screen.setWindowIcon(icon)
        self.birthdate_widget = QWidget(birthdate_screen)
        self.birthdate_widget.setObjectName(u"birthdate_widget")
        self.gridLayout = QGridLayout(self.birthdate_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.birthdate_dateedit = QDateEdit(self.birthdate_widget)
        self.birthdate_dateedit.setObjectName(u"birthdate_dateedit")
        self.birthdate_dateedit.setFrame(False)
        self.birthdate_dateedit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.birthdate_dateedit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.birthdate_dateedit.setProperty(u"showGroupSeparator", True)
        self.birthdate_dateedit.setMaximumDate(QDate(2030, 12, 31))
        self.birthdate_dateedit.setMinimumDate(QDate(1900, 9, 14))
        self.birthdate_dateedit.setCalendarPopup(False)
        self.birthdate_dateedit.setDate(QDate(2020, 7, 4))

        self.gridLayout_2.addWidget(self.birthdate_dateedit, 0, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 4)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.gridLayout.addLayout(self.gridLayout_2, 3, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.birthdate_title = QLabel(self.birthdate_widget)
        self.birthdate_title.setObjectName(u"birthdate_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.birthdate_title.sizePolicy().hasHeightForWidth())
        self.birthdate_title.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.birthdate_title, 1, 1, 1, 1)

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
        birthdate_screen.setCentralWidget(self.birthdate_widget)
        self.statusbar = QStatusBar(birthdate_screen)
        self.statusbar.setObjectName(u"statusbar")
        birthdate_screen.setStatusBar(self.statusbar)

        self.retranslateUi(birthdate_screen)

        QMetaObject.connectSlotsByName(birthdate_screen)
    # setupUi

    def retranslateUi(self, birthdate_screen):
        birthdate_screen.setWindowTitle(QCoreApplication.translate("birthdate_screen", u"Stat Tracker", None))
#if QT_CONFIG(tooltip)
        self.birthdate_dateedit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.birthdate_dateedit.setSpecialValueText("")
        self.birthdate_dateedit.setDisplayFormat(QCoreApplication.translate("birthdate_screen", u"MM/dd/yyyy", None))
        self.birthdate_title.setText(QCoreApplication.translate("birthdate_screen", u"<html><head/><body><p align=\"center\">When's your Birthday?</p></body></html>", None))
    # retranslateUi


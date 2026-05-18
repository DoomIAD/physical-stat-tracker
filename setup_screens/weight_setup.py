# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weight_setup.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QSizePolicy, QSpacerItem, QStatusBar,
    QTextEdit, QWidget)

class Ui_weight_screen(object):
    def setupUi(self, weight_screen):
        if not weight_screen.objectName():
            weight_screen.setObjectName(u"weight_screen")
        weight_screen.resize(686, 480)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AddressBookNew))
        weight_screen.setWindowIcon(icon)
        self.weight_widget = QWidget(weight_screen)
        self.weight_widget.setObjectName(u"weight_widget")
        self.gridLayout = QGridLayout(self.weight_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.weight_textedit = QTextEdit(self.weight_widget)
        self.weight_textedit.setObjectName(u"weight_textedit")
        self.weight_textedit.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.weight_textedit.setFrameShape(QFrame.Shape.StyledPanel)
        self.weight_textedit.setFrameShadow(QFrame.Shadow.Sunken)
        self.weight_textedit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.weight_textedit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.weight_textedit.setUndoRedoEnabled(False)
        self.weight_textedit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.weight_textedit.setOverwriteMode(True)
        self.weight_textedit.setAcceptRichText(False)
        self.weight_textedit.setPlaceholderText(u"170")

        self.gridLayout_2.addWidget(self.weight_textedit, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.weight_label = QLabel(self.weight_widget)
        self.weight_label.setObjectName(u"weight_label")

        self.gridLayout_2.addWidget(self.weight_label, 0, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 4)
        self.gridLayout_2.setColumnStretch(3, 1)

        self.gridLayout.addLayout(self.gridLayout_2, 3, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.weight_title = QLabel(self.weight_widget)
        self.weight_title.setObjectName(u"weight_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weight_title.sizePolicy().hasHeightForWidth())
        self.weight_title.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.weight_title, 1, 1, 1, 1)

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
        weight_screen.setCentralWidget(self.weight_widget)
        self.statusbar = QStatusBar(weight_screen)
        self.statusbar.setObjectName(u"statusbar")
        weight_screen.setStatusBar(self.statusbar)

        self.retranslateUi(weight_screen)

        QMetaObject.connectSlotsByName(weight_screen)
    # setupUi

    def retranslateUi(self, weight_screen):
        weight_screen.setWindowTitle(QCoreApplication.translate("weight_screen", u"Stat Tracker", None))
        self.weight_label.setText(QCoreApplication.translate("weight_screen", u"lb", None))
        self.weight_title.setText(QCoreApplication.translate("weight_screen", u"<html><head/><body><p align=\"center\">How Much do you Weigh?</p></body></html>", None))
    # retranslateUi


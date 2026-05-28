# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weight_manager_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_weight_manager_widget(object):
    def setupUi(self, weight_manager_widget):
        if not weight_manager_widget.objectName():
            weight_manager_widget.setObjectName(u"weight_manager_widget")
        weight_manager_widget.resize(680, 370)
        self.gridLayout = QGridLayout(weight_manager_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)

        self.retranslateUi(weight_manager_widget)

        QMetaObject.connectSlotsByName(weight_manager_widget)
    # setupUi

    def retranslateUi(self, weight_manager_widget):
        weight_manager_widget.setWindowTitle(QCoreApplication.translate("weight_manager_widget", u"Stat Tracker", None))
    # retranslateUi


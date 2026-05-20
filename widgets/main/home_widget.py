# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from widgets.main.weight_chart import WeightChartWidget
from widgets.main.activity_chart import ActivityChartWidget

class Ui_debug_widget(object):
    def setupUi(self, debug_widget):
        if not debug_widget.objectName():
            debug_widget.setObjectName(u"debug_widget")
        debug_widget.resize(696, 177)
        self.gridLayout = QGridLayout(debug_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.centerLayout = QVBoxLayout()
        self.centerLayout.setObjectName(u"centerLayout")
        self.centerLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.centerLayout.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, 5)
        self.top_Layout = QHBoxLayout()
        self.top_Layout.setSpacing(20)
        self.top_Layout.setObjectName(u"top_Layout")
        self.top_Layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.sidebar_pushButton = QPushButton(debug_widget)
        self.sidebar_pushButton.setObjectName(u"sidebar_pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_pushButton.sizePolicy().hasHeightForWidth())
        self.sidebar_pushButton.setSizePolicy(sizePolicy)

        self.top_Layout.addWidget(self.sidebar_pushButton)

        self.title_label = QLabel(debug_widget)
        self.title_label.setObjectName(u"title_label")
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)

        self.top_Layout.addWidget(self.title_label)

        self.profile_pushButton = QPushButton(debug_widget)
        self.profile_pushButton.setObjectName(u"profile_pushButton")
        sizePolicy.setHeightForWidth(self.profile_pushButton.sizePolicy().hasHeightForWidth())
        self.profile_pushButton.setSizePolicy(sizePolicy)

        self.top_Layout.addWidget(self.profile_pushButton)

        self.top_Layout.setStretch(0, 1)
        self.top_Layout.setStretch(1, 6)
        self.top_Layout.setStretch(2, 1)

        self.verticalLayout.addLayout(self.top_Layout)

        self.graph_Layout = QHBoxLayout()
        self.graph_Layout.setSpacing(5)
        self.graph_Layout.setObjectName(u"graph_Layout")
        
        self.weightchart_widget = WeightChartWidget(debug_widget)
        self.weightchart_widget.setObjectName(u"weightchart_widget")

        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.weightchart_widget.sizePolicy().hasHeightForWidth())
        self.weightchart_widget.setSizePolicy(sizePolicy1)

        self.graph_Layout.addWidget(self.weightchart_widget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.today_label = QLabel(debug_widget)
        self.today_label.setObjectName(u"today_label")
        sizePolicy.setHeightForWidth(self.today_label.sizePolicy().hasHeightForWidth())
        self.today_label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.today_label)

        self.workout_label = QLabel(debug_widget)
        self.workout_label.setObjectName(u"workout_label")
        sizePolicy.setHeightForWidth(self.workout_label.sizePolicy().hasHeightForWidth())
        self.workout_label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.workout_label)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)

        self.graph_Layout.addLayout(self.verticalLayout_2)

        self.graph_Layout.setStretch(0, 3)
        self.graph_Layout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.graph_Layout)

        self.stats_Layout = QHBoxLayout()
        self.stats_Layout.setSpacing(12)
        self.stats_Layout.setObjectName(u"stats_Layout")
        self.stats_Layout.setContentsMargins(5, -1, 5, -1)
        self.bmi_label = QLabel(debug_widget)
        self.bmi_label.setObjectName(u"bmi_label")

        self.stats_Layout.addWidget(self.bmi_label)

        self.fat_label = QLabel(debug_widget)
        self.fat_label.setObjectName(u"fat_label")

        self.stats_Layout.addWidget(self.fat_label)

        self.percentile_label = QLabel(debug_widget)
        self.percentile_label.setObjectName(u"percentile_label")

        self.stats_Layout.addWidget(self.percentile_label)

        self.stats_Layout.setStretch(0, 1)
        self.stats_Layout.setStretch(1, 1)
        self.stats_Layout.setStretch(2, 1)

        self.verticalLayout.addLayout(self.stats_Layout)

        self.activity_widget = ActivityChartWidget(debug_widget)
        self.activity_widget.setObjectName(u"activity_widget")

        self.verticalLayout.addWidget(self.activity_widget)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 4)

        self.centerLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.centerLayout, 1, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)

        self.retranslateUi(debug_widget)

        QMetaObject.connectSlotsByName(debug_widget)
    # setupUi

    def retranslateUi(self, debug_widget):
        debug_widget.setWindowTitle(QCoreApplication.translate("debug_widget", u"Stat Tracker", None))
        self.sidebar_pushButton.setText(QCoreApplication.translate("debug_widget", u"side_bar", None))
        self.title_label.setText(QCoreApplication.translate("debug_widget", u"Hey There <user>", None))
        self.profile_pushButton.setText(QCoreApplication.translate("debug_widget", u"Profile", None))
        self.today_label.setText(QCoreApplication.translate("debug_widget", u"Today's Workout", None))
        self.workout_label.setText(QCoreApplication.translate("debug_widget", u"<todays_workout>", None))
        self.bmi_label.setText(QCoreApplication.translate("debug_widget", u"<bmi>", None))
        self.fat_label.setText(QCoreApplication.translate("debug_widget", u"<fat_percent>", None))
        self.percentile_label.setText(QCoreApplication.translate("debug_widget", u"<fitness_percentile>", None))
    # retranslateUi


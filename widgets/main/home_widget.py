# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from datetime import date
import math

from sql.queries.read_database import *

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

        self.debug_widget = debug_widget
        self.debug_widget.showEvent = self.on_show_event

    def on_show_event(self, event):
        self.update_label()
        super().showEvent(event)  # Ensure base class behavior is preserved

    def update_label(self):
        # Get user data
        print("Updating labels with user data...")
        global name
        name = get_all_user_names()[0]
        user_data = get_user_by_name(name)

        # Extract user data
        global height_ft, height_in, birthdate, gender, neck_circumference, waist_circumference
        height_ft = user_data[1] 
        height_in = user_data[2]
        birthdate = user_data[3]   
        gender = user_data[4]
        neck_circumference = user_data[5]
        waist_circumference = user_data[6]
        current_weight = get_current_weight(name)
        weight_history= get_weight_history(name)

        def update_name():
            self.title_label.setText(f"Hey There {name}")

        def update_bmi():
            bmi = self.calculate_bmi(current_weight, height_ft, height_in)
            self.bmi_label.setText(f"{bmi:.1f} BMI")

        def update_body_fat():
            if neck_circumference is not None and waist_circumference is not None:
                body_fat = self.calculate_body_fat(gender, neck_circumference, waist_circumference)
                self.fat_label.setText(f"{body_fat:.1f}% Body Fat")
            else:
                self.fat_label.setText("loading...")

        def update_fitness_percentile():
            # Placeholder for fitness percentile calculation
            self.percentile_label.setText("loading....")

        def update_workout():
            today = date.today()
            workout_plan = self.get_todays_workout(today)
            if workout_plan is not None:
                self.workout_label.setText(f"Today's Workout: {workout_plan}")
            else:
                self.workout_label.setText(f"Today's Workout: No workout planned")
        
        update_name()
        update_bmi()
        update_body_fat()
        update_fitness_percentile()
        update_workout()
        self.update_weight_graph(name)
        self.update_activity_graph()

    def update_weight_graph(self, name):
        weight_history = get_weight_history(name)

        series = self.weightchart_widget.series
        series.clear()

        if not weight_history:
            return

        weights = []

        for index, (date, weight) in enumerate(weight_history):
            series.append(index, float(weight))
            weights.append(float(weight))

        chart = self.weightchart_widget.chart
        axis_x = self.weightchart_widget.axis_x
        axis_y = self.weightchart_widget.axis_y

        axis_x.setRange(0, len(weight_history) - 1)

        min_weight = min(weights)
        max_weight = max(weights)
        padding = 5

        axis_y.setRange(min_weight - padding, max_weight + padding)
        
    def update_activity_graph(self):
        # Need to update to match self.activity_widget to match activity history data
        pass

    def calculate_bmi(self, weight_lbs, height_ft, height_in):
        total_height_in = (height_ft * 12) + height_in
        bmi = (weight_lbs / (total_height_in ** 2)) * 703
        return round(bmi, 2)

    def calculate_body_fat(self, gender, neck, waist):
        if gender is None or neck is None or waist is None:
            return {"Missing data for body fat calculation"}
        else:
            if gender.lower() == 'male':
                body_fat = 86.010 * math.log10(waist - neck) - 70.041 * math.log10(69) + 36.76
            else:
                body_fat = 163.205 * math.log10(waist - neck) - 97.684 * math.log10(64) - 78.387
            return round(body_fat, 2)

    def get_todays_workout(self, today):
        if today is None:
            return "loading..."
        else:
            # Fetch all workout_week entries
            workout_week_data = get_all_workout_week()
            for entry in workout_week_data:
                # Assuming entry[1] is the date and entry[2] is the workout plan name
                if entry[1] == today:
                    return entry[2]
            return None

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


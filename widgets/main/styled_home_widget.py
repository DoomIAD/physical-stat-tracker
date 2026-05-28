# -*- coding: utf-8 -*-

from datetime import date
import math

from sql.queries.read_database import *

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication, QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QVBoxLayout, QWidget
)

from widgets.main.weight_chart import WeightChartWidget
from widgets.main.activity_chart import ActivityChartWidget


class Ui_debug_widget(object):
    def setupUi(self, debug_widget):
        if not debug_widget.objectName():
            debug_widget.setObjectName(u"debug_widget")

        debug_widget.resize(1100, 700)

        # Root: copied from the weight dashboard pattern only for the left nav.
        # The original home content remains in the main content area.
        self.rootLayout = QHBoxLayout(debug_widget)
        self.rootLayout.setObjectName(u"rootLayout")
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setSpacing(0)

        # =========================== Left Navigation =========================== #
        self.sidebar_frame = QFrame(debug_widget)
        self.sidebar_frame.setObjectName(u"sidebar")
        self.sidebar_frame.setFixedWidth(260)

        self.sidebarLayout = QVBoxLayout(self.sidebar_frame)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.sidebarLayout.setContentsMargins(24, 32, 24, 24)
        self.sidebarLayout.setSpacing(18)

        self.logo_label = QLabel(u"⚖  Stat Tracker", self.sidebar_frame)
        self.logo_label.setObjectName(u"logo")
        self.sidebarLayout.addWidget(self.logo_label)

        self.overview_nav = QPushButton(u"⌂  Overview", self.sidebar_frame)
        self.overview_nav.setObjectName(u"navActive")
        self.overview_nav.setCursor(Qt.PointingHandCursor)

        self.weight_nav = QPushButton(u"⌁  Weight", self.sidebar_frame)
        self.weight_nav.setObjectName(u"nav")
        self.weight_nav.setCursor(Qt.PointingHandCursor)

        self.goals_nav = QPushButton(u"◎  Goals", self.sidebar_frame)
        self.goals_nav.setObjectName(u"nav")
        self.goals_nav.setCursor(Qt.PointingHandCursor)

        self.insights_nav = QPushButton(u"▥  Insights", self.sidebar_frame)
        self.insights_nav.setObjectName(u"nav")
        self.insights_nav.setCursor(Qt.PointingHandCursor)

        self.settings_nav = QPushButton(u"⚙  Settings", self.sidebar_frame)
        self.settings_nav.setObjectName(u"nav")
        self.settings_nav.setCursor(Qt.PointingHandCursor)

        for button in (
            self.overview_nav,
            self.weight_nav,
            self.goals_nav,
            self.insights_nav,
            self.settings_nav,
        ):
            button.setFlat(True)
            button.setMinimumHeight(44)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            self.sidebarLayout.addWidget(button)

        self.sidebarLayout.addStretch()

        self.note_label = QLabel(
            u"✦\n\nYou've got this!\nConsistency today creates\nresults tomorrow.",
            self.sidebar_frame,
        )
        self.note_label.setObjectName(u"note")
        self.note_label.setWordWrap(True)
        self.sidebarLayout.addWidget(self.note_label)

        self.profile_pushButton = QPushButton(u"U    Profile                         ˅", self.sidebar_frame)
        self.profile_pushButton.setObjectName(u"user")
        self.profile_pushButton.setFlat(True)
        self.profile_pushButton.setCursor(Qt.PointingHandCursor)
        self.sidebarLayout.addWidget(self.profile_pushButton)

        self.rootLayout.addWidget(self.sidebar_frame)

        # =========================== Original Home Content =========================== #
        self.main_frame = QFrame(debug_widget)
        self.main_frame.setObjectName(u"main")
        self.gridLayout = QGridLayout(self.main_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(36, 32, 36, 32)
        self.gridLayout.setSpacing(0)

        self.centerLayout = QVBoxLayout()
        self.centerLayout.setObjectName(u"centerLayout")
        self.centerLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.centerLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(22)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        # Header: original title retained, sidebar/profile button removed from top.
        self.top_Layout = QHBoxLayout()
        self.top_Layout.setSpacing(20)
        self.top_Layout.setObjectName(u"top_Layout")

        self.title_label = QLabel(debug_widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.top_Layout.addWidget(self.title_label)

        self.verticalLayout.addLayout(self.top_Layout)

        self.graph_Layout = QHBoxLayout()
        self.graph_Layout.setSpacing(22)
        self.graph_Layout.setObjectName(u"graph_Layout")

        self.weightchart_card = QFrame(debug_widget)
        self.weightchart_card.setObjectName(u"card")
        self.weightchart_card_layout = QVBoxLayout(self.weightchart_card)
        self.weightchart_card_layout.setContentsMargins(22, 22, 22, 22)

        self.weightchart_title = QLabel(u"Weight History", self.weightchart_card)
        self.weightchart_title.setObjectName(u"sectionTitle")
        self.weightchart_card_layout.addWidget(self.weightchart_title)

        self.weightchart_widget = WeightChartWidget(self.weightchart_card)
        self.weightchart_widget.setObjectName(u"weightchart_widget")
        self.weightchart_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.weightchart_card_layout.addWidget(self.weightchart_widget)

        self.graph_Layout.addWidget(self.weightchart_card)

        self.side_cards_layout = QVBoxLayout()
        self.side_cards_layout.setSpacing(22)
        self.side_cards_layout.setObjectName(u"side_cards_layout")

        self.today_card = QFrame(debug_widget)
        self.today_card.setObjectName(u"card")
        self.today_card_layout = QVBoxLayout(self.today_card)
        self.today_card_layout.setContentsMargins(22, 22, 22, 22)
        self.today_card_layout.setSpacing(12)

        self.today_label = QLabel(debug_widget)
        self.today_label.setObjectName(u"sectionTitle")
        self.today_card_layout.addWidget(self.today_label)

        self.workout_label = QLabel(debug_widget)
        self.workout_label.setObjectName(u"bodyText")
        self.workout_label.setWordWrap(True)
        self.today_card_layout.addWidget(self.workout_label)
        self.today_card_layout.addStretch()

        self.side_cards_layout.addWidget(self.today_card)
        self.side_cards_layout.addStretch()

        self.graph_Layout.addLayout(self.side_cards_layout)
        self.graph_Layout.setStretch(0, 3)
        self.graph_Layout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.graph_Layout)

        self.stats_Layout = QHBoxLayout()
        self.stats_Layout.setSpacing(22)
        self.stats_Layout.setObjectName(u"stats_Layout")
        self.stats_Layout.setContentsMargins(0, 0, 0, 0)

        self.bmi_label = QLabel(debug_widget)
        self.bmi_label.setObjectName(u"metricCard")
        self.fat_label = QLabel(debug_widget)
        self.fat_label.setObjectName(u"metricCard")
        self.percentile_label = QLabel(debug_widget)
        self.percentile_label.setObjectName(u"metricCard")

        self.stats_Layout.addWidget(self.bmi_label)
        self.stats_Layout.addWidget(self.fat_label)
        self.stats_Layout.addWidget(self.percentile_label)

        self.verticalLayout.addLayout(self.stats_Layout)

        self.activity_card = QFrame(debug_widget)
        self.activity_card.setObjectName(u"card")
        self.activity_card_layout = QVBoxLayout(self.activity_card)
        self.activity_card_layout.setContentsMargins(22, 22, 22, 22)

        self.activity_title = QLabel(u"Activity", self.activity_card)
        self.activity_title.setObjectName(u"sectionTitle")
        self.activity_card_layout.addWidget(self.activity_title)

        self.activity_widget = ActivityChartWidget(self.activity_card)
        self.activity_widget.setObjectName(u"activity_widget")
        self.activity_card_layout.addWidget(self.activity_widget)

        self.verticalLayout.addWidget(self.activity_card)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 3)

        self.centerLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.centerLayout, 0, 0, 1, 1)

        self.rootLayout.addWidget(self.main_frame)

        self.retranslateUi(debug_widget)
        self.apply_styles(debug_widget)

        QMetaObject.connectSlotsByName(debug_widget)

        self.debug_widget = debug_widget
        self.original_show_event = debug_widget.showEvent
        self.debug_widget.showEvent = self.on_show_event

    def apply_styles(self, debug_widget):
        debug_widget.setStyleSheet("""
            QWidget {
                font-family: Arial;
                color: #111827;
                background: #F8FAFC;
            }

            #sidebar {
                background: #F3F6FB;
                border-right: 1px solid #E5E7EB;
            }

            #main {
                background: #F8FAFC;
            }

            #logo {
                font-size: 20px;
                font-weight: 700;
                color: #111827;
                padding-bottom: 24px;
            }

            #nav, #navActive {
                font-size: 16px;
                text-align: left;
                padding: 10px 14px;
                border-radius: 10px;
                border: none;
            }

            #nav {
                color: #4B5563;
                background: transparent;
            }

            #nav:hover {
                background: #EEF2F7;
            }

            #navActive {
                color: #2563EB;
                background: #E8F0FF;
                font-weight: 700;
            }

            #note {
                background: #EEF2FF;
                color: #6D5DD3;
                border-radius: 14px;
                padding: 18px;
                font-size: 14px;
                line-height: 1.4;
            }

            #user {
                background: transparent;
                color: #4B5563;
                font-size: 15px;
                text-align: left;
                border: none;
                padding: 10px 0;
            }

            #title_label {
                font-size: 30px;
                font-weight: 800;
                color: #111827;
                padding-bottom: 4px;
            }

            #card {
                background: #FFFFFF;
                border: 1px solid #E5E7EB;
                border-radius: 14px;
            }

            #sectionTitle {
                font-size: 18px;
                font-weight: 700;
                color: #111827;
                background: transparent;
            }

            #bodyText {
                font-size: 15px;
                color: #4B5563;
                background: transparent;
            }

            #metricCard {
                background: #FFFFFF;
                border: 1px solid #E5E7EB;
                border-radius: 14px;
                padding: 18px;
                font-size: 18px;
                font-weight: 700;
                color: #111827;
            }
        """)


    def _refresh_nav_button_style(self, button):
        button.style().unpolish(button)
        button.style().polish(button)
        button.update()

    def set_active_nav(self, active_button):
        for button in (
            self.overview_nav,
            self.weight_nav,
            self.goals_nav,
            self.insights_nav,
            self.settings_nav,
        ):
            button.setObjectName(u"navActive" if button is active_button else u"nav")
            self._refresh_nav_button_style(button)

    def connect_navigation(
        self,
        stack,
        home_widget=None,
        weight_widget=None,
        goals_widget=None,
        insights_widget=None,
        settings_widget=None,
    ):
        """Connect the left navigation bar to a QStackedWidget.

        Pass only the screens that currently exist. Missing screens are disabled
        so users cannot click into pages that have not been built yet.
        """
        home_widget = home_widget or self.debug_widget

        nav_targets = {
            self.overview_nav: home_widget,
            self.weight_nav: weight_widget,
            self.goals_nav: goals_widget,
            self.insights_nav: insights_widget,
            self.settings_nav: settings_widget,
        }

        for button, target_widget in nav_targets.items():
            if target_widget is None:
                button.setEnabled(False)
                continue

            button.setEnabled(True)
            button.clicked.connect(
                lambda checked=False, btn=button, target=target_widget: self._navigate_to(
                    stack, btn, target
                )
            )

    def _navigate_to(self, stack, active_button, target_widget):
        stack.setCurrentWidget(target_widget)
        self.set_active_nav(active_button)

    # Overide to run update_label() every time widget is shown
    def on_show_event(self, event):
        self.set_active_nav(self.overview_nav)
        self.update_label()
        self.original_show_event(event)

    # Function to update all labels with user data from database
    def update_label(self):
        # Get user data
        print("Updating labels with user data...")
        users = get_all_user_names()
        if not users:
            return
        name = users[0]
        user_data = get_user_by_name(name)

        # Extract user data into usable variables
        height_ft = user_data[1] 
        height_in = user_data[2]
        birthdate = user_data[3]   
        gender = user_data[4]
        neck_circumference = user_data[5]
        waist_circumference = user_data[6]
        current_weight = get_current_weight(name)
        weight_history= get_weight_history(name)

        # Updates name label with user's name
        def update_name():
            self.title_label.setText(f"Hey There {name}")

        # Updates BMI label with calculated BMI from user data
        def update_bmi():
            bmi = self.calculate_bmi(current_weight, height_ft, height_in)
            if bmi is None:
                self.bmi_label.setText("No BMI data")
            else:
                self.bmi_label.setText(f"{bmi:.1f} BMI")

        # Updates body fat label with calculated body fat percentage from user data
        # Requires neck and waist circumference to be filled out
        def update_body_fat():
            if neck_circumference is not None and waist_circumference is not None:
                body_fat = self.calculate_body_fat(gender, neck_circumference, waist_circumference)
                self.fat_label.setText(f"{body_fat:.1f}% Body Fat")
            else:
                self.fat_label.setText("Missing data for body fat calculation")

        # Need to find API or table to find fitness percentiles
        def update_fitness_percentile():
            # hardcoded in the meantime
            self.percentile_label.setText("No Information for Fitness Percentile")

        # Updates today's workout label with workout plan from database that matches current day of the week, if it exists
        def update_workout():
            workout_plan = self.get_todays_workout(name)
            
            if workout_plan is not None:
                self.workout_label.setText(workout_plan)
            else:
                self.workout_label.setText("No workout planned")
        
        # Calls all update functions to update labels with user data from database
        update_name()
        update_bmi()
        update_body_fat()
        update_fitness_percentile()
        update_workout()

        # Function are defined within their own scope
        self.update_weight_graph(name)
        self.update_activity_graph(name)

    # Creates a line graph of user's weight history using data from database
    def update_weight_graph(self, name):
        weight_history = get_weight_history(name)

        series = self.weightchart_widget.series
        series.clear()

        if not weight_history:
            return

        weights = []

        for index, (date, weight) in enumerate(weight_history):
            weight = float(weight)
            series.append(index, weight)
            weights.append(weight)

        axis_x = self.weightchart_widget.axis_x
        axis_y = self.weightchart_widget.axis_y

        axis_x.setRange(0, len(weight_history) - 1)

        min_weight = min(weights)
        max_weight = max(weights)
        padding = 2

        axis_y.setRange(min_weight - padding, max_weight + padding)
    
    # Creates a GitHub like activity graph to show amount of time user spent exercising each day
    def update_activity_graph(self, name):
        self.activity_widget.load_activity_data(name)
    
    # BMI calculation
    def calculate_bmi(self, weight_lbs, height_ft, height_in):
        if weight_lbs is None or height_ft is None or height_in is None:
            return None
        try:
            total_height_in = (float(height_ft) * 12) + float(height_in)
            weight_lbs = float(weight_lbs)
        except (TypeError, ValueError):
            return None
        if total_height_in <= 0:
            return None
        bmi = (weight_lbs / (total_height_in ** 2)) * 703
        return round(bmi, 2)

    # Body fat calculation using U.S. Navy Method, requires neck and waist circumference
    def calculate_body_fat(self, gender, neck, waist):
        if gender is None or neck is None or waist is None:
            return {"Missing data for body fat calculation"}
        else:
            if gender.lower() == 'male':
                body_fat = 86.010 * math.log10(waist - neck) - 70.041 * math.log10(69) + 36.76
            else:
                body_fat = 163.205 * math.log10(waist - neck) - 97.684 * math.log10(64) - 78.387
            return round(body_fat, 2)

    # Finds the workout plan for the current day of the week
    def get_todays_workout(self, username):
        from sql.queries.read_database import get_user_workout_plan_for_day
        return get_user_workout_plan_for_day(username)

    def retranslateUi(self, debug_widget):
        debug_widget.setWindowTitle(QCoreApplication.translate("debug_widget", u"Stat Tracker", None))
        self.title_label.setText(QCoreApplication.translate("debug_widget", u"Hey There <user>", None))
        self.today_label.setText(QCoreApplication.translate("debug_widget", u"Today's Workout", None))
        self.workout_label.setText(QCoreApplication.translate("debug_widget", u"<todays_workout>", None))
        self.bmi_label.setText(QCoreApplication.translate("debug_widget", u"<bmi>", None))
        self.fat_label.setText(QCoreApplication.translate("debug_widget", u"<fat_percent>", None))
        self.percentile_label.setText(QCoreApplication.translate("debug_widget", u"<fitness_percentile>", None))
    # retranslateUi
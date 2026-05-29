# weight_dashboard.py
import datetime
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QPainter, QPen
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QFrame, QGridLayout, QLineEdit, QSizePolicy, QDialog, QDialogButtonBox
)

from sql.queries.edit_database import update_user
from sql.queries.insert_database import insert_weight
from widgets.weight.goal_dialog import GoalDialog
from widgets.weight.weight_graph_widget import WeightChart
from widgets.navigation.navigation_bar_widget import NavigationBar
from sql.queries.read_database import get_all_user_names, get_weight_history, get_goal_data


class Card(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("card")
        self.setFrameShape(QFrame.NoFrame)


class Donut(QWidget):
    def __init__(self, progress=64):
        super().__init__()
        self.progress = progress
        self.setMinimumSize(120, 120)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        rect = self.rect().adjusted(15, 15, -15, -15)

        p.setPen(QPen(QColor("#E5E7EB"), 8))
        p.drawArc(rect, 0, 360 * 16)

        p.setPen(QPen(QColor("#34A853"), 8, Qt.SolidLine, Qt.RoundCap))
        p.drawArc(rect, 90 * 16, int(-360 * self.progress / 100) * 16)

        p.setPen(QColor("#111827"))
        p.setFont(QFont("Arial", 18, QFont.Bold))
        p.drawText(rect, Qt.AlignCenter, f"{self.progress}%")

        p.setFont(QFont("Arial", 9))
        p.setPen(QColor("#6B7280"))
        p.drawText(rect.adjusted(0, 30, 0, 0), Qt.AlignCenter, "Progress")

class Dashboard(QWidget):
    def __init__(self):

        # gets username of active user
        users = get_all_user_names()
        if not users:
            return
        name = users[0]

        # Gets basic weight related details
        weight_history=get_weight_history(name)
        temp_date, self.current_weight = weight_history[-1]
        # Sets yesterday's weight to today's if no data for yesterday
        if len(weight_history)>1:
            temp_date,yesterdays_weight=weight_history[-2]
            changed_weight=self.current_weight-yesterdays_weight
        else:
            yesterdays_weight = self.current_weight
            changed_weight=0
        
        # Uses goal data if existing in DB, else use 150lb default
        goal_data = get_goal_data(name)
        if goal_data is None:
            self.goal_weight = 150
            self.start_weight = 150
        else:
            self.goal_weight, self.start_weight = goal_data

        super().__init__()
        self.setWindowTitle("WeightTrack")
        self.resize(1440, 850)

        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # Navigation Bar Called
        self.navigation_bar = NavigationBar(active_page="Weight", parent=self)
        root.addWidget(self.navigation_bar)

        main = QFrame()
        main.setObjectName("main")
        main_layout = QVBoxLayout(main)
        main_layout.setContentsMargins(36, 36, 36, 36)
        main_layout.setSpacing(28)

        header = QHBoxLayout()
        title_box = QVBoxLayout()
        title = QLabel("Weight Progress")
        title.setObjectName("title")
        subtitle = QLabel("Track your progress and stay on goal.")
        subtitle.setObjectName("subtitle")
        title_box.addWidget(title)
        title_box.addWidget(subtitle)

        date = QLabel(f"📅  {datetime.datetime.today().date()}")
        date.setObjectName("date")

        header.addLayout(title_box)
        header.addStretch()
        header.addWidget(date)
        main_layout.addLayout(header)

        grid = QGridLayout()
        grid.setSpacing(28)

        weight_card = Card()
        wl = QVBoxLayout(weight_card)
        wl.setContentsMargins(28, 24, 28, 24)

        wl.addWidget(QLabel("Enter your weight for today"))

        self.weight_input = QLineEdit()
        self.weight_input.setPlaceholderText("0.0")
        self.weight_input.setObjectName("weightInput")
        self.weight_input.setAlignment(Qt.AlignLeft)
        wl.addWidget(self.weight_input)


        save = QPushButton("Save Weight")
        save.setObjectName("primaryButton")
        save.clicked.connect(lambda: self.save_weight(name))
        wl.addWidget(save)

        goal_card = Card()
        gl = QHBoxLayout(goal_card)
        gl.setContentsMargins(28, 24, 28, 24)

        left_goal = QVBoxLayout()
        left_goal.addWidget(QLabel("Goal Weight"))

        self.goal_value = QLabel(f"{self.goal_weight} lbs")
        self.goal_value.setObjectName("metric")
        left_goal.addWidget(self.goal_value)

        edit = QPushButton("✎  Edit Goal")
        edit.setObjectName("secondaryButton")
        edit.clicked.connect(
            lambda checked=False: self.open_goal_dialog(name)
        )
        left_goal.addWidget(edit)
        left_goal.addStretch()

        donut_box = QVBoxLayout()

        self.donut = Donut(self.calculate_progress())

        donut_box.addWidget(self.donut)

        gl.addLayout(left_goal)
        gl.addLayout(donut_box)

        summary_card = Card()
        sl = QVBoxLayout(summary_card)
        sl.setContentsMargins(28, 24, 28, 24)
        sl.addWidget(QLabel("Summary"))
        sl.addWidget(QLabel(f"↗   Current Weight                         {round(self.current_weight,1)} lbs"))
        sl.addWidget(QLabel(f"↓   Change vs yesterday                  {round(changed_weight,1)} lbs"))
        sl.addStretch()

        grid.addWidget(weight_card, 0, 0)
        grid.addWidget(goal_card, 0, 1)
        grid.addWidget(summary_card, 0, 2)

        main_layout.addLayout(grid)

        chart_card = Card()
        chart_layout = QVBoxLayout(chart_card)
        chart_layout.setContentsMargins(28, 24, 28, 24)

        chart_header = QHBoxLayout()
        chart_title = QLabel("Weight History")
        chart_title.setObjectName("sectionTitle")
        chart_header.addWidget(chart_title)
        chart_header.addStretch()

        chart_layout.addLayout(chart_header)
        self.weight_chart = WeightChart()
        self.weight_chart.goal = self.goal_weight
        chart_layout.addWidget(self.weight_chart)
        self.weight_chart.get_weight_data(name)

        main_layout.addWidget(chart_card)

        root.addWidget(main)

        self._navigation_targets = {}

        self.setStyleSheet("""
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

            #nav:disabled {
                color: #A0AEC0;
                background: transparent;
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

            #title {
                font-size: 30px;
                font-weight: 800;
            }

            #subtitle, #date {
                color: #6B7280;
                font-size: 15px;
            }

            #card {
                background: white;
                border: 1px solid #E5E7EB;
                border-radius: 14px;
            }

            QLabel {
                font-size: 15px;
            }

            #weightInput {
                font-size: 54px;
                border: none;
                background: transparent;
                color: #111827;
            }

            #metric {
                font-size: 36px;
                font-weight: 300;
            }

            #primaryButton {
                background: #2563EB;
                color: white;
                border: none;
                border-radius: 9px;
                padding: 14px;
                font-size: 15px;
                font-weight: 700;
            }

            #secondaryButton {
                background: white;
                color: #2563EB;
                border: 1px solid #E5E7EB;
                border-radius: 9px;
                padding: 12px;
                font-size: 15px;
                font-weight: 600;
            }

            #sectionTitle {
                font-size: 18px;
                font-weight: 700;
            }

            #tabs {
                color: #4B5563;
                background: #F8FAFC;
                border: 1px solid #E5E7EB;
                border-radius: 8px;
                padding: 8px 14px;
            }
                           
        """)


    def calculate_progress(self):
        total_change = self.start_weight - self.goal_weight

        if total_change == 0:
            return 100 if self.current_weight == self.goal_weight else 0

        progress = ((self.start_weight - self.current_weight) / total_change) * 100
        return max(0, min(round(progress, 1), 100))

    def save_weight(self,name):
        weight=self.weight_input.text()
        insert_weight(name, round(float(weight),1), datetime.datetime.now().strftime("%Y-%m-%d"))
        self.current_weight = round(float(weight), 1)
        self.weight_chart.get_weight_data(name)
        self.donut.progress = self.calculate_progress()
        self.donut.update()
        print(f"Saved weight: {weight}")

    def open_goal_dialog(self,name):
        dialog = GoalDialog(self.goal_weight, self)

        if dialog.exec():
            new_goal = dialog.get_goal_weight()
            self.goal_weight = new_goal
            self.goal_value.setText(f"{new_goal} lbs")

            update_user(
                username=name,
                goal=new_goal,
                start_weight=self.current_weight
            )

            self.start_weight = self.current_weight
            self.weight_chart.set_goal(new_goal)

            self.donut.progress = self.calculate_progress()
            self.donut.update()

            print(f"New goal: {new_goal}")

    def showEvent(self, event):
        self.navigation_bar.set_active_nav(self.navigation_bar.weight_nav_button)
        super().showEvent(event)

    def connect_navigation(
        self,
        stack,
        home_widget=None,
        weight_widget=None,
        goals_widget=None,
        insights_widget=None,
        settings_widget=None,
    ):
        self.navigation_bar.connect_navigation(
            stack,
            home_widget,
            weight_widget,
            goals_widget,
            insights_widget,
            settings_widget,
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec())
# weight_dashboard.py
import sys
from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPainter, QPen, QColor, QFont, QPainterPath
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QFrame, QGridLayout, QLineEdit, QSizePolicy
)


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


class WeightChart(QWidget):
    def __init__(self):
        super().__init__()
        self.weights = [
            186, 185, 184.2, 184.1, 183, 182.2, 181, 181.2,
            181.5, 180.5, 178.5, 177.8, 175.5, 174.6, 172.8,
            172.9, 171.2, 171.4, 170, 169.2, 169.3, 168.5, 169.1, 168.4
        ]
        self.goal = 150
        self.setMinimumHeight(340)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        margin_l, margin_t, margin_r, margin_b = 55, 40, 35, 55
        w = self.width() - margin_l - margin_r
        h = self.height() - margin_t - margin_b

        y_min, y_max = 140, 190

        def x_at(i):
            return margin_l + i * w / (len(self.weights) - 1)

        def y_at(value):
            return margin_t + (y_max - value) / (y_max - y_min) * h

        p.setFont(QFont("Arial", 9))
        p.setPen(QColor("#6B7280"))
        for y in range(140, 191, 10):
            py = y_at(y)
            p.drawText(10, py + 4, str(y))
            p.setPen(QPen(QColor("#E5E7EB"), 1, Qt.DashLine))
            p.drawLine(margin_l, py, margin_l + w, py)
            p.setPen(QColor("#6B7280"))

        goal_y = y_at(self.goal)
        p.setPen(QPen(QColor("#34A853"), 2, Qt.DashLine))
        p.drawLine(margin_l, goal_y, margin_l + w, goal_y)
        p.setPen(QColor("#34A853"))
        p.drawText(margin_l + w - 100, goal_y - 10, "Goal: 150.0 lbs")

        path = QPainterPath(QPointF(x_at(0), y_at(self.weights[0])))
        for i, weight in enumerate(self.weights[1:], 1):
            path.lineTo(x_at(i), y_at(weight))

        p.setPen(QPen(QColor("#2563EB"), 2))
        p.drawPath(path)

        p.setBrush(QColor("#FFFFFF"))
        for i, weight in enumerate(self.weights):
            p.drawEllipse(QPointF(x_at(i), y_at(weight)), 3, 3)

        last_x = x_at(len(self.weights) - 1)
        last_y = y_at(self.weights[-1])
        p.setBrush(QColor("#2563EB"))
        p.setPen(Qt.NoPen)
        p.drawRoundedRect(last_x - 3, last_y - 15, 52, 28, 6, 6)
        p.setPen(QColor("#FFFFFF"))
        p.drawText(last_x + 5, last_y + 4, "168.4")

        p.setPen(QColor("#6B7280"))
        labels = ["Feb 22", "Mar 7", "Mar 21", "Apr 4", "Apr 18", "May 2", "May 16", "May 22"]
        for i, label in enumerate(labels):
            x = margin_l + i * w / (len(labels) - 1)
            p.drawText(x - 20, self.height() - 22, label)


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WeightTrack")
        self.resize(1440, 850)

        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # =========================== Left Navigation =========================== #
        sidebar = QFrame(self)
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(260)

        side_layout = QVBoxLayout(sidebar)
        side_layout.setObjectName("sidebarLayout")
        side_layout.setContentsMargins(24, 32, 24, 24)
        side_layout.setSpacing(18)

        logo = QLabel("⚖  Stat Tracker", sidebar)
        logo.setObjectName("logo")
        side_layout.addWidget(logo)

        self.overview_nav_button = QPushButton("⌂  Overview", sidebar)
        self.weight_nav_button = QPushButton("⌁  Weight", sidebar)
        self.goals_nav_button = QPushButton("◎  Goals", sidebar)
        self.insights_nav_button = QPushButton("▥  Insights", sidebar)
        self.settings_nav_button = QPushButton("⚙  Settings", sidebar)

        self.nav_buttons = {
            "Overview": self.overview_nav_button,
            "Weight": self.weight_nav_button,
            "Goals": self.goals_nav_button,
            "Insights": self.insights_nav_button,
            "Settings": self.settings_nav_button
        }

        for button in self.nav_buttons.values():
            button.setCursor(Qt.PointingHandCursor)
            button.setFlat(True)
            button.setMinimumHeight(44)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            button.setObjectName("nav")
            side_layout.addWidget(button)

        self.weight_nav_button.setObjectName("navActive")

        side_layout.addStretch()

        note = QLabel("✦\n\nYou've got this!\nConsistency today creates\nresults tomorrow.", sidebar)
        note.setObjectName("note")
        note.setWordWrap(True)
        side_layout.addWidget(note)

        self.profile_pushButton = QPushButton("U    Profile                         ˅", sidebar)
        self.profile_pushButton.setObjectName("user")
        self.profile_pushButton.setFlat(True)
        self.profile_pushButton.setCursor(Qt.PointingHandCursor)
        side_layout.addWidget(self.profile_pushButton)

        main = QFrame()
        main.setObjectName("main")
        main_layout = QVBoxLayout(main)
        main_layout.setContentsMargins(36, 36, 36, 36)
        main_layout.setSpacing(28)

        header = QHBoxLayout()
        title_box = QVBoxLayout()
        title = QLabel("Overview")
        title.setObjectName("title")
        subtitle = QLabel("Track your progress and stay on goal.")
        subtitle.setObjectName("subtitle")
        title_box.addWidget(title)
        title_box.addWidget(subtitle)

        date = QLabel("📅  May 22, 2024")
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

        weight_input = QLineEdit("168.4")
        weight_input.setObjectName("weightInput")
        weight_input.setAlignment(Qt.AlignLeft)
        wl.addWidget(weight_input)

        wl.addWidget(QLabel("📅  May 22, 2024"))

        save = QPushButton("Save Weight")
        save.setObjectName("primaryButton")
        wl.addWidget(save)

        goal_card = Card()
        gl = QHBoxLayout(goal_card)
        gl.setContentsMargins(28, 24, 28, 24)

        left_goal = QVBoxLayout()
        left_goal.addWidget(QLabel("Goal Weight"))

        goal_value = QLabel("150.0 lbs")
        goal_value.setObjectName("metric")
        left_goal.addWidget(goal_value)

        edit = QPushButton("✎  Edit Goal")
        edit.setObjectName("secondaryButton")
        left_goal.addWidget(edit)
        left_goal.addStretch()

        donut_box = QVBoxLayout()
        donut_box.addWidget(Donut(64))
        donut_box.addWidget(QLabel("18.4 lbs to go"), alignment=Qt.AlignCenter)

        gl.addLayout(left_goal)
        gl.addLayout(donut_box)

        summary_card = Card()
        sl = QVBoxLayout(summary_card)
        sl.setContentsMargins(28, 24, 28, 24)
        sl.addWidget(QLabel("Summary"))
        sl.addWidget(QLabel("↗   Current Weight                         168.4 lbs"))
        sl.addWidget(QLabel("↓   Change vs yesterday                  -0.6 lbs"))
        sl.addWidget(QLabel("↓   Change vs goal                       -18.4 lbs"))
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
        tabs = QLabel("7D     30D     3M     6M     1Y     All     📅")
        tabs.setObjectName("tabs")
        chart_header.addWidget(chart_title)
        chart_header.addStretch()
        chart_header.addWidget(tabs)

        chart_layout.addLayout(chart_header)
        chart_layout.addWidget(WeightChart())

        main_layout.addWidget(chart_card)

        root.addWidget(sidebar)
        root.addWidget(main)

        self._navigation_targets = {}
        self._setup_default_navigation_state()

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

        self.set_active_nav(self.weight_nav_button)

    def _refresh_nav_button_style(self, button):
        button.style().unpolish(button)
        button.style().polish(button)
        button.update()

    def set_active_nav(self, active_button):
        for button in self.nav_buttons.values():
            button.setObjectName("navActive" if button is active_button else "nav")
            self._refresh_nav_button_style(button)

    def _navigate_to(self, stack, active_button, target_widget):
        stack.setCurrentWidget(target_widget)
        self.set_active_nav(active_button)


    def showEvent(self, event):
        """Keep the sidebar state correct whenever this page becomes visible."""
        self.set_active_nav(self.weight_nav_button)
        super().showEvent(event)

    def _setup_default_navigation_state(self):
        """Disable nav buttons until main.py wires them to real stacked-widget pages."""
        self.overview_nav_button.setEnabled(False)
        self.weight_nav_button.setEnabled(True)
        self.goals_nav_button.setEnabled(False)
        self.insights_nav_button.setEnabled(False)
        self.settings_nav_button.setEnabled(False)

    def connect_navigation(
        self,
        stack,
        home_widget=None,
        weight_widget=None,
        goals_widget=None,
        insights_widget=None,
        settings_widget=None,
    ):
        self.stack = stack

        routes = {
            "Overview": home_widget,
            "Weight": weight_widget,
            "Goals": goals_widget,
            "Insights": insights_widget,
            "Settings": settings_widget,
        }

        for name, button in self.nav_buttons.items():
            target = routes.get(name)

            if target is not None:
                button.setEnabled(True)
                button.clicked.connect(
                    lambda checked=False, btn=button, w=target: self._navigate_to(stack, btn, w)
                )
            else:
                button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec())
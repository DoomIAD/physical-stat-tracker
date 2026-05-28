from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame, QLabel, QPushButton, QVBoxLayout, QSizePolicy
)


class NavigationBar(QFrame):
    def __init__(self, active_page="Weight", parent=None):
        super().__init__(parent)

        self.setObjectName("sidebar")
        self.setFixedWidth(260)

        self.side_layout = QVBoxLayout(self)
        self.side_layout.setObjectName("sidebarLayout")
        self.side_layout.setContentsMargins(24, 32, 24, 24)
        self.side_layout.setSpacing(18)

        logo = QLabel("⚖  Stat Tracker", self)
        logo.setObjectName("logo")
        self.side_layout.addWidget(logo)

        self.overview_nav_button = QPushButton("⌂  Overview", self)
        self.weight_nav_button = QPushButton("⌁  Weight", self)
        self.goals_nav_button = QPushButton("◎  Goals", self)
        self.insights_nav_button = QPushButton("▥  Insights", self)
        self.settings_nav_button = QPushButton("⚙  Settings", self)

        self.nav_buttons = {
            "Overview": self.overview_nav_button,
            "Weight": self.weight_nav_button,
            "Goals": self.goals_nav_button,
            "Insights": self.insights_nav_button,
            "Settings": self.settings_nav_button,
        }

        for button in self.nav_buttons.values():
            button.setCursor(Qt.PointingHandCursor)
            button.setFlat(True)
            button.setMinimumHeight(44)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            button.setObjectName("nav")
            self.side_layout.addWidget(button)

        self.side_layout.addStretch()

        note = QLabel(
            "✦\n\nYou've got this!\nConsistency today creates\nresults tomorrow.",
            self
        )
        note.setObjectName("note")
        note.setWordWrap(True)
        self.side_layout.addWidget(note)

        self.profile_pushButton = QPushButton(
            "U    Profile                         ˅",
            self
        )
        self.profile_pushButton.setObjectName("user")
        self.profile_pushButton.setFlat(True)
        self.profile_pushButton.setCursor(Qt.PointingHandCursor)
        self.side_layout.addWidget(self.profile_pushButton)

        self.set_active_nav(self.nav_buttons[active_page])
        self.setup_default_navigation_state()

    def refresh_nav_button_style(self, button):
        button.style().unpolish(button)
        button.style().polish(button)
        button.update()

    def set_active_nav(self, active_button):
        for button in self.nav_buttons.values():
            button.setObjectName("navActive" if button is active_button else "nav")
            self.refresh_nav_button_style(button)

    def setup_default_navigation_state(self):
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
                    lambda checked=False, btn=button, w=target: self.navigate_to(stack, btn, w)
                )
            else:
                button.setEnabled(False)

    def navigate_to(self, stack, active_button, target_widget):
        stack.setCurrentWidget(target_widget)
        self.set_active_nav(active_button)
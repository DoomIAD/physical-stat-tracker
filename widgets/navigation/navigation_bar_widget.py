from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame, QLabel, QPushButton, QVBoxLayout, QSizePolicy
)
from shiboken6 import isValid

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

        self._nav_stack = stack
        self._nav_indexes = {}

        for name, button in self.nav_buttons.items():
            target = routes.get(name)

            try:
                button.clicked.disconnect()
            except RuntimeError:
                pass
            except TypeError:
                pass

            if target is not None and isValid(target):
                index = stack.indexOf(target)

                if index == -1:
                    stack.addWidget(target)
                    index = stack.indexOf(target)

                self._nav_indexes[button] = index
                button.setEnabled(True)
                button.clicked.connect(
                    lambda checked=False, btn=button: self.navigate_to(btn)
                )
            else:
                button.setEnabled(False)


    def navigate_to(self, active_button):
        index = self._nav_indexes.get(active_button)

        if index is None:
            return

        if index < 0 or index >= self._nav_stack.count():
            return

        self._nav_stack.setCurrentIndex(index)
        self.set_active_nav(active_button)
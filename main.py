from datetime import datetime
from PySide6 import QtWidgets
from PySide6.QtGui import QFont
from PySide6.QtCore import QSettings
import sys
import math
from datetime import date

from widgets.setup.welcome_widget import Ui_welcome_screen
from widgets.setup.name_widget import Ui_name_widget
from widgets.setup.birthdate_widget import Ui_birthdate_widget
from widgets.setup.height_widget import Ui_height_widget
from widgets.setup.weight_widget import Ui_weight_widget
from widgets.main.styled_home_widget import Ui_debug_widget
from widgets.weight.weight_dashboard_widget import Dashboard

from sql.queries.create_database import *
from sql.queries.insert_database import *
from sql.queries.read_database import *
from sql.queries.edit_database import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 300)

        # Stack
        self.stack = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stack)

        #=========================== Screens ===========================#
        # Welcome screen
        self.welcome_widget = QtWidgets.QWidget()
        self.welcome_ui = Ui_welcome_screen()
        self.welcome_ui.setupUi(self.welcome_widget)

        # Name screen
        self.name_widget = QtWidgets.QWidget()
        self.name_ui = Ui_name_widget()
        self.name_ui.setupUi(self.name_widget)

        # Birthdate screen
        self.birthdate_widget = QtWidgets.QWidget()
        self.birthdate_ui = Ui_birthdate_widget()
        self.birthdate_ui.setupUi(self.birthdate_widget)

        # Height screen
        self.height_widget = QtWidgets.QWidget()
        self.height_ui = Ui_height_widget()
        self.height_ui.setupUi(self.height_widget)

        # Weight screen
        self.weight_widget = QtWidgets.QWidget()
        self.weight_ui = Ui_weight_widget()
        self.weight_ui.setupUi(self.weight_widget)

        # Home screen
        self.debug_widget = QtWidgets.QWidget()
        self.debug_ui = Ui_debug_widget()
        self.debug_ui.setupUi(self.debug_widget)

        # Weight Manager screen
        self.weight_dashboard_widget = Dashboard()

        # Add to stack
        self.stack.addWidget(self.welcome_widget)
        self.stack.addWidget(self.name_widget)
        self.stack.addWidget(self.birthdate_widget)
        self.stack.addWidget(self.height_widget)
        self.stack.addWidget(self.weight_widget)
        self.stack.addWidget(self.debug_widget)
        self.stack.addWidget(self.weight_dashboard_widget)

        self.debug_ui.connect_navigation(
            stack=self.stack,
            home_widget=self.debug_widget,
            weight_widget=self.weight_dashboard_widget,
        )

        self.weight_dashboard_widget.connect_navigation(
            stack=self.stack,
            home_widget=self.debug_widget,
            weight_widget=self.weight_dashboard_widget,
        )

        # Ensure DB/tables exist
        create_database()

        # Persistent app settings
        self.settings = QSettings("physical-stat-tracker", "physical-stat-tracker")

        # Check if setup was completed previously
        setup_complete = self.settings.value("setup_complete", False, type=bool)

        # Check if a user actually exists in DB
        has_user = len(get_all_user_names()) > 0

        # Decide which screen to open
        if setup_complete and has_user:
            self.stack.setCurrentWidget(self.debug_widget)
        else:
            self.settings.setValue("setup_complete", False)
            self.stack.setCurrentWidget(self.welcome_widget)
        #=========================== Basic Functions ===========================#

        # Continue button logic
        self.welcome_ui.continue_button.clicked.connect(self.next_screen)
        self.name_ui.continue_button.clicked.connect(self.next_screen)
        self.birthdate_ui.continue_button.clicked.connect(self.next_screen)
        self.height_ui.continue_button.clicked.connect(self.next_screen)
        self.weight_ui.continue_button.clicked.connect(self.finish_setup)

        # Widget text scaling
        self.update_fonts([
            self.welcome_ui.welcome_title,
            self.weight_ui.weight_title,
            self.height_ui.height_title,
            self.birthdate_ui.birthdate_title,
            self.name_ui.name_title
        ])

    # Uploads setup data to database after all screens done
    def save_data(self):
        # Checks each screen for updated values
        name = self.name_ui.name_TextEdit.toPlainText()
        birthdate = self.birthdate_ui.birthdate_dateEdit.date()
        height_feet = self.height_ui.ft_textEdit.toPlainText()
        height_inches = self.height_ui.in_textEdit.toPlainText()
        weight = self.weight_ui.weight_textEdit.toPlainText()
        print(f"Saving data: {name}, {birthdate.toString('yyyy-MM-dd')}, {height_feet} ft, {height_inches} in, {weight} lbs")

        # Saves data to database if all fields are filled out
        if name and birthdate and height_feet and height_inches and weight:
            insert_user(name, int(height_feet), float(height_inches), birthdate.toString("yyyy-MM-dd"))
            try:
                weight_value = float(weight)
                insert_weight(name, weight_value, datetime.datetime.now().strftime("%Y-%m-%d"))
            except Exception as e:
                print(f"Invalid weight insert: {e}")

    # Ensures values are usable before allowing user to continue to next screen
    def data_checking(self):
        current_index = self.stack.currentIndex()

        if current_index == 1:
            name = self.name_ui.name_TextEdit.toPlainText()
            if not name.strip():
                QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter your name.")
                return False

        elif current_index == 3:
            ft = self.height_ui.ft_textEdit.toPlainText()
            in_ = self.height_ui.in_textEdit.toPlainText()
            if not ft.isdigit() or not in_.isdigit():
                QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter valid numbers for height.")
                return False

        elif current_index == 4:
            weight = self.weight_ui.weight_textEdit.toPlainText()
            if not weight.replace(".", "", 1).isdigit():
                QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter a valid number for weight.")
                return False
        return True

    # Moves to next screen of stack after data_checking()
    def next_screen(self):
        if not self.data_checking():
            return
        self.stack.setCurrentIndex(self.stack.currentIndex() + 1)

    # Resizes fonts of all screens when window is resized
    def resizeEvent(self, event):
        self.update_fonts([
            self.welcome_ui.welcome_title,
            self.weight_ui.weight_title,
            self.height_ui.height_title,
            self.birthdate_ui.birthdate_title,
            self.name_ui.name_title
        ])
        super().resizeEvent(event)
    # Font specific function for resize
    def update_fonts(self, labels):
        font_size = int(self.width() / 20)
        for widget in labels:
            widget.setFont(QFont("Arial", font_size))
    
    def finish_setup(self):
        print("Finishing setup...")
        if not self.data_checking():
            print("Data check failed, cannot finish setup.")
            return

        create_database()
        self.save_data()
        self.settings.setValue("setup_complete", True)
        self.stack.setCurrentWidget(self.debug_widget)
        print("Setup complete, moving to home screen.")

# Main function to run app
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
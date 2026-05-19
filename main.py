# Startup Basics 
#---------------------------
# source .venv/bin/activate
# pyside6-designer
#=================================================

from PySide6 import QtWidgets
from PySide6.QtGui import QFont
import sys

from widgets.setup.welcome_widget import Ui_welcome_screen
from widgets.setup.name_widget import Ui_name_widget
from widgets.setup.birthdate_widget import Ui_birthdate_widget
from widgets.setup.height_widget import Ui_height_widget
from widgets.setup.weight_widget import Ui_weight_widget
from widgets.main.home_widget import Ui_debug_widget

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

        # Debug screen
        self.debug_widget = QtWidgets.QWidget()
        self.debug_ui = Ui_debug_widget()
        self.debug_ui.setupUi(self.debug_widget)

        # Add to stack
        self.stack.addWidget(self.welcome_widget)
        self.stack.addWidget(self.name_widget)
        self.stack.addWidget(self.birthdate_widget)
        self.stack.addWidget(self.height_widget)
        self.stack.addWidget(self.weight_widget)
        self.stack.addWidget(self.debug_widget)

        self.stack.setCurrentIndex(0)
        #=========================== Basic Functions ===========================#

        # Continue button logic
        self.welcome_ui.continue_button.clicked.connect(self.next_screen)
        self.name_ui.continue_button.clicked.connect(self.next_screen)
        self.birthdate_ui.continue_button.clicked.connect(self.next_screen)
        self.height_ui.continue_button.clicked.connect(self.next_screen)
        self.weight_ui.continue_button.clicked.connect(self.next_screen)

        # Widget text scaling
        self.update_fonts([
            self.welcome_ui.welcome_title,
            self.weight_ui.weight_title,
            self.height_ui.height_title,
            self.birthdate_ui.birthdate_title,
            self.name_ui.name_title
        ])

    def save_data(self):
        name = self.name_ui.name_TextEdit.toPlainText()
        birthdate = self.birthdate_ui.birthdate_dateEdit.date()
        height_feet = self.height_ui.ft_textEdit.toPlainText()
        height_inches = self.height_ui.in_textEdit.toPlainText()
        weight = self.weight_ui.weight_textEdit.toPlainText()

        print(f"Name: {name}")
        print(f"Birthdate: {birthdate.toString()}")
        print(f"Height: {height_feet} ft {height_inches} in")
        print(f"Weight: {weight} lbs")

    def data_checking(self):
        current_index = self.stack.currentIndex()
        # Name Screen
        if current_index == 1:
            name = self.name_ui.name_TextEdit.toPlainText()
            if not name.strip():
                QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter your name.")
                return False
        # Birthdate screen
        elif current_index == 2:
            birthdate = self.birthdate_ui.birthdate_dateEdit.date()
        # Height screen
        elif current_index == 3: 
            ft = self.height_ui.ft_textEdit.toPlainText()
            in_ = self.height_ui.in_textEdit.toPlainText()
            if not ft.isdigit() or not in_.isdigit():
                QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter valid numbers for height.")
                return False
        # Weight screen
        elif current_index == 4: 
            weight = self.weight_ui.weight_textEdit.toPlainText()
            if not weight.isdigit():
                QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter a valid number for weight.")
                return False
            self.save_data()
        return True

    def next_screen(self):
        if not self.data_checking():
            return
        current_index = self.stack.currentIndex()
        if current_index < self.stack.count() - 1:
            new_index = current_index + 1
            self.stack.setCurrentIndex(new_index)

            # Run when debug widget appears
            if self.stack.widget(new_index) == self.debug_widget:
                self.update_label()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_fonts([
            self.welcome_ui.welcome_title,
            self.weight_ui.weight_title,
            self.height_ui.height_title,
            self.birthdate_ui.birthdate_title,
            self.name_ui.name_title
        ])

    def update_fonts(self, labels, base_size=24, min_size=24):
        scale = min(self.width() / 400, self.height() / 300)
        size = max(min_size, int(base_size * scale))

        for label in labels:
            font = label.font()
            font.setPointSize(size)
            label.setFont(font)
    
    def update_label(self):
        self.debug_ui.title_label.setText(f"Hey There {self.name_ui.name_TextEdit.toPlainText()}")
        self.debug_ui.bmi_label.setText(f"BMI: {self.calculate_bmi()}")
        self.debug_ui.fat_label.setText(f"Body Fat %: {self.calculate_body_fat()}")
        self.debug_ui.percentile_label.setText(f"Percentile: {self.calculate_percentile()}")
        self.debug_ui.workout_label.setText(f"Today's Workout: {self.get_todays_workout()}")
    
    def calculate_bmi(self):
        height_ft = int(self.height_ui.ft_textEdit.toPlainText())
        height_in = int(self.height_ui.in_textEdit.toPlainText())
        weight_lb = int(self.weight_ui.weight_textEdit.toPlainText())

        total_height_in = height_ft * 12 + height_in
        bmi = (weight_lb / (total_height_in ** 2)) * 703
        return round(bmi, 2)
    
    def calculate_body_fat(self):
        # Placeholder for body fat calculation
        return "N/A"

    def calculate_percentile(self):
        # Placeholder for percentile calculation
        return "N/A"

    def get_todays_workout(self):
        # Placeholder for today's workout
        return "N/A"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
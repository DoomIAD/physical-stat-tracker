from PySide6 import QtWidgets
from PySide6.QtGui import QFont
import sys

from widgets.setup.welcome_widget import Ui_welcome_screen
from widgets.setup.name_widget import Ui_name_widget
from widgets.setup.birthdate_widget import Ui_birthdate_widget
from widgets.setup.height_widget import Ui_height_widget
from widgets.setup.weight_widget import Ui_weight_widget
from widgets.main.debug_widget import Ui_debug_widget

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

        #=========================== Functions ===========================#

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

    def next_screen(self):
        current_index = self.stack.currentIndex()
        if current_index < self.stack.count() - 1:
            self.stack.setCurrentIndex(current_index + 1)

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
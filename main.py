from PySide6 import QtWidgets
from setup_screens.welcome_screen import Ui_welcome_screen
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_welcome_screen()
        self.ui.setupUi(self)

        # Example: connect a button
        self.ui.pushButton.clicked.connect(self.handle_click)

    def handle_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
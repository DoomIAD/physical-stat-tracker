from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QLineEdit,
    QVBoxLayout
)

class GoalDialog(QDialog):
    def __init__(self, current_goal, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Edit Goal Weight")
        self.setFixedWidth(300)

        layout = QVBoxLayout(self)

        title = QLabel("Enter new goal weight")
        layout.addWidget(title)

        self.goal_input = QLineEdit()
        self.goal_input.setText(str(current_goal))
        layout.addWidget(self.goal_input)

        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

    def get_goal_weight(self):
        return float(self.goal_input.text())
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import QWidget

from sql.queries.read_database import get_activity_history


class ActivityChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumHeight(120)

        self.activity_data = []

        self.colors = {
            0: QColor("#ebedf0"),
            1: QColor("#9be9a8"),
            2: QColor("#40c463"),
            3: QColor("#30a14e"),
            4: QColor("#216e39"),
        }

    def load_activity_data(self, username):
        if not self.activity_data:
            return
        self.activity_data = get_activity_history(username)
        self.update()  # triggers repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        cell_size = 10
        gap = 4
        radius = 2

        start_x = 10
        start_y = 10

        for row, days in enumerate(self.activity_data):
            for col, value in enumerate(days):
                x = start_x + col * (cell_size + gap)
                y = start_y + row * (cell_size + gap)

                painter.setBrush(self.colors.get(value, self.colors[0]))
                painter.setPen(Qt.NoPen)

                rect = QRect(x, y, cell_size, cell_size)
                painter.drawRoundedRect(rect, radius, radius)
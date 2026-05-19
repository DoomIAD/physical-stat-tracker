from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import QWidget


class ActivityChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumHeight(120)

        # 7 rows = days, 16 columns = weeks/example history
        self.activity_data = [
            [0, 1, 2, 0, 3, 4, 1, 0, 2, 3, 1, 0, 4, 2, 1, 3],
            [1, 0, 3, 2, 0, 1, 4, 2, 0, 3, 2, 1, 0, 4, 3, 1],
            [0, 2, 1, 4, 3, 0, 2, 1, 3, 0, 4, 2, 1, 3, 0, 2],
            [3, 1, 0, 2, 4, 3, 1, 0, 2, 4, 3, 1, 0, 2, 4, 3],
            [0, 4, 2, 1, 0, 3, 2, 4, 1, 0, 3, 2, 4, 1, 0, 3],
            [2, 0, 1, 3, 4, 2, 0, 1, 3, 4, 2, 0, 1, 3, 4, 2],
            [1, 3, 4, 0, 2, 1, 3, 4, 0, 2, 1, 3, 4, 0, 2, 1],
        ]

        self.colors = {
            0: QColor("#ebedf0"),
            1: QColor("#9be9a8"),
            2: QColor("#40c463"),
            3: QColor("#30a14e"),
            4: QColor("#216e39"),
        }

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
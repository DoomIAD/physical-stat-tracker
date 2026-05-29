import datetime

from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPainter, QPen, QColor, QFont, QPainterPath
from PySide6.QtWidgets import QWidget

from sql.queries.read_database import get_weight_history


class WeightChart(QWidget):
    def __init__(self):
        super().__init__()
        self.weights = []
        self.dates = []
        self.name = None
        self.goal = 150
        self.setMinimumHeight(340)

    # Creates a line graph of user's weight history using data from database
    def get_weight_data(self, name):
        self.name = name
        weight_history = get_weight_history(name)

        self.dates = []
        self.weights = []

        for date, weight in weight_history:
            self.dates.append(self._to_date(date))
            self.weights.append(float(weight))

        self.update()

    def _to_date(self, value):
        if isinstance(value, datetime.datetime):
            return value.date()

        if isinstance(value, datetime.date):
            return value

        if isinstance(value, str):
            return datetime.datetime.strptime(value, "%Y-%m-%d").date()

        return value

    def paintEvent(self, event):
        if not self.weights:
            return

        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        margin_l, margin_t, margin_r, margin_b = 55, 40, 35, 55
        chart_w = self.width() - margin_l - margin_r
        chart_h = self.height() - margin_t - margin_b

        if chart_w <= 0 or chart_h <= 0:
            return

        y_min = min(min(self.weights), self.goal) - 10
        y_max = max(max(self.weights), self.goal) + 10

        def x_at(i):
            if len(self.weights) == 1:
                return margin_l + chart_w / 2

            return margin_l + i * chart_w / (len(self.weights) - 1)

        def y_at(weight):
            if y_max == y_min:
                return margin_t + chart_h / 2

            return margin_t + (y_max - weight) * chart_h / (y_max - y_min)

        def get_y_axis_values():
            start = int(y_min // 10 * 10)
            end = int((y_max + 9) // 10 * 10)

            return range(start, end + 1, 10)

        def get_date_labels():
            if not self.dates:
                return []

            labels = []
            total = len(self.dates)

            if total == 1:
                return [(0, self.dates[0].strftime("%d %b"))]

            target_indexes = {0, total - 1}

            if total > 2:
                target_indexes.add(total // 2)

            for i in sorted(target_indexes):
                labels.append((i, self.dates[i].strftime("%d %b")))

            return labels

        p.setFont(QFont("Arial", 9))
        p.setPen(QColor("#6B7280"))

        for y in get_y_axis_values():
            py = y_at(y)

            p.setPen(QColor("#6B7280"))
            p.drawText(10, int(py + 4), str(y))

            p.setPen(QPen(QColor("#E5E7EB"), 1, Qt.DashLine))
            p.drawLine(
                int(margin_l),
                int(py),
                int(margin_l + chart_w),
                int(py),
            )

        goal_y = y_at(self.goal)

        p.setPen(QPen(QColor("#34A853"), 2, Qt.DashLine))
        p.drawLine(
            int(margin_l),
            int(goal_y),
            int(margin_l + chart_w),
            int(goal_y),
        )

        p.setPen(QColor("#34A853"))
        p.drawText(
            int(margin_l + chart_w - 100),
            int(goal_y - 10),
            f"Goal: {self.goal} lbs",
        )

        path = QPainterPath(QPointF(x_at(0), y_at(self.weights[0])))

        for i, weight in enumerate(self.weights[1:], 1):
            path.lineTo(QPointF(x_at(i), y_at(weight)))

        p.setPen(QPen(QColor("#2563EB"), 2))
        p.drawPath(path)

        p.setBrush(QColor("#FFFFFF"))
        p.setPen(QPen(QColor("#2563EB"), 2))

        for i, weight in enumerate(self.weights):
            p.drawEllipse(QPointF(x_at(i), y_at(weight)), 3, 3)

        last_x = x_at(len(self.weights) - 1)
        last_y = y_at(self.weights[-1])

        p.setBrush(QColor("#2563EB"))
        p.setPen(Qt.NoPen)
        p.drawRoundedRect(
            int(last_x - 3),
            int(last_y - 15),
            52,
            28,
            6,
            6,
        )

        p.setPen(QColor("#FFFFFF"))
        p.drawText(
            int(last_x + 5),
            int(last_y + 4),
            f"{self.weights[-1]:g}",
        )

        p.setPen(QColor("#6B7280"))

        for i, label in get_date_labels():
            x = x_at(i)
            p.drawText(
                int(x - 20),
                self.height() - 22,
                label,
            )
import datetime

from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPainter, QPen, QColor, QFont, QPainterPath
from PySide6.QtWidgets import QWidget

from sql.queries.read_database import get_all_user_names, get_weight_history


class WeightChart(QWidget):
    def __init__(self):
        super().__init__()
        self.weights = []
        self.goal = 150
        self.setMinimumHeight(340)

    # Creates a line graph of user's weight history using data from database
    def get_weight_data(self, name):
        weight_history = get_weight_history(name)

        self.weights = [
            float(weight)
            for date, weight in weight_history
        ]

        if not self.weights:
            return

        self.update()

    def paintEvent(self, event):

        users = get_all_user_names()
        if not users:
            return
        name = users[0]

        def x_at(i):
            return margin_l + i * w / (len(self.weights) - 1)

        def y_at(value):
            return margin_t + (y_max - value) / (y_max - y_min) * h

        def get_date_labels(username):
            today = datetime.datetime.today().date()
            weight_logs = get_weight_history(username)

            if not weight_logs:
                return []

            first_day = weight_logs[0][0]

            if isinstance(first_day, datetime.datetime):
                first_day = first_day.date()
            elif isinstance(first_day, str):
                first_day = datetime.datetime.strptime(first_day, "%Y-%m-%d").date()

            cutoff_date = max(first_day, today - datetime.timedelta(days=30))

            labels = []
            current_date = today

            while current_date >= cutoff_date:
                labels.insert(0, current_date.strftime("%d %b"))
                current_date -= datetime.timedelta(days=7)

            return labels

        def get_min_max(username):
            weight_history = get_weight_history(username)
            min_weight = min(float(weight) for date, weight in weight_history)
            max_weight = max(float(weight) for date, weight in weight_history)
            return min_weight, max_weight

        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        margin_l, margin_t, margin_r, margin_b = 55, 40, 35, 55
        w = self.width() - margin_l - margin_r
        h = self.height() - margin_t - margin_b

        y_min, y_max = get_min_max(name)
        y_min = y_min - 10
        y_max = y_max + 10

        p.setFont(QFont("Arial", 9))
        p.setPen(QColor("#6B7280"))

        for y in range(140, 191, 10):
            py = y_at(y)
            p.drawText(10, py + 4, str(y))
            p.setPen(QPen(QColor("#E5E7EB"), 1, Qt.DashLine))
            p.drawLine(margin_l, py, margin_l + w, py)
            p.setPen(QColor("#6B7280"))

        goal_y = y_at(self.goal)
        p.setPen(QPen(QColor("#34A853"), 2, Qt.DashLine))
        p.drawLine(margin_l, goal_y, margin_l + w, goal_y)

        p.setPen(QColor("#34A853"))
        goal_weight = 150
        p.drawText(margin_l + w - 100, goal_y - 10, f"Goal: {goal_weight} lbs")

        path = QPainterPath(QPointF(x_at(0), y_at(self.weights[0])))

        for i, weight in enumerate(self.weights[1:], 1):
            path.lineTo(x_at(i), y_at(weight))

        p.setPen(QPen(QColor("#2563EB"), 2))
        p.drawPath(path)

        p.setBrush(QColor("#FFFFFF"))

        for i, weight in enumerate(self.weights):
            p.drawEllipse(QPointF(x_at(i), y_at(weight)), 3, 3)

        last_x = x_at(len(self.weights) - 1)
        last_y = y_at(self.weights[-1])

        p.setBrush(QColor("#2563EB"))
        p.setPen(Qt.NoPen)
        p.drawRoundedRect(last_x - 3, last_y - 15, 52, 28, 6, 6)

        p.setPen(QColor("#FFFFFF"))

        weight_history = get_weight_history(name)
        temp_date, current_weight = weight_history[-1]

        p.drawText(last_x + 5, last_y + 4, f"{current_weight}")

        p.setPen(QColor("#6B7280"))

        labels = get_date_labels(name)

        for i, label in enumerate(labels):
            if len(labels) == 1:
                x = margin_l + w / 2
            else:
                x = margin_l + i * w / (len(labels) - 1)

            p.drawText(x - 20, self.height() - 22, label)
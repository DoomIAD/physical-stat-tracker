from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt, QMargins


class WeightChartWidget(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.series = QLineSeries()

        # Soft transparent line
        pen = QPen(QColor(255, 255, 255, 50))
        pen.setWidthF(2.0)
        self.series.setPen(pen)

        self.chart = QChart()
        self.chart.addSeries(self.series)

        # Remove visual clutter
        self.chart.legend().hide()
        self.chart.setTitle("")
        self.chart.setBackgroundVisible(False)
        self.chart.setPlotAreaBackgroundVisible(False)
        self.chart.setMargins(QMargins(0, 0, 0, 0))

        # X axis
        self.axis_x = QValueAxis()
        self.axis_x.setRange(0, 1)

        # Hide labels but keep grid lines
        self.axis_x.setLabelsVisible(False)
        self.axis_x.setGridLineVisible(True)
        self.axis_x.setLineVisible(False)

        # Optional: subtle grid color
        self.axis_x.setGridLineColor(QColor(255, 255, 255, 30))

        # Y axis
        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, 1)

        # Show labels
        self.axis_y.setLabelsVisible(True)

        # Keep clean appearance
        self.axis_y.setGridLineVisible(False)
        self.axis_y.setLineVisible(False)

        # Optional label styling
        self.axis_y.setLabelsColor(QColor(255, 255, 255, 120))

        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)

        self.series.attachAxis(self.axis_x)
        self.series.attachAxis(self.axis_y)

        self.setChart(self.chart)

        # Smooth rendering
        self.setRenderHint(QPainter.Antialiasing)

        # Fully transparent widget background
        self.setStyleSheet("background: transparent; border: 0px;")
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt


class WeightChartWidget(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.series = QLineSeries()
        self.series.setName("Weight")

        self.series.append(0, 180)
        self.series.append(1, 178)
        self.series.append(2, 176)
        self.series.append(3, 177)

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Weight")
        self.chart.legend().hide()
        self.chart.setBackgroundVisible(False)
        self.chart.setPlotAreaBackgroundVisible(False)

        axis_x = QValueAxis()
        axis_x.setTitleText("Week")
        axis_x.setRange(0, 3)

        axis_y = QValueAxis()
        axis_y.setTitleText("Weight")
        axis_y.setRange(170, 185)

        self.chart.addAxis(axis_x, Qt.AlignBottom)
        self.chart.addAxis(axis_y, Qt.AlignLeft)

        self.series.attachAxis(axis_x)
        self.series.attachAxis(axis_y)

        self.setChart(self.chart)
        self.setRenderHint(QPainter.Antialiasing)
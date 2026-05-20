from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt


class WeightChartWidget(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.series = QLineSeries()
        self.series.setName("Weight")

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Weight")
        self.chart.legend().hide()
        self.chart.setBackgroundVisible(False)
        self.chart.setPlotAreaBackgroundVisible(False)

        self.axis_x = QValueAxis()
        self.axis_x.setTitleText("Entry")
        self.axis_x.setLabelFormat("%d")
        self.axis_x.setRange(0, 1)

        self.axis_y = QValueAxis()
        self.axis_y.setTitleText("Weight")
        self.axis_y.setRange(0, 1)

        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)

        self.series.attachAxis(self.axis_x)
        self.series.attachAxis(self.axis_y)

        self.setChart(self.chart)
        self.setRenderHint(QPainter.Antialiasing)
"""Tests for widgets.main.activity_chart.ActivityChartWidget."""

from __future__ import annotations

from PySide6.QtCore import QSize

from widgets.main import activity_chart as activity_module
from widgets.main.activity_chart import ActivityChartWidget


def test_activity_chart_initial_state(qapp):
    widget = ActivityChartWidget()

    assert widget.minimumHeight() == 120
    assert widget.activity_data == []
    assert set(widget.colors) == {0, 1, 2, 3, 4}


def test_load_activity_data_fetches_database_grid_and_updates(monkeypatch, qapp):
    grid = [[0 for _ in range(6)] for _ in range(7)]
    grid[0][0] = 4
    calls = []

    monkeypatch.setattr(activity_module, "get_activity_history", lambda username: calls.append(username) or grid)

    widget = ActivityChartWidget()
    updated = []
    widget.update = lambda: updated.append(True)

    widget.load_activity_data("David")

    assert calls == ["David"]
    assert widget.activity_data is grid
    assert updated == [True]


def test_load_activity_data_does_not_update_for_empty_result(monkeypatch, qapp):
    monkeypatch.setattr(activity_module, "get_activity_history", lambda username: [])
    widget = ActivityChartWidget()
    updated = []
    widget.update = lambda: updated.append(True)

    widget.load_activity_data("David")

    assert widget.activity_data == []
    assert updated == []


def test_paint_event_handles_empty_and_populated_data(qapp):
    widget = ActivityChartWidget()
    widget.resize(QSize(200, 200))

    widget.paintEvent(None)
    widget.activity_data = [[0, 1, 2, 3, 4, 99] for _ in range(7)]
    widget.paintEvent(None)

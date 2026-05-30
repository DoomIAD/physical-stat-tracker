"""Tests for widgets.weight.weight_graph_widget.WeightChart."""

from __future__ import annotations

import datetime as dt

from widgets.weight import weight_graph_widget as graph_module
from widgets.weight.weight_graph_widget import WeightChart


def test_weight_chart_initial_state(qapp):
    chart = WeightChart()

    assert chart.weights == []
    assert chart.dates == []
    assert chart.name is None
    assert chart.goal == 150
    assert chart.minimumHeight() == 340


def test_to_date_accepts_datetime_date_and_string(qapp):
    chart = WeightChart()

    assert chart._to_date(dt.datetime(2026, 5, 30, 12, 0)) == dt.date(2026, 5, 30)
    assert chart._to_date(dt.date(2026, 5, 30)) == dt.date(2026, 5, 30)
    assert chart._to_date("2026-05-30") == dt.date(2026, 5, 30)


def test_get_weight_data_loads_goal_dates_and_weights(monkeypatch, qapp):
    monkeypatch.setattr(graph_module, "get_goal_data", lambda name: (165.0, 185.0))
    monkeypatch.setattr(
        graph_module,
        "get_weight_history",
        lambda name: [("2026-05-29", 181.2), (dt.date(2026, 5, 30), 180)],
    )

    chart = WeightChart()
    updated = []
    chart.update = lambda: updated.append(True)

    chart.get_weight_data("David")

    assert chart.name == "David"
    assert chart.goal == 165.0
    assert chart.dates == [dt.date(2026, 5, 29), dt.date(2026, 5, 30)]
    assert chart.weights == [181.2, 180.0]
    assert updated == [True]


def test_get_weight_data_keeps_default_goal_when_no_goal_data(monkeypatch, qapp):
    monkeypatch.setattr(graph_module, "get_goal_data", lambda name: None)
    monkeypatch.setattr(graph_module, "get_weight_history", lambda name: [])
    chart = WeightChart()
    chart.goal = 177.0

    chart.get_weight_data("David")

    assert chart.goal == 177.0
    assert chart.weights == []
    assert chart.dates == []


def test_set_goal_updates_goal_and_repaints(qapp):
    chart = WeightChart()
    updated = []
    chart.update = lambda: updated.append(True)

    chart.set_goal("155.5")

    assert chart.goal == 155.5
    assert updated == [True]


def test_paint_event_handles_empty_single_and_multiple_points(qapp):
    chart = WeightChart()
    chart.resize(500, 360)

    chart.paintEvent(None)

    chart.goal = 170.0
    chart.weights = [180.0]
    chart.dates = [dt.date(2026, 5, 30)]
    chart.paintEvent(None)

    chart.weights = [182.0, 180.0, 179.5]
    chart.dates = [dt.date(2026, 5, 28), dt.date(2026, 5, 29), dt.date(2026, 5, 30)]
    chart.paintEvent(None)

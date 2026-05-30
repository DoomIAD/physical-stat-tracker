"""Comprehensive unit tests for widgets.weight.weight_dashboard_widget."""

from __future__ import annotations

import datetime as dt

import pytest
from PySide6.QtWidgets import QFrame
from widgets.weight import weight_dashboard_widget as dashboard_module
from widgets.weight.weight_dashboard_widget import Card, Dashboard, Donut


def make_dashboard_without_init(current_weight=180.0, start_weight=200.0, goal_weight=160.0):
    instance = Dashboard.__new__(Dashboard)
    instance.current_weight = current_weight
    instance.start_weight = start_weight
    instance.goal_weight = goal_weight
    return instance


@pytest.mark.parametrize(
    "current,start,goal,expected",
    [
        (180.0, 200.0, 160.0, 50.0),
        (160.0, 200.0, 160.0, 100.0),
        (210.0, 200.0, 160.0, 0),
        (150.0, 200.0, 160.0, 100),
        (150.0, 150.0, 150.0, 100),
        (151.0, 150.0, 150.0, 0),
        (190.0, 160.0, 200.0, 75.0),
    ],
)
def test_calculate_progress_clamps_and_handles_gain_or_loss_goals(current, start, goal, expected):
    dashboard = make_dashboard_without_init(current, start, goal)

    assert dashboard.calculate_progress() == expected


def test_save_weight_inserts_rounded_weight_and_refreshes_ui(monkeypatch):
    dashboard = make_dashboard_without_init(current_weight=180.0, start_weight=200.0, goal_weight=160.0)
    dashboard.weight_input = type("FakeInput", (), {"text": lambda self: "177.66"})()

    class FakeChart:
        def __init__(self):
            self.names = []

        def get_weight_data(self, name):
            self.names.append(name)

    class FakeDonut:
        def __init__(self):
            self.progress = None
            self.updated = False

        def update(self):
            self.updated = True

    dashboard.weight_chart = FakeChart()
    dashboard.donut = FakeDonut()
    inserted = []

    monkeypatch.setattr(dashboard_module, "insert_weight", lambda name, weight, date: inserted.append((name, weight, date)))

    class FakeDateTime(dt.datetime):
        @classmethod
        def now(cls):
            return cls(2026, 5, 30, 12, 0, 0)

    monkeypatch.setattr(dashboard_module.datetime, "datetime", FakeDateTime)

    dashboard.save_weight("David")

    assert inserted == [("David", 177.7, "2026-05-30")]
    assert dashboard.current_weight == 177.7
    assert dashboard.weight_chart.names == ["David"]
    assert dashboard.donut.progress == dashboard.calculate_progress()
    assert dashboard.donut.updated is True


def test_save_weight_rejects_non_numeric_input_without_mutating_state(monkeypatch):
    dashboard = make_dashboard_without_init(current_weight=180.0, start_weight=200.0, goal_weight=160.0)
    dashboard.weight_input = type("FakeInput", (), {"text": lambda self: "abc"})()
    dashboard.weight_chart = type("FakeChart", (), {"get_weight_data": lambda self, name: None})()
    dashboard.donut = type("FakeDonut", (), {"update": lambda self: None})()
    calls = []
    monkeypatch.setattr(dashboard_module, "insert_weight", lambda *args: calls.append(args))

    with pytest.raises(ValueError):
        dashboard.save_weight("David")

    assert calls == []
    assert dashboard.current_weight == 180.0


def test_open_goal_dialog_accepts_goal_and_updates_user(monkeypatch):
    dashboard = make_dashboard_without_init(current_weight=180.0, start_weight=200.0, goal_weight=160.0)

    class FakeLabel:
        def __init__(self):
            self.text = None

        def setText(self, text):
            self.text = text

    class FakeChart:
        def __init__(self):
            self.goal = None

        def set_goal(self, goal):
            self.goal = goal

    class FakeDonut:
        def __init__(self):
            self.progress = None
            self.updated = False

        def update(self):
            self.updated = True

    class FakeGoalDialog:
        def __init__(self, current_goal, parent):
            self.current_goal = current_goal
            self.parent = parent

        def exec(self):
            return True

        def get_goal_weight(self):
            return 155.0

    dashboard.goal_value = FakeLabel()
    dashboard.weight_chart = FakeChart()
    dashboard.donut = FakeDonut()
    updates = []

    monkeypatch.setattr(dashboard_module, "GoalDialog", FakeGoalDialog)
    monkeypatch.setattr(dashboard_module, "update_user", lambda **kwargs: updates.append(kwargs))

    dashboard.open_goal_dialog("David")

    assert dashboard.goal_weight == 155.0
    assert dashboard.goal_value.text == "155.0 lbs"
    assert updates == [{"username": "David", "goal": 155.0, "start_weight": 180.0}]
    assert dashboard.start_weight == 180.0
    assert dashboard.weight_chart.goal == 155.0
    assert dashboard.donut.progress == dashboard.calculate_progress()
    assert dashboard.donut.updated is True


def test_open_goal_dialog_cancel_does_not_update(monkeypatch):
    dashboard = make_dashboard_without_init(current_weight=180.0, start_weight=200.0, goal_weight=160.0)
    dashboard.goal_value = type("FakeLabel", (), {"setText": lambda self, text: None})()
    dashboard.weight_chart = type("FakeChart", (), {"set_goal": lambda self, goal: None})()
    dashboard.donut = type("FakeDonut", (), {"update": lambda self: None})()

    class CancelledGoalDialog:
        def __init__(self, current_goal, parent):
            pass

        def exec(self):
            return False

    calls = []
    monkeypatch.setattr(dashboard_module, "GoalDialog", CancelledGoalDialog)
    monkeypatch.setattr(dashboard_module, "update_user", lambda **kwargs: calls.append(kwargs))

    dashboard.open_goal_dialog("David")

    assert dashboard.goal_weight == 160.0
    assert dashboard.start_weight == 200.0
    assert calls == []


def test_connect_navigation_delegates_to_navigation_bar():
    dashboard = make_dashboard_without_init()

    class FakeNavigationBar:
        def __init__(self):
            self.args = None

        def connect_navigation(self, *args):
            self.args = args

    dashboard.navigation_bar = FakeNavigationBar()
    stack = object()
    home = object()
    weight = object()

    dashboard.connect_navigation(stack=stack, home_widget=home, weight_widget=weight)

    assert dashboard.navigation_bar.args == (stack, home, weight, None, None, None)


def test_show_event_marks_weight_nav_active(monkeypatch):
    dashboard = make_dashboard_without_init()
    dashboard.navigation_bar = type(
        "FakeNav",
        (),
        {
            "weight_nav_button": object(),
            "set_active_nav": lambda self, button: setattr(self, "active", button),
        },
    )()
    called = []
    monkeypatch.setattr(dashboard_module.QWidget, "showEvent", lambda self, event: called.append(event))
    event = object()

    dashboard.showEvent(event)

    assert dashboard.navigation_bar.active is dashboard.navigation_bar.weight_nav_button
    assert called == [event]


def test_card_and_donut_smoke_render(qapp):
    card = Card()
    donut = Donut(72.5)
    donut.resize(160, 160)

    assert card.objectName() == "card"
    assert donut.progress == 72.5
    donut.paintEvent(None)


def test_dashboard_init_returns_early_when_no_users(monkeypatch):
    monkeypatch.setattr(dashboard_module, "get_all_user_names", lambda: [])

    dashboard = Dashboard()

    assert not hasattr(dashboard, "navigation_bar")
    assert not hasattr(dashboard, "current_weight")


def test_dashboard_init_builds_core_state_with_existing_user(monkeypatch, qapp):
    class FakeNavigationBar(QFrame):
        def __init__(self, active_page="Weight", parent=None):
            super().__init__(parent)
            self.active_page = active_page
            self.parent_ref = parent

    monkeypatch.setattr(dashboard_module, "NavigationBar", FakeNavigationBar)
    monkeypatch.setattr(dashboard_module, "get_all_user_names", lambda: ["David"])
    monkeypatch.setattr(dashboard_module, "get_weight_history", lambda name: [("2026-05-29", 181.0), ("2026-05-30", 180.0)])
    monkeypatch.setattr(dashboard_module, "get_goal_data", lambda name: (165.0, 185.0))
    monkeypatch.setattr(dashboard_module.WeightChart, "get_weight_data", lambda self, name: setattr(self, "loaded_name", name))

    dashboard = Dashboard()

    assert dashboard.current_weight == 180.0
    assert dashboard.goal_weight == 165.0
    assert dashboard.start_weight == 185.0
    assert dashboard.goal_value.text() == "165.0 lbs"
    assert dashboard.weight_chart.goal == 165.0
    assert dashboard.weight_chart.loaded_name == "David"

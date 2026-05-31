"""Tests for widgets.main.styled_home_widget.Ui_debug_widget logic."""

from __future__ import annotations

import math
from unittest.mock import Mock

import pytest

from widgets.main import styled_home_widget as home_module
from widgets.main.styled_home_widget import Ui_debug_widget


@pytest.fixture
def ui():
    return Ui_debug_widget()


@pytest.mark.parametrize(
    "weight,height_ft,height_in,expected",
    [
        (180, 5, 10, round((180 / (70 ** 2)) * 703, 2)),
        ("180", "5", "10", round((180 / (70 ** 2)) * 703, 2)),
        (0, 5, 10, 0.0),
        (180, 6, 0, round((180 / (72 ** 2)) * 703, 2)),
    ],
)
def test_calculate_bmi_valid_inputs(ui, weight, height_ft, height_in, expected):
    assert ui.calculate_bmi(weight, height_ft, height_in) == expected


@pytest.mark.parametrize(
    "weight,height_ft,height_in",
    [
        (None, 5, 10),
        (180, None, 10),
        (180, 5, None),
        ("abc", 5, 10),
        (180, "bad", 10),
        (180, 0, 0),
        (180, -5, 10),
    ],
)
def test_calculate_bmi_invalid_inputs_return_none(ui, weight, height_ft, height_in):
    assert ui.calculate_bmi(weight, height_ft, height_in) is None


@pytest.mark.parametrize(
    "gender,neck,waist,constant_height,offset",
    [
        ("male", 16, 34, 69, 36.76),
        ("MALE", 16, 34, 69, 36.76),
    ],
)
def test_calculate_body_fat_male(ui, gender, neck, waist, constant_height, offset):
    expected = 86.010 * math.log10(waist - neck) - 70.041 * math.log10(constant_height) + offset
    assert ui.calculate_body_fat(gender, neck, waist) == round(expected, 2)


def test_calculate_body_fat_female(ui):
    expected = 163.205 * math.log10(30 - 14) - 97.684 * math.log10(64) - 78.387
    assert ui.calculate_body_fat("female", 14, 30) == round(expected, 2)


@pytest.mark.parametrize("gender,neck,waist", [(None, 14, 30), ("female", None, 30), ("female", 14, None)])
def test_calculate_body_fat_missing_data(ui, gender, neck, waist):
    assert ui.calculate_body_fat(gender, neck, waist) == {"Missing data for body fat calculation"}


@pytest.mark.parametrize("gender,neck,waist", [("male", 16, 16), ("female", 20, 18)])
def test_calculate_body_fat_invalid_measurements_raise_value_error(ui, gender, neck, waist):
    with pytest.raises(ValueError):
        ui.calculate_body_fat(gender, neck, waist)


def test_get_todays_workout_uses_read_database_function(monkeypatch, ui):
    calls = []

    def fake_get_user_workout_plan_for_day(username):
        calls.append(username)
        return "Push Day"

    monkeypatch.setattr(
        "sql.queries.read_database.get_user_workout_plan_for_day",
        fake_get_user_workout_plan_for_day,
    )

    assert ui.get_todays_workout("David") == "Push Day"
    assert calls == ["David"]


def test_update_weight_graph_delegates_to_weight_chart(ui):
    ui.weightchart_widget = Mock()

    ui.update_weight_graph("David")

    ui.weightchart_widget.get_weight_data.assert_called_once_with("David")


def test_update_activity_graph_delegates_to_activity_widget(ui):
    ui.activity_widget = Mock()

    ui.update_activity_graph("David")

    ui.activity_widget.load_activity_data.assert_called_once_with("David")


def install_label_mocks(ui):
    ui.title_label = Mock()
    ui.bmi_label = Mock()
    ui.fat_label = Mock()
    ui.percentile_label = Mock()
    ui.workout_label = Mock()
    ui.update_weight_graph = Mock()
    ui.update_activity_graph = Mock()


def test_update_label_returns_without_work_when_no_users(monkeypatch, ui):
    monkeypatch.setattr(home_module, "get_all_user_names", lambda: [])
    install_label_mocks(ui)

    ui.update_label()

    ui.title_label.setText.assert_not_called()
    ui.update_weight_graph.assert_not_called()
    ui.update_activity_graph.assert_not_called()


def test_update_label_updates_all_labels_and_graphs(monkeypatch, ui):
    monkeypatch.setattr(home_module, "get_all_user_names", lambda: ["David"])
    monkeypatch.setattr(
        home_module,
        "get_user_by_name",
        lambda name: ("David", 5, 10, "2000-01-01", "male", 16, 34, 165, 185),
    )
    monkeypatch.setattr(home_module, "get_current_weight", lambda name: 180)
    monkeypatch.setattr(home_module, "get_weight_history", lambda name: [("2026-05-30", 180)])
    monkeypatch.setattr(ui, "get_todays_workout", lambda name: "Leg Day")
    install_label_mocks(ui)

    ui.update_label()

    ui.title_label.setText.assert_called_once_with("Hey There David,")
    ui.bmi_label.setText.assert_called_once_with(f"{ui.calculate_bmi(180, 5, 10):.1f} BMI")
    ui.fat_label.setText.assert_called_once_with(f"{ui.calculate_body_fat('male', 16, 34):.1f}% Body Fat")
    ui.percentile_label.setText.assert_called_once_with("No Information for Fitness Percentile")
    ui.workout_label.setText.assert_called_once_with("Leg Day")
    ui.update_weight_graph.assert_called_once_with("David")
    ui.update_activity_graph.assert_called_once_with("David")


def test_update_label_handles_missing_weight_and_missing_body_fat_inputs(monkeypatch, ui):
    monkeypatch.setattr(home_module, "get_all_user_names", lambda: ["David"])
    monkeypatch.setattr(
        home_module,
        "get_user_by_name",
        lambda name: ("David", 5, 10, "2000-01-01", "male", None, None, None, None),
    )
    monkeypatch.setattr(home_module, "get_current_weight", lambda name: None)
    monkeypatch.setattr(home_module, "get_weight_history", lambda name: [])
    monkeypatch.setattr(ui, "get_todays_workout", lambda name: None)
    install_label_mocks(ui)

    ui.update_label()

    ui.bmi_label.setText.assert_called_once_with("No BMI data")
    ui.fat_label.setText.assert_called_once_with("Missing data for body fat calculation")
    ui.workout_label.setText.assert_called_once_with("No workout planned")


def test_connect_navigation_delegates_to_navigation_bar(ui):
    ui.navigation_bar = Mock()
    stack, home, weight, goals, insights, settings = [object() for _ in range(6)]

    ui.connect_navigation(stack, home, weight, goals, insights, settings)

    ui.navigation_bar.connect_navigation.assert_called_once_with(
        stack, home, weight, goals, insights, settings
    )


def test_on_show_event_sets_active_nav_updates_labels_and_calls_original(ui):
    event = object()
    ui.navigation_bar = Mock()
    ui.navigation_bar.overview_nav_button = object()
    ui.update_label = Mock()
    ui.original_show_event = Mock()

    ui.on_show_event(event)

    ui.navigation_bar.set_active_nav.assert_called_once_with(ui.navigation_bar.overview_nav_button)
    ui.update_label.assert_called_once_with()
    ui.original_show_event.assert_called_once_with(event)

"""Tests for widgets.weight.goal_dialog.GoalDialog."""

from __future__ import annotations

import pytest
from PySide6.QtWidgets import QDialogButtonBox, QLineEdit

from widgets.weight.goal_dialog import GoalDialog


def test_goal_dialog_prefills_current_goal_and_returns_float(qapp):
    dialog = GoalDialog(165.5)

    assert dialog.windowTitle() == "Edit Goal Weight"
    assert dialog.findChild(QLineEdit).text() == "165.5"
    assert dialog.get_goal_weight() == 165.5


def test_goal_dialog_returns_edited_float(qapp):
    dialog = GoalDialog(165.0)
    dialog.goal_input.setText("155.25")

    assert dialog.get_goal_weight() == 155.25


def test_goal_dialog_invalid_text_raises_value_error(qapp):
    dialog = GoalDialog(165.0)
    dialog.goal_input.setText("not-a-number")

    with pytest.raises(ValueError):
        dialog.get_goal_weight()


def test_goal_dialog_has_ok_and_cancel_buttons(qapp):
    dialog = GoalDialog(165.0)
    buttons = dialog.findChild(QDialogButtonBox)

    assert buttons.button(QDialogButtonBox.Ok) is not None
    assert buttons.button(QDialogButtonBox.Cancel) is not None

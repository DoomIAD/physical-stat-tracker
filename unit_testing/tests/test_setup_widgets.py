"""Smoke tests for generated setup screen widgets."""

from __future__ import annotations

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QWidget

from widgets.setup.birthdate_widget import Ui_birthdate_widget
from widgets.setup.height_widget import Ui_height_widget
from widgets.setup.name_widget import Ui_name_widget
from widgets.setup.weight_widget import Ui_weight_widget
from widgets.setup.welcome_widget import Ui_welcome_screen


def test_welcome_widget_text_and_button(qapp):
    widget = QWidget()
    ui = Ui_welcome_screen()

    ui.setupUi(widget)

    assert widget.windowTitle() == "Stat Tracker"
    assert ui.welcome_title.text() == "Welcome to Stat Tracker"
    assert ui.continue_button.text() == "Continue"


def test_name_widget_text_input_and_button(qapp):
    widget = QWidget()
    ui = Ui_name_widget()

    ui.setupUi(widget)

    assert ui.name_title.text() == "What is Your Name?"
    assert ui.name_TextEdit.placeholderText() == "John Doe"
    assert ui.name_TextEdit.maximumHeight() == 50
    assert ui.continue_button.text() == "Continue"


def test_birthdate_widget_defaults_and_range(qapp):
    widget = QWidget()
    ui = Ui_birthdate_widget()

    ui.setupUi(widget)

    assert ui.birthdate_title.text() == "When is your Birthdate?"
    assert ui.birthdate_dateEdit.displayFormat() == "MM/dd/yyyy"
    assert ui.birthdate_dateEdit.date() == QDate(1999, 9, 1)
    assert ui.birthdate_dateEdit.minimumDate() == QDate(1900, 9, 14)
    assert ui.birthdate_dateEdit.maximumDate() == QDate(2025, 12, 31)
    assert ui.continue_button.text() == "Continue"


def test_height_widget_placeholders_and_labels(qapp):
    widget = QWidget()
    ui = Ui_height_widget()

    ui.setupUi(widget)

    assert ui.height_title.text() == "How Tall are You?"
    assert ui.ft_textEdit.placeholderText() == "5"
    assert ui.in_textEdit.placeholderText() == "6"
    assert ui.ft_label.text() == "ft"
    assert ui.in_label.text() == "in"
    assert ui.continue_button.text() == "Continue"


def test_weight_widget_placeholder_label_and_button(qapp):
    widget = QWidget()
    ui = Ui_weight_widget()

    ui.setupUi(widget)

    assert ui.weight_title.text() == "How Much do You Weigh?"
    assert ui.weight_label.text() == "lb"
    assert ui.weight_textEdit.placeholderText() == "6"
    assert ui.continue_button.text() == "Continue"

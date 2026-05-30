"""Unit tests for main.MainWindow methods without booting the full UI."""

from __future__ import annotations

import datetime as dt

from PySide6 import QtWidgets
from PySide6.QtGui import QFont

import main as main_module

MainWindow = main_module.MainWindow


class FakeTextEdit:
    def __init__(self, text=""):
        self._text = text

    def toPlainText(self):
        return self._text

    def setPlainText(self, text):
        self._text = text


class FakeDate:
    def __init__(self, value="2000-01-15"):
        self.value = value

    def toString(self, fmt):
        assert fmt == "yyyy-MM-dd"
        return self.value


class FakeDateEdit:
    def __init__(self, value="2000-01-15"):
        self._date = FakeDate(value)

    def date(self):
        return self._date


class FakeStack:
    def __init__(self, index=0):
        self._index = index
        self.current_widget = None
        self.removed = []
        self.added = []

    def currentIndex(self):
        return self._index

    def setCurrentIndex(self, index):
        self._index = index

    def setCurrentWidget(self, widget):
        self.current_widget = widget

    def removeWidget(self, widget):
        self.removed.append(widget)

    def addWidget(self, widget):
        self.added.append(widget)


class FakeFontLabel:
    def __init__(self):
        self.font = None

    def setFont(self, font):
        self.font = font


def make_main_window_without_init(stack_index=0):
    window = MainWindow.__new__(MainWindow)
    window.stack = FakeStack(index=stack_index)
    window.name_ui = type("NameUi", (), {"name_TextEdit": FakeTextEdit("David")})()
    window.birthdate_ui = type("BirthdateUi", (), {"birthdate_dateEdit": FakeDateEdit("2000-01-15")})()
    window.height_ui = type(
        "HeightUi",
        (),
        {"ft_textEdit": FakeTextEdit("5"), "in_textEdit": FakeTextEdit("11")},
    )()
    window.weight_ui = type("WeightUi", (), {"weight_textEdit": FakeTextEdit("180.5")})()
    return window


def capture_warnings(monkeypatch):
    warnings = []
    monkeypatch.setattr(QtWidgets.QMessageBox, "warning", lambda *args: warnings.append(args))
    return warnings


def test_data_checking_requires_non_blank_name(monkeypatch):
    window = make_main_window_without_init(stack_index=1)
    window.name_ui.name_TextEdit.setPlainText("   ")
    warnings = capture_warnings(monkeypatch)

    assert window.data_checking() is False
    assert warnings[0][2] == "Please enter your name."


def test_data_checking_accepts_non_blank_name(monkeypatch):
    window = make_main_window_without_init(stack_index=1)
    window.name_ui.name_TextEdit.setPlainText("David")

    assert window.data_checking() is True


def test_data_checking_requires_numeric_height(monkeypatch):
    window = make_main_window_without_init(stack_index=3)
    warnings = capture_warnings(monkeypatch)

    window.height_ui.ft_textEdit.setPlainText("five")
    assert window.data_checking() is False
    assert warnings[-1][2] == "Please enter valid numbers for height."

    window.height_ui.ft_textEdit.setPlainText("5")
    window.height_ui.in_textEdit.setPlainText("11.5")
    assert window.data_checking() is False
    assert warnings[-1][2] == "Please enter valid numbers for height."


def test_data_checking_accepts_integer_height(monkeypatch):
    window = make_main_window_without_init(stack_index=3)

    assert window.data_checking() is True


def test_data_checking_requires_numeric_weight(monkeypatch):
    window = make_main_window_without_init(stack_index=4)
    warnings = capture_warnings(monkeypatch)

    for bad_value in ["180..5", "abc", ""]:
        window.weight_ui.weight_textEdit.setPlainText(bad_value)
        assert window.data_checking() is False

    assert warnings[-1][2] == "Please enter a valid number for weight."


def test_data_checking_accepts_decimal_weight(monkeypatch):
    window = make_main_window_without_init(stack_index=4)
    window.weight_ui.weight_textEdit.setPlainText("180.5")

    assert window.data_checking() is True


def test_next_screen_advances_when_data_valid(monkeypatch):
    window = make_main_window_without_init(stack_index=2)
    monkeypatch.setattr(window, "data_checking", lambda: True)

    window.next_screen()

    assert window.stack.currentIndex() == 3


def test_next_screen_stays_put_when_data_invalid(monkeypatch):
    window = make_main_window_without_init(stack_index=2)
    monkeypatch.setattr(window, "data_checking", lambda: False)

    window.next_screen()

    assert window.stack.currentIndex() == 2


def test_save_data_inserts_user_and_weight(monkeypatch):
    window = make_main_window_without_init(stack_index=4)
    inserted_users = []
    inserted_weights = []

    monkeypatch.setattr(main_module, "insert_user", lambda *args: inserted_users.append(args))
    monkeypatch.setattr(main_module, "insert_weight", lambda *args: inserted_weights.append(args))

    class FakeDateTime(dt.datetime):
        @classmethod
        def now(cls):
            return cls(2026, 5, 30, 12, 0, 0)

    monkeypatch.setattr(main_module.datetime, "datetime", FakeDateTime)

    window.save_data()

    assert inserted_users == [("David", 5, 11.0, "2000-01-15")]
    assert inserted_weights == [("David", 180.5, "2026-05-30")]


def test_save_data_skips_when_required_fields_missing(monkeypatch):
    window = make_main_window_without_init(stack_index=4)
    window.name_ui.name_TextEdit.setPlainText("")
    inserted_users = []
    inserted_weights = []
    monkeypatch.setattr(main_module, "insert_user", lambda *args: inserted_users.append(args))
    monkeypatch.setattr(main_module, "insert_weight", lambda *args: inserted_weights.append(args))

    window.save_data()

    assert inserted_users == []
    assert inserted_weights == []


def test_save_data_does_not_insert_weight_when_weight_conversion_fails(monkeypatch):
    window = make_main_window_without_init(stack_index=4)
    window.weight_ui.weight_textEdit.setPlainText("bad")
    inserted_users = []
    inserted_weights = []
    monkeypatch.setattr(main_module, "insert_user", lambda *args: inserted_users.append(args))
    monkeypatch.setattr(main_module, "insert_weight", lambda *args: inserted_weights.append(args))

    window.save_data()

    assert inserted_users == [("David", 5, 11.0, "2000-01-15")]
    assert inserted_weights == []


def test_update_fonts_sets_width_based_font_size(monkeypatch):
    window = make_main_window_without_init()
    monkeypatch.setattr(window, "width", lambda: 800)
    labels = [FakeFontLabel(), FakeFontLabel()]

    window.update_fonts(labels)

    assert all(isinstance(label.font, QFont) for label in labels)
    assert [label.font.pointSize() for label in labels] == [40, 40]


def test_finish_setup_saves_data_rebuilds_dashboard_and_goes_home(monkeypatch):
    window = make_main_window_without_init(stack_index=4)
    window.debug_widget = object()
    old_dashboard = type("OldDashboard", (), {"deleteLater": lambda self: None})()
    window.weight_dashboard_widget = old_dashboard
    window.debug_ui = type("DebugUi", (), {"connect_navigation": lambda self, **kwargs: setattr(self, "kwargs", kwargs)})()

    class FakeDashboard:
        def connect_navigation(self, **kwargs):
            self.kwargs = kwargs

    class FakeSettings:
        def __init__(self):
            self.values = {}

        def setValue(self, key, value):
            self.values[key] = value

    calls = []
    window.settings = FakeSettings()
    monkeypatch.setattr(window, "data_checking", lambda: True)
    monkeypatch.setattr(window, "save_data", lambda: calls.append("save_data"))
    monkeypatch.setattr(main_module, "create_database", lambda: calls.append("create_database"))
    monkeypatch.setattr(main_module, "Dashboard", FakeDashboard)

    window.finish_setup()

    assert calls == ["create_database", "save_data"]
    assert window.settings.values == {"setup_complete": True}
    assert window.stack.removed == [old_dashboard]
    assert isinstance(window.weight_dashboard_widget, FakeDashboard)
    assert window.stack.added == [window.weight_dashboard_widget]
    assert window.stack.current_widget is window.debug_widget


def test_finish_setup_returns_early_when_data_invalid(monkeypatch):
    window = make_main_window_without_init(stack_index=4)
    window.settings = object()
    calls = []

    monkeypatch.setattr(window, "data_checking", lambda: False)
    monkeypatch.setattr(window, "save_data", lambda: calls.append("save_data"))
    monkeypatch.setattr(main_module, "create_database", lambda: calls.append("create_database"))

    window.finish_setup()

    assert calls == []

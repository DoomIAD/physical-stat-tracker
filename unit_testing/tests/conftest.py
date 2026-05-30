"""Shared pytest fixtures for the physical-stat-tracker test suite."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest
from PySide6.QtWidgets import QApplication

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")


@pytest.fixture(autouse=True)
def isolated_runtime(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """Isolate hard-coded DB paths and QSettings side effects for every test."""
    (tmp_path / "sql").mkdir()
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("QT_QPA_PLATFORM", "offscreen")
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path / "config"))
    yield tmp_path


@pytest.fixture
def isolated_database(isolated_runtime: Path) -> Path:
    """Path to the per-test SQLite database used by production code."""
    return isolated_runtime / "sql" / "my_database.db"


@pytest.fixture(scope="session")
def qapp():
    """Create one QApplication for QWidget tests, if one does not already exist."""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


@pytest.fixture
def project_root() -> Path:
    return PROJECT_ROOT

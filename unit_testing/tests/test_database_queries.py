"""Comprehensive tests for sql.queries database helpers."""

from __future__ import annotations

import datetime as dt
import sqlite3

import pytest

from sql.queries.create_database import create_database
from sql.queries.edit_database import update_user
from sql.queries.insert_database import insert_user, insert_weight
from sql.queries.read_database import (
    get_activity_history,
    get_all_users,
    get_all_user_names,
    get_all_workout_plan_details,
    get_all_workout_plans,
    get_all_workout_week,
    get_current_weight,
    get_goal_data,
    get_user_by_name,
    get_user_workout_plan_for_day,
    get_weight_history,
    get_workout_plan_by_name,
)


def test_create_database_creates_expected_tables_and_columns(isolated_database):
    create_database()

    with sqlite3.connect(isolated_database) as conn:
        tables = {
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            ).fetchall()
        }
        columns = {
            table: [row[1] for row in conn.execute(f"PRAGMA table_info({table})")]
            for table in tables
        }

    assert {
        "users",
        "weight_history",
        "activity_history",
        "workout_plans",
        "workout_plan_details",
    }.issubset(tables)
    assert columns["users"] == [
        "username",
        "height_ft",
        "height_in",
        "birthdate",
        "gender",
        "neck_circumference",
        "waist_circumference",
        "goal",
        "start_weight",
    ]
    assert columns["weight_history"] == ["username", "date", "weight"]
    assert columns["activity_history"] == ["username", "date", "score"]
    assert columns["workout_plans"] == ["plan_name", "username", "workout_order"]
    assert columns["workout_plan_details"] == [
        "plan_name",
        "workout_name",
        "weight",
        "sets",
        "reps",
    ]


def test_insert_user_and_read_full_user_record_and_names():
    create_database()

    insert_user(
        "David",
        5,
        11.0,
        "2000-01-15",
        gender="male",
        neck_circumference=16.0,
        waist_circumference=34.0,
        goal=170.0,
        start_weight=185.0,
    )

    assert get_all_user_names() == ["David"]
    assert get_all_users() == [
        ("David", 5, 11.0, "2000-01-15", "male", 16.0, 34.0, 170.0, 185.0)
    ]
    assert get_user_by_name("David") == get_all_users()[0]
    assert get_goal_data("David") == (170.0, 185.0)


def test_duplicate_username_does_not_replace_existing_user():
    create_database()

    insert_user("David", 5, 11.0, "2000-01-15")
    insert_user("David", 6, 0.0, "1999-01-01")

    assert get_all_user_names() == ["David"]
    assert get_user_by_name("David")[1:4] == (5, 11.0, "2000-01-15")


def test_insert_weight_replaces_same_date_and_reads_current_weight():
    create_database()
    insert_user("David", 5, 11.0, "2000-01-15")

    insert_weight("David", 180.25, "2026-05-29")
    insert_weight("David", 179.75, "2026-05-30")
    insert_weight("David", 178.25, "2026-05-30")

    assert get_current_weight("David") == 178.25
    assert get_weight_history("David") == [
        ("2026-05-29", 180.25),
        ("2026-05-30", 178.25),
    ]


def test_weight_history_is_user_scoped_even_when_dates_overlap():
    """Regression test: different users should be able to log weight on the same date."""
    create_database()
    insert_user("David", 5, 11.0, "2000-01-15")
    insert_user("Alex", 5, 8.0, "2001-02-01")

    insert_weight("David", 180.0, "2026-05-30")
    insert_weight("Alex", 145.0, "2026-05-30")

    assert get_weight_history("David") == [("2026-05-30", 180.0)]
    assert get_weight_history("Alex") == [("2026-05-30", 145.0)]


def test_update_user_updates_only_provided_fields_and_goal_data():
    create_database()
    insert_user("David", 5, 11.0, "2000-01-15")

    update_user("David", goal=165.0, start_weight=185.5, gender="male")

    user = get_user_by_name("David")
    assert user[0:4] == ("David", 5, 11.0, "2000-01-15")
    assert user[4] == "male"
    assert get_goal_data("David") == (165.0, 185.5)


def test_update_user_can_update_every_editable_field():
    create_database()
    insert_user("David", 5, 11.0, "2000-01-15")

    update_user(
        "David",
        height_ft=6,
        height_in=1.5,
        birthdate="1998-12-31",
        gender="male",
        neck_circumference=15.5,
        waist_circumference=32.0,
        goal=175.0,
        start_weight=190.0,
    )

    assert get_user_by_name("David") == (
        "David",
        6,
        1.5,
        "1998-12-31",
        "male",
        15.5,
        32.0,
        175.0,
        190.0,
    )


def test_update_user_with_no_fields_is_noop(monkeypatch):
    calls = []
    monkeypatch.setattr(
        "sql.queries.edit_database.execute_query",
        lambda query, params: calls.append((query, params)),
    )

    update_user("David")

    assert calls == []


def test_workout_plan_readers_and_daily_cycle(isolated_database):
    create_database()
    insert_user("David", 5, 11.0, "2000-01-15")

    with sqlite3.connect(isolated_database) as conn:
        conn.executemany(
            "INSERT INTO workout_plans(plan_name, username, workout_order) VALUES (?, ?, ?)",
            [("Push", "David", 1), ("Pull", "David", 2), ("Legs", "David", 3)],
        )
        conn.executemany(
            "INSERT INTO workout_plan_details(plan_name, workout_name, weight, sets, reps) VALUES (?, ?, ?, ?, ?)",
            [("Push", "Bench", 135.0, 3, 8), ("Legs", "Squat", 185.0, 5, 5)],
        )

    assert get_all_workout_plans() == [
        ("Push", "David", 1),
        ("Pull", "David", 2),
        ("Legs", "David", 3),
    ]
    assert get_all_workout_plan_details() == [
        ("Push", "Bench", 135.0, 3, 8),
        ("Legs", "Squat", 185.0, 5, 5),
    ]
    assert get_user_workout_plan_for_day("David", dt.date(2026, 1, 1)) == "Push"
    assert get_user_workout_plan_for_day("David", dt.date(2026, 1, 2)) == "Pull"
    assert get_user_workout_plan_for_day("David", dt.date(2026, 1, 3)) == "Legs"
    assert get_user_workout_plan_for_day("David", dt.date(2026, 1, 4)) == "Push"
    assert get_all_workout_week(dt.date(2026, 1, 2)) == [
        ("David", 0, "Push"),
        ("David", 1, "Pull"),
        ("David", 2, "Legs"),
    ]


def test_get_workout_plan_by_name_returns_matching_plan(isolated_database):
    create_database()
    insert_user("David", 5, 11.0, "2000-01-15")
    with sqlite3.connect(isolated_database) as conn:
        conn.execute(
            "INSERT INTO workout_plans(plan_name, username, workout_order) VALUES (?, ?, ?)",
            ("Push", "David", 1),
        )

    assert get_workout_plan_by_name("Push") == ("Push", "David", 1)


def test_activity_history_builds_7_by_6_grid_with_score_buckets(
    monkeypatch,
    isolated_database,
):
    import datetime as dt
    import sqlite3
    import sql.queries.read_database as read_db

    create_database()
    insert_user("David", 5, 11.0, "2000-01-15")

    class FakeDateTime(dt.datetime):
        @classmethod
        def now(cls):
            return cls(2026, 5, 30, 12, 0, 0)

    monkeypatch.setattr(read_db.datetime, "datetime", FakeDateTime)

    with sqlite3.connect(isolated_database) as conn:
        conn.executemany(
            "INSERT INTO activity_history(username, date, score) VALUES (?, ?, ?)",
            [
                ("David", "2026-04-19", 1.0),    # grid[0][0] -> 1
                ("David", "2026-04-20", 24.0),   # grid[1][0] -> 1
                ("David", "2026-04-21", 25.0),   # grid[2][0] -> 1
                ("David", "2026-05-30", 100.0),  # grid[6][5] -> 4
            ],
        )

    grid = read_db.get_activity_history("David")

    assert len(grid) == 7
    assert all(len(row) == 6 for row in grid)
    assert grid[0][0] == 1
    assert grid[1][0] == 1
    assert grid[2][0] == 1
    assert grid[6][5] == 4


def test_read_functions_return_safe_defaults_when_database_missing():
    assert get_all_users() == []
    assert get_all_user_names() == []
    assert get_all_workout_plans() == []
    assert get_all_workout_plan_details() == []
    assert get_user_by_name("missing") is None
    assert get_user_workout_plan_for_day("missing", dt.date(2026, 1, 1)) is None
    assert get_current_weight("missing") is None
    assert get_weight_history("missing") == []
    assert get_goal_data("missing") is None
    assert get_activity_history("missing") == [[0 for _ in range(6)] for _ in range(7)]

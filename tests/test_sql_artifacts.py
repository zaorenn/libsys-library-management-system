"""Checks for SQL files shipped as project deliverables."""

from __future__ import annotations

import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def test_schema_and_report_queries_are_valid_sqlite():
    connection = sqlite3.connect(":memory:")
    try:
        connection.executescript((PROJECT_ROOT / "schema.sql").read_text(encoding="utf-8"))
        report_sql = (PROJECT_ROOT / "reports.sql").read_text(encoding="utf-8")
        statements = [statement.strip() for statement in report_sql.split(";") if statement.strip()]
        assert len(statements) == 6
        for statement in statements:
            connection.execute(statement).fetchall()
    finally:
        connection.close()

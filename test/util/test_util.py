from data_forge.util.query_builder import build_select_query
import pytest


def test_build_select_query():
    table_name = "test_table"
    columns = [{"name": "column_a"}, {"name": "column_b"}]
    source = "test_source"

    assert ((build_select_query(table_name=table_name, columns=columns, source=source))
            == "select column_a, column_b from test_table")
    assert ((build_select_query(table_name=table_name, columns=columns, source=source, format_query=True))
            == "select column_a, column_b from test_source.test_table")
from datetime import datetime

from data_forge.util.query_builder import build_select_query, latest_data_fetching_query, build_columns

table_name = "test_table"
columns = [{"name": "column_a"}, {"name": "column_b"}]
source = "test_source"
highest_mark = datetime.now()
marking_column = "test_marking_column"


def test_build_select_query():
    assert ((build_select_query(table_name=table_name, columns=columns, source=source))
            == "select column_a, column_b from test_table")
    assert ((build_select_query(table_name=table_name, columns=columns, source=source, format_query=True))
            == "select column_a, column_b from test_source.test_table")


def test_latest_data_fetching_query():
    assert (
            latest_data_fetching_query(
                table_name=table_name,
                highest_mark=highest_mark,
                columns=columns,
                source=source,
                marking_column=marking_column
            ) == f"select column_a, column_b from test_table where test_marking_column > '{highest_mark}'"
    )
    assert (
            latest_data_fetching_query(
                table_name=table_name,
                highest_mark=highest_mark,
                columns=columns,
                source=source,
                marking_column=marking_column,
                format_query=True
            ) == f"select column_a, column_b from test_source.test_table where test_marking_column > '{highest_mark}'"
    )


def test_build_columns():
    assert (
            build_columns(columns=columns) == "column_a, column_b"
    )
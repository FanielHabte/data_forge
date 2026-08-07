from datetime import datetime


def build_select_query(table_name: str, columns: list[dict], source: str, format_query: bool = False):
    columns = build_columns(columns)

    if format_query:
        return f"""select {columns} from {source}.{table_name}"""

    return f"""select {columns} from {table_name}"""


def latest_data_fetching_query(table_name: str, highest_mark: datetime, columns: list[dict], marking_column: str,
                               source: str, format_query: bool = False):
    columns = build_columns(columns)

    if format_query:
        return f"""select {columns} from {source}.{table_name} where {marking_column} > '{highest_mark}'"""

    return f"select {columns} from {table_name} where {marking_column} > '{highest_mark}'"


def build_columns(columns: list[dict]):
    column_names = []

    for column in columns:
        column_names.append(column["name"])

    return ", ".join(column_names)

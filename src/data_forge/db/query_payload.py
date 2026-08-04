from dataclasses import dataclass
from datetime import datetime

from data_forge.logging.watermark import CheckPoint
from src.data_forge.context.context import Context


@dataclass(frozen=True)
class Query:
    context: Context

    def build_select_query(self, table_name: str, source: str, merged_type: bool = False):
        columns = self._build_columns(table_name=table_name, source=source)

        if merged_type:
            return f""" select {columns} from {source}.{table_name} """

        return f""" select {columns} from {table_name} """

    def latest_data_fetching_query(self, table_name: str, source: str, water_mark: datetime, marking_column):
        columns = self._build_columns(table_name=table_name, source=source)

        return f"select {columns} from {table_name} where {marking_column} > {water_mark}"

    def _build_columns(self, table_name: str, source: str):
        columns = self.context.tables[source][table_name]
        column_names = []

        for column in columns:
            column_names.append(column["name"])

        if len(column_names) == 0:
            raise RuntimeError(f"Table {table_name} does not have columns")

        return ", ".join(column_names)

from dataclasses import dataclass

from src.data_forge.context.context import Context


@dataclass(frozen=True)
class Query:
    context: Context

    def build_select_query(self, table_name: str):
        columns = self._build_columns(table_name=table_name)
        return f""" select {columns} from {table_name} """

    def _build_columns(self, table_name: str):
        table_columns = []
        column_names = []

        for table in self.context.tables:
            if table["name"] == table_name:
                table_columns.extend(table["columns"])

        for column in table_columns:
            column_names.append(column["name"])

        if len(column_names) == 0:
            raise RuntimeError(f"Table {table_name} does not have columns")

        return ", ".join(column_names)

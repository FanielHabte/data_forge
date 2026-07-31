from dataclasses import dataclass

from src.data_forge.context.context import Context


@dataclass(frozen=True)
class Query:
    context: Context

    def build_query(self, table_name: str):
        columns = self.build_columns(table_name=table_name)
        return f""" select {columns} from {table_name} """

    def build_columns(self, table_name: str):
        for table in self.context.tables:
            if table["name"] == table_name:
                table_columns: list[dict] = table["columns"]

        column_names = [column["name"] for column in table_columns]

        return ", ".join(column_names)

from dataclasses import dataclass
from pathlib import Path

from data_forge.sales_force.auth.auth import Auth
from src.data_forge.context.context import Context
from data_forge.db.query_payload import Query
from data_forge.sales_force.sales_force import SalesForce


@dataclass(frozen=True)
class Pipeline:
    context: Context
    auth: Auth
    query: Query
    sales_force: SalesForce

    @classmethod
    def configure(cls, config_path: Path) -> "Pipeline":
        context_obj = Context.load_context_from(file_path=config_path)
        auth_obj = Auth(context=context_obj)
        query_obj = Query(context=context_obj)
        sales_force_obj = SalesForce(context=context_obj, auth=auth_obj, query=query_obj)

        return cls(
            context=context_obj,
            auth=auth_obj,
            query=query_obj,
            sales_force=sales_force_obj
        )

    def fetch_data(self, from_table: str):
        self.sales_force.fetch_data_from_table(table_name=from_table)

    def bulk_export(self, from_table: str, to_folder: Path):
        self.sales_force.request_bulk_export(table_name=from_table, folder_path=to_folder)

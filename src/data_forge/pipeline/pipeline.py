from dataclasses import dataclass
from pathlib import Path

from src.data_forge.pipeline.auth.auth import Auth
from src.data_forge.context.context import Context
from src.data_forge.db.query import Query
from src.data_forge.pipeline.sales_force.sales_force import SalesForce


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

    def run(self, table_name: str):
        self.sales_force.fetch_data_from_table(table_name)

    def bulk_export(self, from_table: str, to_folder: Path):
        self.sales_force.request_bulk_export(table_name=from_table, folder_path=to_folder)

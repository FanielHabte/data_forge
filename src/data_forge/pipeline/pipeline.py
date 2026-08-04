from dataclasses import dataclass
from pathlib import Path

from data_forge.dw.edi import Edi
from data_forge.erp.erp import Erp
from data_forge.ops.ops import Ops
from src.data_forge.context.context import Context
from data_forge.sales_force.sales_force import SalesForce


@dataclass(frozen=True)
class Pipeline:
    context: Context
    sales_force: SalesForce
    erp: Erp
    ops: Ops
    dw: Edi

    def bulk_export(self, from_table: str, to_folder: Path):
        self.sales_force.request_bulk_export(table_name=from_table, folder_path=to_folder)

    def run_daily_api_el(self):
        source = "crm"
        tables = list(self.context.tables[source].keys())

        for table in tables:
            data_stream = self.sales_force.fetch_data_from_table(table_name=table)
            self.dw.insert_dataframe(data_stream=data_stream, table_name=table, source=source)

    def run_daily_el(self, for_db: str):
        target_db: Ops | Erp = self.erp

        if for_db == "ops":
            target_db: Ops | Erp = self.ops

        tables = list(self.context.tables[target_db.source].keys())

        for table in tables:
            print(f"\nStarted processing data for table: {table}")
            data_stream = self.erp.extract_latest_data(table_name=table)
            self.dw.insert_dataframe(data_stream=data_stream, table_name=table, source=target_db.source)
            print(f"Completed loading {table}")

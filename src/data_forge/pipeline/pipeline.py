from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from data_forge.db_services.target import TargetDW
from data_forge.db_services.source import SourceDB
from src.data_forge.context.context import Context
from data_forge.sales_force.sales_force import SalesForce
from data_forge.logging.watermark import Watermark


@dataclass(frozen=True)
class Pipeline:
    context: Context
    sales_force: SalesForce
    erp: SourceDB
    ops: SourceDB
    edi: TargetDW

    def bulk_export(self, from_table: str, to_folder: Path):
        self.sales_force.request_bulk_export(table_name=from_table, folder_path=to_folder)

    def run_daily_api_el(self):
        source = "crm"
        tables = self.context.get_tables(source)

        for table in tables:
            data_stream = self.sales_force.fetch_data_from_table(table_name=table)
            self.edi.insert_dataframe(data_stream=data_stream, table_name=table, source=source)

    def run_daily_pipeline(self, run_datetime: datetime):
        db_sources = [self.erp, self.ops]
        for db_source in db_sources:
            self._read_write_tables(source_db=db_source, run_datetime=run_datetime)

    def run_erp_pipeline(self, run_datetime: datetime):
        self._read_write_tables(source_db=self.erp, run_datetime=run_datetime)

    def run_ops_pipeline(self, run_datetime: datetime):
        self._read_write_tables(source_db=self.ops, run_datetime=run_datetime)

    def _read_write_tables(self, source_db: SourceDB, run_datetime: datetime):
        tables = self.context.get_tables(source_db.source)
        for table in tables:
            print(f"Started work on table {table}")
            watermark_response = Watermark.load(table_name=table, target_dw=self.edi)
            data_stream = source_db.request_data(table_name=table, run_datetime=run_datetime, watermark_response=watermark_response)
            self.edi.insert_dataframe(data_stream=data_stream, table_name=table, source=source_db.source)
            print(f"Completed work on table <<{table}>>\n")

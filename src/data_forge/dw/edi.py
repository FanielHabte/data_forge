from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from data_forge.db.db_super_class import DWInterface
from polars.dataframe.frame import DataFrame


@dataclass
class Edi(DWInterface):

    def extract_latest_data(self, table_name: str):
        pass

    def extract_between(self, start_time: datetime, end_time: datetime, table_name: str | None = None):
        pass

    def bulk_export(self, to_folder: Path):
        pass

    def bulk_export_between(self, start_time: datetime, end_time: datetime, to_folder: Path,
                            table_name: str | None = None):
        pass

    def bulk_insert(self):
        pass

    def insert_dataframe(self, data_stream, table_name: str, source: str):
        with self.engine.connect() as conn:
            for batch_index, batch_df in enumerate(data_stream):
                batch_df.write_database(
                    table_name=f"{source}.{table_name}",
                    connection=conn,
                    engine='sqlalchemy',
                    if_table_exists='append'
                )
                print(f"Processed batch {batch_index + 1} with {len(batch_df)}")

    def merge_latest_data(self):
        pass

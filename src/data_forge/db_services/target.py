from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from data_forge.db_engine.db_super_class import DWInterface


@dataclass
class TargetDW(DWInterface):

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
        with self.db_engine.build_connection() as conn:
            print(f"EDI: built connection for: {self.db_engine.build_uri()}")
            for batch_index, batch_df in enumerate(data_stream):
                batch_df.write_database(
                    table_name=f"{source}.{table_name}",
                    connection=conn,
                    engine='sqlalchemy',
                    if_table_exists='append'
                )
                print(f"EDI: Wrote batch index of {batch_index} and {len(batch_df)} records")

    def merge_latest_data(self):
        pass

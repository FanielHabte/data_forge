from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import polars as pl

from data_forge.db_engine.db_super_class import DbInterface
from data_forge.util.query_builder import build_select_query

@dataclass
class SourceDB(DbInterface):
    source: str

    def extract_latest_data(self, table_name: str):

        sql_query = build_select_query(
            table_name=table_name,
            columns=self.context.fetch_columns(table_name, self.source),
            source=self.source
        )

        with self.engine.connect() as conn:
            df_iter = pl.read_database(
                query=sql_query,
                connection=conn,
                iter_batches=True,
                batch_size=50000
            )

            for df in df_iter:
                yield df.with_columns(
                    pl.lit(datetime.now()).alias("dw_run_timestamp")
                )

    def extract_between(self, start_time: datetime, end_time: datetime, table_name: str | None = None):
        pass

    def bulk_export(self, to_folder: Path):
        pass

    def bulk_export_between(self, start_time: datetime, end_time: datetime, to_folder: Path,
                            table_name: str | None = None):
        pass

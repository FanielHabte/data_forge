from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import polars as pl

from data_forge.db_engine.db_super_class import DbInterface
from data_forge.util.query_builder import build_select_query


@dataclass
class SourceDB(DbInterface):
    source: str

    def extract_latest_data(self, table_name: str, run_datetime: datetime):
        chuck_size = 500_000
        sql_query = build_select_query(
            table_name=table_name,
            columns=self.context.get_columns(table_name=table_name, source=self.source),
            source=self.source
        )
        print(f"{self.source}: built query: {sql_query}")

        with self.db_engine.build_connection().execution_options(stream_results=True, yield_per=chuck_size) as conn:
            print(f"{self.source}: built connection for: {self.db_engine.build_uri()}")
            df_iter = pl.read_database(
                query=sql_query,
                connection=conn,
                iter_batches=True,
                batch_size=chuck_size,
                infer_schema_length=chuck_size
            )

            for df in df_iter:
                print(f"{self.source}: read {len(df)} records")
                yield df.with_columns(
                    pl.lit(run_datetime).alias("dw_run_timestamp")
                )

    def extract_between(self, start_time: datetime, end_time: datetime, table_name: str):
        pass

    def bulk_export(self, to_folder: Path):
        pass

    def bulk_export_between(self, start_time: datetime, end_time: datetime, to_folder: Path,
                            table_name: str | None = None):
        pass

from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import text

from data_forge.db_services.target import TargetDW
import polars as pl


@dataclass
class Watermark:
    source_system: str
    table_name: str
    schema_name: str
    marking_column: str
    high_watermark: datetime
    dw_run_timestamp: datetime

    @staticmethod
    def load(target_dw: TargetDW, table_name: str) -> dict:
        sql_query = text(f"SELECT * FROM meta_data.watermarks WHERE table_name = '{table_name}'")

        with target_dw.db_engine.build_connection() as conn:
            df = pl.read_database(query=sql_query, connection=conn)
            if df.is_empty():
                print("No watermark")
                return {"is_empty": True}

            df_row = df.row(0, named=True)

            return {"is_empty": False, "wm_object": Watermark(**df_row)}

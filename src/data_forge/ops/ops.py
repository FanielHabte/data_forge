from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from data_forge.db.db_super_class import DbInterface


@dataclass
class Ops(DbInterface):

    def extract_latest_data(self):
        pass

    def extract_between(self, start_time: datetime, end_time: datetime, table_name: str | None = None):
        pass

    def bulk_export(self, to_folder: Path):
        pass

    def bulk_export_between(self, start_time: datetime, end_time: datetime, to_folder: Path,
                            table_name: str | None = None):
        pass
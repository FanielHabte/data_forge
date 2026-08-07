from dataclasses import dataclass
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path

from data_forge.context.context import Context
from data_forge.db_engine.engine import DBEngine


@dataclass
class DbInterface(ABC):
    db_engine: DBEngine
    context: Context

    @abstractmethod
    def extract_data(self, run_datetime: datetime, sql_query: str):
        pass

    @abstractmethod
    def extract_after_watermark(self, table_name: str, run_datetime: datetime, watermark):
        pass

    @abstractmethod
    def bulk_export(self, to_folder: Path):
        pass

    @abstractmethod
    def bulk_export_between(self, start_time: datetime, end_time: datetime, to_folder: Path,
                            table_name: str | None = None):
        pass


@dataclass
class DWInterface(DbInterface):

    @abstractmethod
    def bulk_insert(self):
        pass

    @abstractmethod
    def insert_dataframe(self, data_stream, table_name: str, source: str):
        pass

    @abstractmethod
    def merge_latest_data(self):
        pass

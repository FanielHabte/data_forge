from dataclasses import dataclass
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path

from sqlalchemy.engine import Engine

from data_forge.context.context import Context


@dataclass
class DbInterface(ABC):
    engine: Engine
    context: Context

    # check_point: CheckPoint

    @abstractmethod
    def extract_latest_data(self, table_name: str):
        pass

    @abstractmethod
    def extract_between(self, start_time: datetime, end_time: datetime, table_name: str | None = None):
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

from dataclasses import dataclass
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path

from sqlalchemy.engine import Engine

from data_forge.context.context import Context
from data_forge.db.query_payload import Query
from data_forge.logging.checkpoint import CheckPoint


@dataclass
class DbInterface(ABC):
    engine: Engine
    context: Context
    query: Query
    check_point: CheckPoint

    @abstractmethod
    def extract_latest_data(self):
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

    @abstractmethod
    def load(self, table_name: str | None = None):
        pass

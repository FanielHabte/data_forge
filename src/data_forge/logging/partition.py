from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class ExtractionPartition:
    partition_id: str
    airflow_run_id: str
    airflow_task_id: str

    object_name: str
    partition_field: str
    partition_start: datetime
    partition_end: datetime

    source_query: str | None = None
    expected_records: int | None = None

@dataclass
class ExtractionPartitionRepository:
    pass
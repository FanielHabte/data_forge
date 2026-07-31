from dataclasses import dataclass, field
from datetime import datetime

from src.data_forge.util.helper import utc_now


@dataclass
class BatchEvent:
    partition_id: str
    page_number: int

    records_received: int
    records_written: int
    records_rejected: int

    source_cursor: str | None = None
    next_cursor: str | None = None
    destination_uri: str | None = None

    error_type: str | None = None
    error_message: str | None = None
    created_at: datetime = field(default_factory=utc_now)

@dataclass
class BatchEventRepository:
    pass
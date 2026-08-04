from dataclasses import dataclass, field
from datetime import datetime

from src.data_forge.util.helper import utc_now


@dataclass
class Event:
    partition_id: str
    status: str
    records_received: int
    records_written: int
    records_rejected: int
    destination_uri: str | None = None
    error_type: str | None = None
    error_message: str | None = None
    created_at: datetime = field(default_factory=utc_now)

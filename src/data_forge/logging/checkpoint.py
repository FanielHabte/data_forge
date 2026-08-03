from dataclasses import dataclass, field
from datetime import datetime

from src.data_forge.util.helper import utc_now


@dataclass
class CheckPoint:
    partition_id: str
    last_committed_page: int
    records_written: int

    cursor: str | None
    high_watermark: str | None = None
    high_watermark_id: str | None = None

    destination_uri: str | None = None
    updated_at: datetime = field(default_factory=utc_now)

@dataclass
class CheckPointRepository:
    pass
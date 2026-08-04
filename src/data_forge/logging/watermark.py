from dataclasses import dataclass, field
from datetime import datetime

from src.data_forge.util.helper import utc_now


@dataclass
class Watermark:
    mark: datetime
    source: str
    table: str
    create_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

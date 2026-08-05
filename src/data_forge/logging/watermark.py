from dataclasses import dataclass, field
from datetime import datetime

from src.data_forge.util.util import utc_now


@dataclass
class Watermark:
    highest_mark: datetime
    source_name: str
    table_name: str
    column_name: str
    create_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

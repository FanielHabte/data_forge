import json
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> datetime:
    """Return a timezone-aware UTC timestamp."""
    return datetime.now(timezone.utc)


def load_json(path: Path) -> dict:
    with open(path, "r") as j_file:
        return json.load(j_file)

import json

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Context:
    base_url: str
    chunk_size: int
    client_id: str
    client_secret: str
    export_path: str
    grant_type: str
    marking_columns: dict
    tables: dict
    databases: dict

    @classmethod
    def load_context_from(cls, file_path: Path) -> "Context":
        manifest = _read_resource_file(file_path=file_path)
        return cls(**manifest)

    @classmethod
    def get_columns(cls, table_name: str, source: str) -> list[dict]:
        return cls.tables[source][table_name]

    @classmethod
    def get_tables(cls, source: str) -> list[str]:
        return list(cls.tables[source].keys())


def _read_resource_file(file_path: Path) -> dict:
    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} is not invalid file path.")

    with open(file_path, 'r') as file:
        config_data = json.load(file)

    return config_data

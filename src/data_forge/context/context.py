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
    tables: dict
    databases: dict

    @classmethod
    def load_context_from(cls, file_path: Path) -> "Context":
        manifest = _read_resource_file(file_path=file_path)
        return cls(**manifest)


def _read_resource_file(file_path: Path) -> dict:
    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} is not invalid file path.")

    with open(file_path, 'r') as file:
        config_data = json.load(file)

    return config_data

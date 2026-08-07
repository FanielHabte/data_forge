import json
from pathlib import Path


def load_json(path: Path) -> dict:
    with open(path, "r") as j_file:
        return json.load(j_file)

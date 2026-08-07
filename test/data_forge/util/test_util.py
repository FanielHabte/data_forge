from pathlib import Path

from data_forge.util.util import load_json


def test_load_json():
    path = Path(__file__).resolve().parent.parent.parent / "resources/data/test.json"
    assert (load_json(path=path) == {"name": "test"})

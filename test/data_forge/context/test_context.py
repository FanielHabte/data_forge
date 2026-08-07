import json
from pathlib import Path

from data_forge.context.context import Context


def test_context_object():
    config_path = Path(__file__).resolve().parent.parent.parent / "resources/manifest/valid_manifest.json"
    context = Context.load_context_from(file_path=config_path)

    with open(config_path, "r") as j_file:
        expected_dict = json.load(j_file)
        assert expected_dict == context.__dict__


def test_context_get_columns():
    config_path = Path(__file__).resolve().parent.parent.parent / "resources/manifest/valid_manifest.json"
    context = Context.load_context_from(file_path=config_path)

    with open(config_path, "r") as j_file:
        manifest_file = json.load(j_file)

        for source in ["crm", "erp", "ops"]:
            tables = list(manifest_file["marking_column"][source].keys())

            for table in tables:
                assert manifest_file["tables"][source][table] == context.get_columns(table_name=table, source=source)


def test_get_tables():
    config_path = Path(__file__).resolve().parent.parent.parent / "resources/manifest/valid_manifest.json"
    context = Context.load_context_from(file_path=config_path)

    with open(config_path, "r") as j_file:
        manifest_file = json.load(j_file)

        for source in ["crm", "erp", "ops"]:
            assert list(manifest_file["marking_column"][source].keys()) == context.get_tables(source=source)


def test_get_marking_column():
    config_path = Path(__file__).resolve().parent.parent.parent / "resources/manifest/valid_manifest.json"
    context = Context.load_context_from(file_path=config_path)

    with open(config_path, "r") as j_file:
        manifest_file = json.load(j_file)

        for source in ["crm", "erp", "ops"]:
            tables = list(manifest_file["marking_column"][source].keys())

            for table in tables:
                assert manifest_file["marking_column"][source][table] == context.get_marking_column(source=source,
                                                                                                    table_name=table)
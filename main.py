from pathlib import Path

from src.data_forge import Pipeline

ROOT_PATH = Path(__file__).resolve().parent
RESOURCES_FOLDER = ROOT_PATH / "src/resources"
CONFIG_PATH = RESOURCES_FOLDER / "manifest.json"
TABLE_NAME = "Opportunity"

pipeline = Pipeline.configure(config_path=CONFIG_PATH)
pipeline.bulk_export(from_table=TABLE_NAME, to_folder=RESOURCES_FOLDER)

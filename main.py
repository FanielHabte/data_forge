from pathlib import Path
from src.data_forge import Pipeline, load_json

root_path = Path(__file__).resolve().parent
config_path = root_path / "src/resources/manifest.json"
manifest = load_json(config_path)
export_path = manifest["export_path"]

pipeline = Pipeline.configure(config_path=config_path)
pipeline.bulk_export(from_table="Opportunity", to_folder=export_path)


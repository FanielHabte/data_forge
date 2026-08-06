from datetime import datetime
from pathlib import Path
from src.data_forge import Builder

root_path = Path(__file__).resolve().parent
config_path = root_path / "src/resources/manifest.json"
builder = Builder(config_path=config_path)

context = builder.context()
export_path = Path(context.export_path)

pipeline = builder.pipeline()
pipeline_start_datetime = datetime.now()

pipeline.run_daily_pipeline(run_datetime=pipeline_start_datetime)

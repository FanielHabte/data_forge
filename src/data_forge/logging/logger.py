import json
from dataclasses import dataclass
from pathlib import Path
from logging import basicConfig, getLogger, Logger, INFO

from data_forge.logging.event import Event
from datetime import datetime, timezone


@dataclass
class EventLogger:
    log_path: Path
    level: int = INFO

    def __post_init__(self):
        self.json_log_path: Path = self.log_path.with_suffix(".jsonl")

        # Configure root logger for text output
        basicConfig(
            filename=self.log_path,
            level=self.level,
            format="%(levelname)s | %(message)s"
        )
        self.logger: Logger = getLogger("data_forge.event")

    def log_event(self, event: Event, level: str = "info") -> None:
        """Logs an event both to the terminal/file logger and JSON Lines output."""
        terminal_msg = self._format_terminal(event)
        json_data = self._format_json(event)

        # 1. Log human-readable text
        log_method = getattr(self.logger, level.lower(), self.logger.info)
        log_method(terminal_msg)

        # 2. Append JSON payload (JSON Lines format)
        with open(self.json_log_path, "a", encoding="utf-8") as j_file:
            j_file.write(json.dumps(json_data) + "\n")

    @staticmethod
    def _format_terminal(event: Event) -> str:
        err = f" | ERROR: [{event.error_type}] {event.error_message}" if event.error_type else ""
        return (
            f"[{event.created_at}] "
            f"Partition: {event.partition_id:<8} | "
            f"Status: {event.status:<8} | "
            f"Recv/Rej/Writ: {event.records_received}/{event.records_rejected}/{event.records_written}"
            f"{err}"
        )

    @staticmethod
    def _format_json(event: Event) -> dict:
        log_data = {
            "timestamp": str(event.created_at),
            "partition_id": event.partition_id,
            "status": event.status,
            "metrics": {
                "records_received": event.records_received,
                "records_rejected": event.records_rejected,
                "records_written": event.records_written,
            },
        }
        if event.error_type or event.error_message:
            log_data["error"] = {
                "type": event.error_type,
                "message": event.error_message,
            }
        return log_data


if __name__ == "__main__":
    # 1. Successful Event Example
    successful_event = Event(
        partition_id="part-001",
        status="SUCCESS",
        records_received=1000,
        records_written=1000,
        records_rejected=0,
        destination_uri="s3://my-bucket/data/part-001.parquet",
        created_at=datetime.now(timezone.utc)
    )

    # 2. Failed Event Example (with error details)
    failed_event = Event(
        partition_id="part-002",
        status="FAILED",
        records_received=500,
        records_written=450,
        records_rejected=50,
        error_type="DataValidationError",
        error_message="Schema mismatch on field 'user_id'",
        created_at=datetime.now(timezone.utc)
    )
    folder_path = Path(__name__).resolve().parent.parent.parent / "resources/log"
    folder_path.mkdir(exist_ok=True, parents=True)
    logger_path = folder_path / "pipeline.log"

    logger = EventLogger(log_path=logger_path)

    # Pass events directly when logging
    logger.log_event(successful_event, level="info")
    logger.log_event(failed_event, level="error")

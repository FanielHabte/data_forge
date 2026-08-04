import logging
from dataclasses import dataclass

from pathlib import Path


@dataclass
class Log:
    config_path: Path

    def configure(self):
        logging.Logger(name=self.config_path, level=logging.DEBUG)

    def warning(self):
        pass

    def critical(self):
        pass

    def error(self):
        pass

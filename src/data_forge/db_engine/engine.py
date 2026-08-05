from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from dataclasses import dataclass
from data_forge.context.context import Context


@dataclass
class DBEngine:
    host: str
    name: str
    password: str
    port: int
    type: str
    user: str

    @classmethod
    def configure(cls, context: Context, db_name: str) -> "DBEngine":
        return cls(**context.databases[db_name])

    def build(self) -> Engine:
        # sqlalchemy syntax
        # dialect://username:password@host:port/database
        return create_engine(
            f"{self.type}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}")

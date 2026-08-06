from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, Connection

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

    def build_engine(self) -> Engine:
        return create_engine(self.build_uri())

    def build_connection(self) -> Connection:
        return self.build_engine().connect()

    def build_uri(self) -> str:
        # database uri syntax
        # dialect://username:password@host:port/database
        return f"{self.type}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    @classmethod
    def configure(cls, context: Context, db_name: str) -> "DBEngine":
        return cls(**context.databases[db_name])

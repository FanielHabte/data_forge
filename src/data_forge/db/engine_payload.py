from dataclasses import dataclass

from data_forge.context.context import Context


@dataclass(frozen=True)
class DBEnginePayload:
    host: str
    name: str
    password: str
    port: int
    type: str
    user: str

    @classmethod
    def configure(cls, context: Context, db_name: str) -> "DBEnginePayload":
        return cls(**context.databases[db_name])
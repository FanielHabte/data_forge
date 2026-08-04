from sqlalchemy import create_engine
from dataclasses import dataclass
from sqlalchemy.engine import Engine

from data_forge.db.engine_payload import DBEnginePayload


@dataclass(frozen=True)
class DBEngine:
    payload: DBEnginePayload


    def build(self) -> Engine:
        payload = self.payload

        # sqlalchemy syntax
        # dialect://username:password@host:port/database
        return create_engine(
            f"{payload.type}://{payload.user}:{payload.password}@{payload.host}:{payload.port}/{payload.name}")

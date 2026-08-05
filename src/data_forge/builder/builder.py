from dataclasses import dataclass
from pathlib import Path

from data_forge.context.context import Context
from data_forge.db_engine.engine import DBEngine
from data_forge.db_engine.engine_payload import DBEnginePayload
from data_forge.util.query_builder import Query
from data_forge.db_services.target import Edi, TargetDW
from data_forge.db_services.source import Erp, SourceDB
from data_forge.db_services.ops import Ops
from data_forge.pipeline.pipeline import Pipeline
from data_forge.sales_force.auth import Auth
from data_forge.sales_force.sales_force import SalesForce


@dataclass
class Builder:
    config_path: Path

    def context(self):
        return Context.load_context_from(file_path=self.config_path)

    def auth(self):
        return Auth(context=self.context())

    def source_db(self, db_name: str):
        return SourceDB(
            context=self.context(),
            engine=self.engine(db_name=db_name),
        )

    def target_dw(self, db_name: str):
        return TargetDW(
            context=self.context(),
            engine=self.engine(db_name=db_name),
        )

    def pipeline(self):
        return Pipeline(
            context=self.context(),
            dw=self.target_dw(db_name="analytics"),
            erp=self.source_db(db_name="erp"),
            ops=self.source_db(db_name="ops"),
            sales_force=self.salesforce()
        )

    def salesforce(self):
        return SalesForce(
            auth=self.auth(),
            context=self.context()
        )

    def engine(self, db_name):
        return DBEngine.configure(self.context(), db_name).build()

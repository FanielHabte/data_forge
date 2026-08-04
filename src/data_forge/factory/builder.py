from dataclasses import dataclass
from pathlib import Path

from data_forge.context.context import Context
from data_forge.db.engine import DBEngine
from data_forge.db.engine_payload import DBEnginePayload
from data_forge.db.query_payload import Query
from data_forge.dw.edi import Edi
from data_forge.erp.erp import Erp
from data_forge.ops.ops import Ops
from data_forge.pipeline.pipeline import Pipeline
from data_forge.sales_force.auth.auth import Auth
from data_forge.sales_force.sales_force import SalesForce

@dataclass
class Builder:
    config_path: Path

    def context(self):
        return Context.load_context_from(file_path=self.config_path)

    def auth(self):
        return Auth(context=self.context())

    def erp(self):
        return Erp(
            query=self.query(),
            context=self.context(),
            engine=self._engine(db_name="erp"),
        )

    def edi(self):
        return Edi(
            query=self.query(),
            context=self.context(),
            engine=self._engine(db_name="analytics"),
        )

    def ops(self):
        return Ops(
            query=self.query(),
            context=self.context(),
            engine=self._engine(db_name="ops"),
        )

    def pipeline(self):
        return Pipeline(
            context=self.context(),
            dw=self.edi(),
            erp=self.erp(),
            ops=self.ops(),
            sales_force=self.salesforce()
        )

    def query(self):
        return Query(context=self.context())

    def salesforce(self):
        return SalesForce(
            auth=self.auth(),
            query=self.query(),
            context=self.context()
        )

    def _engine(self, db_name):
        return DBEngine(
            payload=DBEnginePayload.configure(self.context(), db_name=db_name)
        ).build()
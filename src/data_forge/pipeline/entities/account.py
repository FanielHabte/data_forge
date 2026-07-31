from datetime import datetime
from typing import Any, Dict, List, Optional

from repository_sqlalchemy import Base, BaseRepository, transaction
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    account_number = Column(Integer, unique=True, nullable=False)
    industry = Column(String(100), nullable=False)
    account_type = Column(String(100), nullable=False)
    billing_country = Column(String(100), nullable=False)
    annual_revenue = Column(Float, nullable=False)
    number_of_employees = Column(Integer, nullable=False)
    owner_id = Column(Integer, nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    last_modified_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)


class AccountRepository(BaseRepository[Account]):
    def find_by_id(self, account_id: int) -> Optional[Account]:
        return self.session.query(self.model).filter_by(id=account_id).first()
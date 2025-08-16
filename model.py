from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserIncome(Base):
    __tablename__ = 'user_income'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    name = Column(String(length=255))
    email = Column(String(length=255))
    income = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "income": self.income,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

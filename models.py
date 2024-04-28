from sqlalchemy import Column, String, Integer
from database import Base

class LoanAbility(Base):
    __tablename__ = "abilities"

    id = Column(Integer, primary_key=True, index=True)
    loan_id = Column(String, index=True)
    user_id = Column(String, index=True)
    pokemon_ability_id = Column(Integer, index=True)
    effect = Column(String)
    language = Column(String, index=True)
    short_effect = Column(String)
    
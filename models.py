from sqlalchemy import Column, String, Integer
from database import Base

class Ability(Base):
    __tablename__ = "abilities"

    loan_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    pokemon_ability_id = Column(Integer, index=True)
    effect = Column(String)
    language = Column(String, index=True)
    short_effect = Column(String)
    
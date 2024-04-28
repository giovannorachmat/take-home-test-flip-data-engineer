import datetime as dt
import pydantic


class BaseAbility(pydantic.BaseModel):
    loan_id: str
    user_id: str
    pokemon_ability_id: int


class LoanAbility(BaseAbility):
    effect: str
    language: str
    short_effect: str

    class Config:
        from_attributes = True


class CreateLoanAbility(BaseAbility):
    pass

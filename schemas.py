import datetime as dt
import pydantic

class LoanAbility(pydantic.BaseModel):
    loan_id: str
    user_id: str
    pokemon_ability_id: int
    effect: str
    language: str
    short_effect: str

    class Config:
        from_attributes = True

class PokemonResponse(pydantic.BaseModel):
    loan_id: str
    user_id: str
    returned_entries: str
    pokemon_list: str

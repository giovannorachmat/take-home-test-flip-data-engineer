import fastapi
from fastapi import FastAPI, HTTPException
from typing import TYPE_CHECKING
import models
import requests
import schemas
import services
import sqlalchemy.orm as orm
import json
# import pydantic

# Initialize FastAPI app
app = FastAPI(title="Pokemon API", description="This is a simple test", docs_url="/")

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


# class BaseAbility(pydantic.BaseModel):
#     loan_id: str
#     user_id: str
#     pokemon_ability_id: int


# class LoanAbility(BaseAbility):
#     effect: str
#     language: str
#     short_effect: str

#     class Config:
#         from_attributes = True


# class CreateLoanAbility(BaseAbility):
#     pass


@app.post("/pokemon/", response_model=schemas.LoanAbility)
async def create_ability(
    # pokemon_ability_id: int,
    loan_ability: schemas.CreateLoanAbility,
    db: orm.Session = fastapi.Depends(services.get_db),
):

    url = "https://pokeapi.co/api/v2/ability/150"

    # Make request to PokeAPI
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail="Pokémon ability not found"
        )

    # Normalize effect entries
    data = response.json()
    effect_entries = data["effect_entries"]
    for entry in effect_entries:
        loan_ability = schemas.LoanAbility(
            loan_id = "9594641568",
            user_id = "5199434",
            pokemon_ability_id = 150,
            effect=json.dumps(entry["effect"]),
            language=json.dumps(entry["language"]),
            short_effect=json.dumps(entry["short_effect"]),
        )

    return await services.create_ability(loan_ability=loan_ability, db=db)

import fastapi
from fastapi import FastAPI, HTTPException
from typing import TYPE_CHECKING

import requests
import schemas
import services
import sqlalchemy.orm as orm
import models
import json

# Initialize FastAPI app
app = FastAPI(title="Pokemon API", description="This is a simple test", docs_url="/")

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


@app.post("/pokemon/", response_model=schemas.LoanAbility)
async def create_ability(
    loan_id: str,
    user_id: str,
    pokemon_ability_id: int,
    db: orm.Session = fastapi.Depends(services.get_db),
):
    url = f"https://pokeapi.co/api/v2/ability/{pokemon_ability_id}"

    # Make request to PokeAPI
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail="Pokémon ability not found"
        )

    # Normalize effect entries
    data = response.json()
    # effect_entries = data["effect_entries"]
    for entry in data["effect_entries"]:
        language = entry['language']['name']
        effect = entry['effect']
        short_effect = entry['short_effect']
    
    loan_ability = models.LoanAbility(
        loan_id=loan_id,
        user_id=user_id,
        pokemon_ability_id=pokemon_ability_id,
        effect=str(effect),
        language=str(language),
        short_effect=str(short_effect),
    )

    db.add(loan_ability)
    db.commit()
    db.refresh(loan_ability)

    return loan_ability

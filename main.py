import fastapi
from fastapi import FastAPI, HTTPException
from typing import TYPE_CHECKING, List, Dict

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


@app.post("/pokemon/", response_model=List[schemas.LoanAbility])
async def insert_loan_abilities(
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
    effect_entries = data.get("effect_entries", [])

    loan_abilities = []
    for entry in effect_entries:
        language = entry["language"]["name"]
        effect = entry["effect"]
        short_effect = entry["short_effect"]

        loan_ability = models.LoanAbility(
            loan_id=loan_id,
            user_id=user_id,
            pokemon_ability_id=pokemon_ability_id,
            effect=str(effect),
            language=str(language),
            short_effect=str(short_effect),
        )
        loan_abilities.append(loan_ability)

    db.add_all(loan_abilities)
    db.commit()

    return loan_abilities


@app.get("/pokemon/")
async def get_loan_abilities(
    loan_id: str,
    user_id: str,
    pokemon_ability_id: int,
    db: orm.Session = fastapi.Depends(services.get_db),
):
    # Retrieve loan and user details from the database
    loan_data = db.query(models.LoanAbility.loan_id).filter_by(loan_id=loan_id).all()
    user_data = db.query(models.LoanAbility.user_id).filter_by(user_id=user_id).all()
    pokemon_ability_data = (
        db.query(models.LoanAbility.pokemon_ability_id)
        .filter_by(pokemon_ability_id=pokemon_ability_id)
        .all()
    )
    language_effect_data = (
        db.query(
            models.LoanAbility.language,
            models.LoanAbility.effect,
            models.LoanAbility.short_effect,
        )
        .filter_by(
            loan_id=loan_id, user_id=user_id, pokemon_ability_id=pokemon_ability_id
        )
        .all()
    )
    if not loan_data:
        raise HTTPException(status_code=404, detail="loan_id not found")
    elif not user_data:
        raise HTTPException(status_code=404, detail="user_id not found")
    elif not pokemon_ability_data:
        raise HTTPException(status_code=404, detail="pokemon_ability_id not found")

    # Retrieve language, effect, and short effect from the database

    returned_entries = []
    for entry in language_effect_data:
        returned_entries.append(
            {
                "language": entry.language,
                "effect": entry.effect,
                "short_effect": entry.short_effect,
            }
        )
    url = f"https://pokeapi.co/api/v2/ability/{pokemon_ability_id}"

    # Make request to PokeAPI
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail="Pokémon ability not found"
        )

    # Normalize effect entries
    data = response.json()
    pokemon_list = [data["pokemon"][0]["pokemon"]["name"]]

    response_data = {
        "loan_id": loan_id,
        "user_id": user_id,
        "returned_entries": returned_entries,
        "pokemon_list": pokemon_list,
    }

    if not response_data:
        raise HTTPException(status_code=404, detail="loan_id or user_id not found")

    return response_data
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Annotated
import requests
# import models
# from database import engine, SessionLocal

# Initialize FastAPI app
app = FastAPI(
    title="Pokemon API",
    description="This is a simple test",
    docs_url="/"
)
# models.Base.metadata.create_all(bind=engine)

# Pydantic model for input JSON
class PokemonRequest(BaseModel):
    pokemon_ability_id: int


# Pydantic model for normalized effect entries
class EffectEntry(BaseModel):
    short_effect: str


# Route to receive input JSON
@app.get("/pokemon_ability/")
async def get_pokemon_ability(request_data: PokemonRequest):
    pokemon_ability_id = request_data.pokemon_ability_id
    url = f"https://pokeapi.co/api/v2/ability/{pokemon_ability_id}"

    # Make request to PokeAPI
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail="Pokémon ability not found"
        )

    # Normalize effect entries
    data = response.json()
    effect_entries = data["effect_entries"]
    normalized_short_effect_effect_entries = []
    for entry in effect_entries:
        normalized_short_effect_effect_entries.append(
            {"short_effect": entry["short_effect"]}
        )
    
    return data

# @app.post("/pokemon/")
# async def post_pokemon_ability(request_data: PokemonRequest):
#     pokemon_ability_id = request_data.pokemon_ability_id
#     url = f"https://pokeapi.co/api/v2/ability/{pokemon_ability_id}"

#     # Make request to PokeAPI
#     response = requests.get(url)
#     if response.status_code != 200:
#         raise HTTPException(
#             status_code=response.status_code, detail="Pokémon ability not found"
#         )

#     # Normalize effect entries
#     data = response.json()
#     effect_entries = data["effect_entries"]
#     normalized_short_effect_effect_entries = []
#     for entry in effect_entries:
#         normalized_short_effect_effect_entries.append(
#             {"short_effect": entry["short_effect"]}
#         )

# # Store normalized effect entries in PostgreSQL
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#         # ability = Ability(name=data["name"], effect=str(normalized_effect_entries))
#         # db.add(ability)
#         # db.commit()
#     except Exception as e:
#         db.rollback()
#         raise HTTPException(
#             status_code=500, detail="Error occurred while saving data to database"
#         )
#     finally:
#         db.close()

from fastapi import FastAPI
import requests

# Initialize FastAPI app
app = FastAPI()

@app.get("/pokemon/")
async def get_pokemon_ability():
    pokemon_ability_id = 150
    url = f"https://pokeapi.co/api/v2/ability/{pokemon_ability_id}"
    response = requests.get(url)
    return response.json()


import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '92b251c8438c9aa05bc3c7cefd7cfc78'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_pokemon = {
    "name": "krasava",
    "photo_id": 12
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemon)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_name = {
    "pokemon_id": pokemon_id,
    "name": "chel",
    "photo_id": 2
}

body_pokeboll = {
    "pokemon_id": pokemon_id
}

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)

response_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeboll)
print(response_pokeboll.text)

import requests
import random

pokemon_id = random.choice(range(1,152))

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
# print(response.content)
pokemon_data = response.json() #json converts into one big python dictionary

print(f"You got pokemon number {pokemon_data['id']},{pokemon_data['name'].capitalize()}")
print(f"Height: {pokemon_data['height']} - Weight: {pokemon_data['weight']}")

pokemon_types =[]
for type_data in pokemon_data['types']:
    print(type_data['type']['name'])
    pokemon_types.append(type_data['type']['name'])
print(f"Type(s): {' and '.join(pokemon_types)}") #joins items in a list

pokemon_abilities = []
for ability_data in pokemon_data['abilities']:
    pokemon_abilities.append(ability_data['ability']['name'])

print(f"Abilities: {', '.join(pokemon_abilities)}")
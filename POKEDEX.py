
# Este código en Python implementa una sencilla aplicación de Pokédex que consulta la API de Pokémon (https://pokeapi.co/) para obtener información sobre un 
# Pokémon específico, la muestra en la consola y guarda los datos en un archivo JSON

import requests
import os
import json


# Construye la URL de la API de Pokémon con el nombre del Pokémon proporcionado.
# Realiza una solicitud GET a la API y verifica si la respuesta es exitosa (código de estado 200).
# Devuelve los datos del Pokémon en formato JSON si la respuesta es exitosa; de lo contrario, devuelve None.

def buscar_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

# Define una lista de atributos que se desean extraer del diccionario de datos del Pokémon.
# Utiliza una comprensión de diccionario para construir un nuevo diccionario llamado datos, extrayendo la información específica de pokemon_data. Además, maneja el caso en que algunos valores pueden ser diccionarios anidados.
# Imprime la información formateada del Pokémon.

def mostrar_informacion(pokemon_data):
    imagen_url = pokemon_data['sprites']['front_default']
    atributos = ['sprites/front_default', 'weight', 'height', 'moves', 'abilities', 'types']
    datos = {atributo.split('/')[0]: pokemon_data.get(atributo.split('/')[0]) 
             if isinstance(pokemon_data.get(atributo.split('/')[0]), dict) 
             else pokemon_data.get(atributo.split('/')[0]) for atributo in atributos}
   

    print(f"Imagen del Pokémon: {imagen_url}")
    print('--------------------------------------------------------------------------------------------------------------------------------------')
    print(f"Peso: {datos['weight']}")
    print('--------------------------------------------------------------------------------------------------------------------------------------')
    print(f"Altura: {datos['height']}")
    print('--------------------------------------------------------------------------------------------------------------------------------------')
    print(f"Movimientos: {', '.join(move['move']['name'] for move in datos['moves'])}")
    print('--------------------------------------------------------------------------------------------------------------------------------------')
    print(f"Habilidades: {', '.join(ability['ability']['name'] for ability in datos['abilities'])}")
    print('--------------------------------------------------------------------------------------------------------------------------------------')
    print(f"Tipos: {', '.join(type['type']['name'] for type in datos['types'])}")
    print('--------------------------------------------------------------------------------------------------------------------------------------')

    return datos

# Construye la ruta del archivo JSON utilizando el nombre del Pokémon y lo guarda en la carpeta "pokedex".
# Crea la carpeta "pokedex" si no existe.
# Abre el archivo en modo escritura y guarda la información en formato JSON con sangría de 2 espacios.

def guardar_en_json(nombre_pokemon, data):
    ruta_archivo = os.path.join('pokedex', f'{nombre_pokemon.lower()}.json')
    os.makedirs('pokedex', exist_ok=True)

    with open(ruta_archivo, 'w') as archivo:
        json.dump(data, archivo, indent=2)


# Solicita al usuario que introduzca el nombre del Pokémon.
# Llama a la función buscar_pokemon para obtener datos del Pokémon.
# Si se obtienen datos, llama a mostrar_informacion y guardar_en_json.
if __name__ == "__main__":
    nombre_pokemon = input("Introduce el nombre del Pokémon: ")
    
    pokemon_data = buscar_pokemon(nombre_pokemon)

    if pokemon_data:
        informacion = mostrar_informacion(pokemon_data)
        guardar_en_json(nombre_pokemon, informacion)

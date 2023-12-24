# HUGO SAIDA TAVIRAS PARRA 010609124


# Este código en Python implementa una sencilla aplicación de Pokédex que consulta la API de Pokémon (https://pokeapi.co/) para obtener información sobre un 
# Pokémon específico, la muestra en la consola y guarda los datos en un archivo JSON

import requests
import os
import json



# se crea la funcion donde se crea la url con el nombre del pokemon que se solicito, solicita los datos a la API y en caso de ser exitosa muestra los datos
# en caso contrario devuelve 'none'

def buscar_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None


# esta funcion crea una lista donde muestran los datos que se desean extraer del diccionario de datos pokemon y crea la variables que se mostraran a continuacion 
# en la misma funcion donde recibira los datos del pokemon que se elija y los mostrara en pantalla ya separados.

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

# esta funcion crea la ruta donde se guardara el archivo JSON usando el nombre del pokemon y guardandolo en una carpeta que se nombra 'POKEDEX' 

def guardar_en_json(nombre_pokemon, data):
    ruta_archivo = os.path.join('pokedex', f'{nombre_pokemon.lower()}.json')
    os.makedirs('pokedex', exist_ok=True)

    with open(ruta_archivo, 'w') as archivo:
        json.dump(data, archivo, indent=2)


# Solicita el nombre del Pokémon y llama a las demas funciones donde se obtienen los datos del pokemon y donde se muestran los datos en pantalla para al final 
# crear y guardar el archivo JSON
if __name__ == "__main__":
    nombre_pokemon = input("Introduce el nombre del Pokémon: ")
    
    pokemon_data = buscar_pokemon(nombre_pokemon)

    if pokemon_data:
        informacion = mostrar_informacion(pokemon_data)
        guardar_en_json(nombre_pokemon, informacion)

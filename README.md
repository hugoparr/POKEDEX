![image](https://github.com/hugoparr/POKEDEX/assets/145738985/6e3c9c6e-ed66-49db-91cd-314dcaa8318c)

Para poder hacer que el programa funcione se necesitan las bibliotecas 

--requests:
Utilizada para realizar solicitudes HTTP a la API de Pokémon.
Puedes instalarla usando el siguiente comando en tu terminal o símbolo del sistema:
'pip install requests'

--json:
Incluida en la biblioteca estándar de Python, se utiliza para trabajar con datos en formato JSON.
--os:
También parte de la biblioteca estándar de Python, se utiliza para operaciones relacionadas con el sistema operativo, como crear directorios y manejar rutas de archivos.
No es necesario instalarla por separado, ya que es parte de la biblioteca estándar de Python.

Al estudiar este código, puedes obtener una comprensión más profunda de cómo funciona Python en el contexto del desarrollo de software, especialmente en lo que respecta a la manipulación de datos, interacciones con APIs y manejo de archivos.

--buscar_pokemon(nombre_pokemon):
Construye la URL de la API con el nombre del Pokémon y realiza una solicitud GET.
Devuelve los datos del Pokémon si la solicitud es exitosa, de lo contrario, retorna None.

--mostrar_informacion(pokemon_data):
Define una lista de atributos deseados del Pokémon.
Utiliza comprensiones de diccionario para extraer y formatear la información del Pokémon.
Imprime la información formateada en la consola.

--guardar_en_json(nombre_pokemon, data):
Construye la ruta del archivo JSON utilizando el nombre del Pokémon.
Crea la carpeta "pokedex" si no existe.
Guarda la información del Pokémon en un archivo JSON en la carpeta "pokedex".

--Bloque Principal (`if name == "main":):
Solicita al usuario que introduzca el nombre del Pokémon.
Llama a buscar_pokemon para obtener datos del Pokémon.
Si se obtienen datos, llama a mostrar_informacion y guardar_en_json.

El código utiliza la biblioteca requests para realizar solicitudes HTTP a la API de Pokémon y maneja datos en formato JSON. Además, organiza la información y la presenta de manera legible en la consola.

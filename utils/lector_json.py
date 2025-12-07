import json
from pathlib import Path

def leer_datos_productos(ruta_archivo):
    """
    Lee el JSON y devuelve la lista completa de diccionarios 
    (con nombre, precio y descripción).
    """
    ruta = Path(ruta_archivo)
    with open(ruta, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    return datos
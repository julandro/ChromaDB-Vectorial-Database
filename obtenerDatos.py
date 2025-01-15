import json


def obtenerDatos():
    with open('./data/datos.json', 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

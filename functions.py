import json
import streamlit as st


def obtenerDatos():
    with open('./datos.json', 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

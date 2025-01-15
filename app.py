import chromadb
import streamlit as st
import json
from obtenerDatos import obtenerDatos
from streamlit_card import card

marcas = ['Dodge', 'Chevrolet', 'Lotus', 'Porshe', 'Alfa Romeo', 'Ford', 'Toyota', 'Honda', 'Ferrari',
          'Lamborghini', 'BMW', 'Nissan', 'Subaru', 'Mercedes-Benz', 'McLaren', 'Fiat', 'Audi', 'Jaguar']

if 'resultado' not in st.session_state:
    st.session_state.resultado = []

client = chromadb.PersistentClient(path="DB-chroma")

collection = client.get_or_create_collection("Carros")


carrosData = obtenerDatos()

idCount = 0
for carro in carrosData:
    collection.upsert(
        documents=carro.get('descripcion', 'Descripción no Disponible'),
        metadatas={
            "marca": carro.get('marca', 'Marca no Disponible'),
            "modelo": carro.get('modelo', 'Modelo no disponible'),
            "descripcion": carro.get('descripcion', 'Descripción no Disponible'),
            "motor": carro.get('motor', 'Motor no disponible'),
            "potencia": carro.get('potencia', 'Potencia no disponible'),
            "transmision": carro.get('transmision', 'Transmision no disponible'),
            "traccion": carro.get('traccion', 'Traccion no disponible'),
            "asientos": carro.get('asientos', 'Asientos no disponibles'),
            "velocidad_maxima": carro.get('velocidad_maxima', 'Velocidad maxima no disponible'),
            "pais_origen": carro.get('pais_origen', 'Pais de origen no disponible'),
            "imagen_url": carro.get('imagen_url', 'imagen no disponible'),
            "precio": carro.get('precio', 'precio no disponible')
        },
        ids=f'{carro.get("marca#", "nd#")}{idCount}'
    )
    idCount += 1

st.title("Testing Chroma DB - Vectorial")
st.subheader("Busca tu carro ideal")
with st.form("my_form"):
    potencia = st.slider("Potencia", 10, 1000)

    precio = st.number_input("Precio")

    selectMarca = st.pills("Marcas de Carros", marcas, selection_mode="single")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Buscar", use_container_width=True)
    if submitted:
        datos = collection.get()
        metadatas = datos.get('metadatas', [])
        resultados_filtrados = []
        for metadata in metadatas:
            if (
                (not potencia or metadata.get("potencia", float("inf")) <= potencia) and
                (not precio or metadata.get("precio", float("inf")) <= precio) and
                (not selectMarca or metadata.get("marca") == selectMarca)
            ):
                st.session_state['resultado'] = resultados_filtrados
                resultados_filtrados.append(metadata)
            else:
                st.session_state['resultado'] = resultados_filtrados


# Mostrar resultados en Streamlit
if st.session_state['resultado']:
    st.write("Resultados encontrados:")
    for result in st.session_state['resultado']:
        card(
            image=result.get(
                "imagen_url", "https://static.vecteezy.com/system/resources/previews/004/639/366/non_2x/error-404-not-found-text-design-vector.jpg"),
            title=result.get("marca", "Marca no disponible"),
            text=(result.get("modelo", "Modelo no disponible"),
                  f'${result.get("precio", "Precio no Disponible")}'),
            on_click=lambda: st.write(
                f"{result.get('descripcion', 'Descripción no Disponible')}"),
        )
else:
    st.write("No se encontraron resultados.")

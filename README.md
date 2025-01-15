# Proyecto Testing-ChromaDB

#### Vista Previa

![Vista previa del proyecto](./assets/img/proyectoPreview.png)

## Descripción

Este es un aplicativo web sencillo en el cual testeo ChromaDB creando un cliente Persistente, lo cual crea un db local y luego le paso una data `(./data/datos.json)` con información sobre algunos autos para luego proceder a hacer un filtro de estos datos

---

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Créditos](#créditos)
- [Recursos y Enlaces Adicionales](#recursos-y-enlaces-adicionales)

---

### Requisitos Previos

- **Python**
  Tener instalado `Python` en su versión `3.11.9`

- **Git** _(opcional)_
  Tener instalado `Git` para la clonación del proyecto

---

## Instalación

Sigue los pasos a continuación para configurar el proyecto en tu entorno local:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/julandro/ChromaDB-Vectorial-Database.git
   ```
2. **Navega al directorio del proyecto:**

   hasta el nivel de app.py

   ```bash
   cd proyecto
   ```

3. **Crea y Activa un entorno virtual:**

   - Con `python` en la terminal:

     ```bash
     python -m venv venv
     ```

   - Luego `Activalo`:

     ```bash
     venv/Scripts/activate
     ```

4. **Instala las dependencias o modulos del proyecto:**
   - Con `pip`:
     ```bash
     pip install -r requirements.txt
     ```

---

## Uso

Una vez instalado y estando en el entorno virtual puedes ejecutar el proyecto:

- **Ejecución:**
  ```bash
  streamlit run ./app.py
  ```

### Ejemplos de Uso

![1](./assets/img/img3.png)

![2](./assets/img/img4.png)

---

## Características

#### Características generales

- **[Filtrado de datos Multiple]:** Se obtienen los datos a través:
  ![](./assets/img/img1.png)
  lo cual no es optimo ya que consume mas al traer todos los datos.
  Ya con los datos a nuestra disposición, se procede a crear los filtros.
  ![](./assets/img/img2.png)

---

## Créditos

- **Autor:** Julian Alejandro Camacho Mendoza
- **Contacto:**
  - **Correo:** julandro.mza@gmail
  - **Cel:** 323 2304966
  - **GitHub:** [julandro](https://github.com/julandro)

---

## Recursos y Enlaces Adicionales

- [Streamlit Documentacion](https://docs.streamlit.io/)
- [ChromaDB Introducción`](./ChromaDB-introduction/README.md)
- [ChromaDB Documentación Oficial](https://docs.trychroma.com/docs/overview/introduction)

# Base de Datos Vectorial con ChromaDB (Open Source)

![Chroma](https://docs.trychroma.com/computer.svg)

Chroma es una base de datos vectorial diseñada para almacenar y consultar grandes cantidades de datos en formato vectorial. Está optimizada para tareas que requieren similitud de vectores, como búsquedas de similitudes y almacenamiento de embeddings. Este README describe cómo configurar y usar ChromaDB para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una colección de datos.

#### ¿Qué son los Embeddings?

Los embeddings son representaciones vectoriales de datos (como texto, imágenes, etc.) que permiten realizar comparaciones eficientes de similitud. En Chroma, los embeddings se generan automáticamente cuando se añaden documentos a la colección. Si ya tienes embeddings pre-generados, puedes incluirlos directamente al agregar o actualizar los documentos.

Chroma utiliza estas representaciones vectoriales para realizar búsquedas basadas en similitud. Esto significa que, cuando se consulta la base de datos, se devuelve el documento que es más similar al vector de consulta proporcionado.

## Métodos de Consulta con Chroma

### 1. Crear o Acceder a una Colección

Para acceder a una colección existente o crear una nueva si no existe, utilizamos el siguiente método:

```python
# Accede a la colección o crea una nueva si no existe
collection = client.get_or_create_collection(name="test")
```

Descripción: Si la colección con el nombre "test" ya existe, ChromaDB la devuelve. Si no, la crea automáticamente.

---

### 2. Insertar Datos en la Colección

Para insertar datos (documentos, embeddings y metadatos) en la colección:

```python

collection.add(
    documents=["lorem ipsum...", "doc2", "doc3", ...],  # Los textos o documentos que deseas almacenar
    metadatas=[{"chapter": "3", "verse": "16"}, {"chapter": "3", "verse": "5"}, {"chapter": "29", "verse": "11"}, ...],  # Metadatos asociados a cada documento
    ids=["id1", "id2", "id3", ...]  # Identificadores únicos para cada documento
)

```

**Descripción:** Agrega una lista de documentos, sus metadatos y un identificador único para cada uno de ellos.
**Parámetros:**

- **documents:** Lista de textos o documentos que se agregarán a la colección.
- **metadatas:** Lista de metadatos relacionados con cada documento, útil para realizar consultas más específicas.
- **ids:** Lista de identificadores únicos para cada documento.

---

### 3. Actualizar Datos en la Colección

Si deseas actualizar los datos (incluso agregar nuevos si no existen), utiliza el siguiente método:

```py
collection.update(
    ids=["id1", "id2", "id3", ...],  # IDs de los documentos que deseas actualizar
    embeddings=[[1.1, 2.3, 3.2], [4.5, 6.9, 4.4], [1.1, 2.3, 3.2], ...],  # Nuevos embeddings para los documentos
    metadatas=[{"chapter": "3", "verse": "16"}, {"chapter": "3", "verse": "5"}, {"chapter": "29", "verse": "11"}, ...],  # Nuevos metadatos
    documents=["doc1", "doc2", "doc3", ...],  # Nuevos documentos
)
```

**Descripción:** Actualiza documentos existentes o agrega nuevos documentos si no están presentes.

**Parámetros:**

- **ids:** Lista de IDs de los documentos que deseas actualizar.
- **embeddings:** Nuevos embeddings que deseas asociar con los documentos.
- **metadatas:** Nuevos metadatos relacionados con los documentos.
- **documents:** Nuevos documentos de texto.

**Nota:** El método upsert permite agregar nuevos datos si no existen, o actualizar los existentes.

---

### 4. Eliminar Datos de la Colección

Si deseas eliminar datos específicos de la colección según su ID o mediante filtros, usa este método:

```py
collection.delete(
    ids=["id1", "id2", "id3", ...],  # IDs de los documentos que deseas eliminar
    where={"chapter": "20"}  # Filtro opcional para eliminar documentos que coincidan con los metadatos
)
```

**Descripción:** Elimina los documentos especificados por sus IDs o mediante un filtro de metadatos.
**Parámetros:**

- **ids:** Lista de IDs de los documentos que deseas eliminar.
- **where:** (Opcional) Filtro de metadatos para eliminar documentos que coincidan con la condición proporcionada.

---

### Resumen de Funcionalidades

Crear o acceder a una colección: `client.get_or_create_collection(name="nombre_de_colección")`
Insertar datos:` collection.add(documents=..., metadatas=..., ids=...)`
Actualizar datos: `collection.update(ids=..., embeddings=..., metadatas=..., documents=...)`
Eliminar datos: `collection.delete(ids=..., where=...)`

---

### Consideraciones Importantes

- **Embeddings:** Si deseas realizar consultas basadas en similitud, los documentos deben estar representados como embeddings (vectores numéricos). Chroma te permite almacenar y consultar estos vectores de manera eficiente.
- **Metadatos:** Los metadatos asociados a cada documento te permiten realizar consultas avanzadas y filtradas, lo que es útil para obtener resultados más específicos.
- **ID único:** Cada documento debe tener un ID único que lo identifique dentro de la colección, lo que facilita la actualización y eliminación de datos.

---

## Créditos

- **Autor:** Julian Alejandro Camacho Mendoza
- **Contacto:**
  - **Correo:** julandro.mza@gmail
  - **Cel:** 323 2304966
  - **GitHub:** [julandro](https://github.com/julandro)

---

## Recursos y Enlaces Adicionales

- [ChromaDB Documentacion](https://docs.trychroma.com/docs/overview/introduction)

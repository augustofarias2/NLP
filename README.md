## NLP: Trabajo Práctico Final - Procesamiento del Lenguaje Natural
<p align="center">
  <img src="https://github.com/augustofarias2/NLP/blob/main/Images/welcome.png" alt="welcome">
  <img src="https://github.com/augustofarias2/NLP/blob/main/Images/ask.png" alt="ask">
</p>

## Introducción
El objetivo de este trabajo fue desarrollar un chatbot especializado en la ciudad de Rosario utilizando la técnica RAG (Retrieval Augmented Generation). El chatbot está diseñado para proporcionar información relevante sobre la ciudad, su historia y actividades disponibles.

## Instrucciones para Reproducir el Proyecto

### Clonar el Repositorio
Para comenzar, clona el repositorio desde GitHub utilizando el siguiente comando:

```bash
git clone https://github.com/augustofarias2/NLP.git
```

### Crear un Entorno Virtual (venv)
Es recomendable crear un entorno virtual para este proyecto. Desde el directorio del proyecto, ejecuta el siguiente comando para crear un nuevo entorno virtual llamado `env`:

```bash
python -m venv env
```
### Activa el entorno virtual
```bash
source env\Scripts\activate
```
### Instala dependencias
```bash
pip install -r requirements.txt
```
### Ejecuta la app
```bash
chainlit run app_chainlit.py -w
```

## Procedimiento de Trabajo
<p align="center">
  <img src="https://github.com/augustofarias2/NLP/blob/main/Images/esquema.png" alt="esquema">
</p>

### 1. Obtención de Documentos PDF
Se recopilaron documentos PDF con información relevante sobre la ciudad de Rosario y diversos temas históricos a través de fuentes confiables en línea.

### 2. Extracción de Texto y Generación de Embeddings
El texto fue extraído de los archivos PDF y se generaron embeddings utilizando técnicas de procesamiento de lenguaje natural. Estos embeddings representan la información textual en vectores numéricos.

- Archivo: `create_db.py`

### 3. Almacenamiento de Embeddings en una Base de Datos Vectorial
Los embeddings fueron almacenados en una base de datos vectorial para su posterior acceso y consulta. En este trabajo, se utilizó ChromaDB para el almacenamiento de embeddings.

- Archivo: `create_db.py`

### 4. Creación de una Base de Datos de Grafos
Se creó una base de datos de grafos para alojar información sobre diversos personajes históricos de la ciudad de Rosario. Esta base de datos incluye atributos como sexo, edad, rama en la que se destacaron, nombre y estado de vida.

- Archivo: `create_base_grafos.py`

### 5. Creación de un Archivo CSV
Se creó un archivo CSV que contiene información tabular sobre actividades disponibles en la ciudad de Rosario. Esta información está organizada en columnas que incluyen ID, lugar, descripción y ubicación de las actividades.

- Archivo: `create_csv.py`

### 6. Desarrollo de un Clasificador
Se desarrolló un clasificador para clasificar las preguntas realizadas por los usuarios y determinar la fuente de información adecuada para proporcionar respuestas precisas. 

- Archivo: `create_clasificador.py`

### 7. Importación de un Modelo de Lenguaje de Gran Escala (LLM)
Se importó un modelo de lenguaje de gran escala (LLM) en este caso utilizamos Llama. Se configuró un prompt específico para generar respuestas coherentes y relevantes.

- Archivo: `create_functions.py`

### 8. Creación de una Interfaz de Usuario (UI)
Se desarrolló una interfaz de usuario utilizando la biblioteca Chainlit. Los usuarios pueden interactuar con el chatbot iniciando sesión en la pantalla inicial y realizando consultas sobre la ciudad de Rosario. El chatbot realiza una serie de pasos descritos anteriormente para proporcionar respuestas basadas en la clasificación de la pregunta.

- Archivos: `chainlit.md` y `app_chainlit.py`

## Conclusiones
El desarrollo de este chatbot especializado en la ciudad de Rosario representa un paso importante en la utilización de técnicas de procesamiento del lenguaje natural para proporcionar información útil y accesible a los usuarios. La combinación de extracción de texto, generación de embeddings, clasificación de preguntas y generación de respuestas ha demostrado ser efectiva para crear un sistema de asistente virtual capaz de responder preguntas sobre la historia, actividades y personajes de la ciudad.

## Futuras Direcciones
Para futuras investigaciones, se podrían explorar nuevas fuentes de información, mejorar la precisión del clasificador y expandir las capacidades de conversación del chatbot. Además, se podría considerar la integración de tecnologías emergentes, como modelos de lenguaje más avanzados y técnicas de generación de texto más sofisticadas, para mejorar aún más la experiencia del usuario.

<p align="center">
  <img src="https://github.com/augustofarias2/NLP/blob/main/Images/ROSARIO-LUGARES-CONOCER.jpg" alt="Rosario">
</p>
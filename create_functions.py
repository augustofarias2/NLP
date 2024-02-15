from langchain_community.embeddings import HuggingFaceEmbeddings
from llama_index import VectorStoreIndex
from llama_index.embeddings import LangchainEmbedding
from llama_index import ServiceContext
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores import ChromaVectorStore


from jinja2 import Template
import requests
# from decouple import config
import torch
from create_db import load_collection
import nltk
# from maps_scraper import *
import pandas as pd
# from time import sleep
# from context import *
nltk.download('stopwords')
from nltk.corpus import stopwords
import time
import pickle
from rdflib import Graph
# import chainlit as cl

start = time.time()

spanish_stop_words = stopwords.words('spanish')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"PyTorch está utilizando el dispositivo: {device}")

HUGGINGFACE_TOKEN= "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"

def zephyr_instruct_template(messages, add_generation_prompt=True):
    # Definir la plantilla Jinja
    template_str = "{% for message in messages %}"
    template_str += "{% if message['role'] == 'user' %}"
    template_str += "<|user|>{{ message['content'] }}</s>\n"
    template_str += "{% elif message['role'] == 'assistant' %}"
    template_str += "<|assistant|>{{ message['content'] }}</s>\n"
    template_str += "{% elif message['role'] == 'system' %}"
    template_str += "<|system|>{{ message['content'] }}</s>\n"
    template_str += "{% else %}"
    template_str += "<|unknown|>{{ message['content'] }}</s>\n"
    template_str += "{% endif %}"
    template_str += "{% endfor %}"
    template_str += "{% if add_generation_prompt %}"
    template_str += "<|assistant|>\n"
    template_str += "{% endif %}"

    # Crear un objeto de plantilla con la cadena de plantilla
    template = Template(template_str)

    # Renderizar la plantilla con los mensajes proporcionados
    return template.render(messages=messages, add_generation_prompt=add_generation_prompt)


# Aquí hacemos la llamada el modelo
def generate_answer(prompt: str, max_new_tokens: int = 256, ) -> None:
    try:
        print(11111111111111111111111111111111111111111111111111111111111111111111)
        # Tu clave API de Hugging Face
        api_key = "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"

        # URL de la API de Hugging Face para la generación de texto
        api_url = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

        # Cabeceras para la solicitud
        headers = {"Authorization": f"Bearer {api_key}"}

        # Datos para enviar en la solicitud POST
        # Sobre los parámetros: https://huggingface.co/docs/transformers/main_classes/text_generation
        data = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": max_new_tokens,
                "temperature": 0.5,
                "top_k": 50,
                "top_p": 0.95
            }
        }

        # Realizamos la solicitud POST
        response = requests.post(api_url, headers=headers, json=data)
        print(2222222222222222222222222222222222222222222222222222222)

        # Extraer respuesta
        respuesta = response.json()[0]["generated_text"][len(prompt):]
        return respuesta

    except Exception as e:
        print(f"An error occurred: {e}")

# Esta función prepara el prompt en estilo QA
def prepare_prompt(query_str: str, nodes: list):#, user_info: str = None):
  TEXT_QA_PROMPT_TMPL = (
    #   "La información del usuario es la siguiente:\n"
    #     "---------------------\n"
    #     "{user_info_str}\n"
    #     "---------------------\n"
      "La información de contexto es la siguiente:\n"
      "---------------------\n"
      "{context_str}\n"
      "---------------------\n"
      ####VER ESTOOOOOOOOOOOOOOOOOOOOO -
      "RESPONDE EN ESPAÑOL. Dada la información de contexto anterior, y sin utilizar conocimiento previo, responde en español la siguiente consulta.\n"
      #En caso de que tu respuesta sea una receta envíala con título, ingredientes, procedimiento. No debes agregar recetas de otros libros ni material adicional. En caso de que la receta pedida no se encuentre en el material provisto debes aclararlo y no enviar receta.\n"
      "Pregunta: {query_str}\n"
      "Respuesta: "
  )

  # Construimos el contexto de la pregunta
  context_str = ''
  for node in nodes:
      page_label = node.metadata["page_label"]
      file_path = node.metadata["file_path"]
      context_str += f"\npage_label: {page_label}\n"
      context_str += f"file_path: {file_path}\n\n"
      context_str += f"{node.text}\n"

  messages = [
      {
          "role": "system",
          "content": "Eres un asistente especialista en la historia de la ciudad de Rosario que siempre responde con respuestas veraces, útiles y basadas en hechos.",
      },
      {"role": "user", "content": TEXT_QA_PROMPT_TMPL.format(context_str=context_str, query_str=query_str)}, #,user_info_str=user_info)},
  ]

  final_prompt = zephyr_instruct_template(messages)
  return final_prompt



def load_model():
    
    print(3333333333333333333333333333333333333333333333333)
    
    print('Cargando modelo de embeddings...')
    embed_model = LangchainEmbedding(HuggingFaceEmbeddings(
        model_name='sentence-transformers/paraphrase-multilingual-mpnet-base-v2',
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    )
    print('Indexando documentos...')
    chroma_collection = load_collection()
    print(4444444444444444444444444444444444444444444444444444444444444444)

    # set up ChromaVectorStore and load in data
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    service_context = ServiceContext.from_defaults(embed_model=embed_model, llm=None)
 
    index = VectorStoreIndex.from_vector_store(
        vector_store, storage_context=storage_context, service_context=service_context, show_progress=True
    )
    
    retriever = index.as_retriever(similarity_top_k=2)
    print(5555555555555555555555555555555555555555555555555555555555)
    return retriever

    
def get_answer(retriever, query_str:str, context: str = None):
    nodes = retriever.retrieve(query_str)
    print(6666666666666666666666666666666666666666666666666666)
    final_prompt = prepare_prompt(query_str, nodes)#, context)
    return generate_answer(final_prompt)

print(777777777777777777777777777777777777777777777777777)

def obtener_actividades_aleatorias(df, num_actividades=2):
    # Seleccionar filas aleatorias del DataFrame
    actividades_aleatorias = df.sample(n=num_actividades)
    
    # Iterar sobre las filas seleccionadas y formatear la salida
    resultados = []
    for _, actividad in actividades_aleatorias.iterrows():
        lugar = actividad['Lugar']
        descripcion = actividad['descripcion']
        ubicacion = actividad['ubicacion']
        resultado = f"Lugar: {lugar}\nDescripcion: {descripcion}\nUbicacion: {ubicacion}"
        resultados.append(resultado)
            
    # Unir los resultados en un solo string
    resultado_final = '\n\n'.join(resultados)
    
    return resultado_final

def obtener_personajes_aleatorios(df, num_personajes=2):
    # Quiero cargar mi grafo de conocimiento desde bdd_grafos/graph.ttl en formato turtle

    #Quiero cargar el grafo en un objeto rdflib.Graph
    graph = Graph()
    graph.parse('bdd_grafos/graph.ttl', format='ttl')

    # Quiero hacer una consulta SPARQL para obtener los personajes que sean de un deporte especifico.







    # y luego hacer una consulta SPARQL para obtener los personajes
    # que sean de la ciudad de Rosario.
    

    personajes_aleatorios = df.sample(n=num_personajes)
    
    # Iterar sobre las filas seleccionadas y formatear la salida
    resultados = []
    for _, personaje in personajes_aleatorios.iterrows():
        nombre = personaje['Nombre']
        descripcion = personaje['descripcion']
        resultado = f"Nombre: {nombre}\nDescripcion: {descripcion}"
        resultados.append(resultado)
            
    # Unir los resultados en un solo string
    resultado_final = '\n\n'.join(resultados)
    
    return resultado_final

def pregunta_clasificar(query: str, retriever):
    # Aquí se clasificaría la pregunta importando el vectorizador y el clasificador
    vectorizador = pickle.load(open('vectorizador.pickle', 'rb'))
    clasificador = pickle.load(open('clasificador.pickle', 'rb'))

    vectorized_query = vectorizador.transform([query])
    prediction = clasificador.predict(vectorized_query)
    if prediction[0] == 0:
        #cargar csv con las actividades
        df = pd.read_csv('data_structured/actividades.csv')
        return obtener_actividades_aleatorias(df,2)
         
    elif prediction[0] == 1:
        return "personaje"
    else:
        get_answer(retriever, query)
    
    return prediction[0]


# retriever = load_model()
# print("fin"*10)
# print(get_answer(retriever, "¿Cuál es la historia de Rosario?"))

# end = time.time()
# print(f"Tiempo de ejecución: {end - start} segundos.")


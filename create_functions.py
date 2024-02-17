from langchain_community.embeddings import HuggingFaceEmbeddings
from llama_index import VectorStoreIndex
from llama_index.embeddings import LangchainEmbedding
from llama_index import ServiceContext
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores import ChromaVectorStore


from jinja2 import Template
import requests
import torch
from create_db import load_collection
import pandas as pd


import time
import pickle
from rdflib import Graph
from rdflib import Graph, Namespace, Literal
from rdflib.plugins.sparql import prepareQuery
import random

start = time.time()


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
    print(11111111111111111111111111111111111111111111111111111111111111111111)
    # Crear un objeto de plantilla con la cadena de plantilla
    template = Template(template_str)

    # Renderizar la plantilla con los mensajes proporcionados
    return template.render(messages=messages, add_generation_prompt=add_generation_prompt)


# Aquí hacemos la llamada el modelo
def generate_answer(prompt: str, max_new_tokens: int = 256, ) -> None:
    try:
        print(2222222222222222222222222222222222222222222222222222222222222222)
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
        print(4444444444444444444444444444444444444444444444444444444)
        # Realizamos la solicitud POST
        response = requests.post(api_url, headers=headers, json=data)
        print(5555555555555555555555555555555555555555555555555555555)

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
  print(6666666666666666666666666666666666666666666666666666)
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
  print(77777777777777777777777777777777777777777777777777)
  final_prompt = zephyr_instruct_template(messages)
  print(88888888888888888888888888888888888888888888888888)
  return final_prompt

def load_model():
    
    print(999999999999999999999999999999999999999999999999)
    
    print('Cargando modelo de embeddings EN FUNCTIONS...')
    embed_model = LangchainEmbedding(HuggingFaceEmbeddings(
        model_name='sentence-transformers/paraphrase-multilingual-mpnet-base-v2',
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    )
    print('Indexando documentos...')
    chroma_collection = load_collection()
    print(10101010101010101010101010101010101010101010101010)

    # set up ChromaVectorStore and load in data
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    service_context = ServiceContext.from_defaults(embed_model=embed_model, llm=None)
 
    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store, storage_context=storage_context, service_context=service_context, show_progress=True
    )
    
    retriever = index.as_retriever(similarity_top_k=2)
    print(12121212121212121212121212121212121212121212121212)
    return retriever

    
def get_answer(retriever, query_str:str, context: str = None):
    nodes = retriever.retrieve(query_str)
    print(1313131313131313131313131313131313131313131313131313)
    final_prompt = prepare_prompt(query_str, nodes)#, context)
    print(14141441414141414141414141414141414141414141414141414)
    return generate_answer(final_prompt)



def obtener_actividades_aleatorias(df, num_actividades=2):
    # Seleccionar filas aleatorias del DataFrame
    actividades_aleatorias = df.sample(n=num_actividades)
    print("15"*10)
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

def obtener_personajes():
    # Cargar el grafo RDF
    g = Graph()
    g.parse("./bdd_grafos/graph.ttl", format="turtle")
    print("16"*10)
    # Definir los prefijos de los espacios de nombres
    n = Namespace("http://example.org/rosario/")
    EX = Namespace("http://example.org/attributes/")

    query = prepareQuery("""
        SELECT ?personaje ?rama ?vive ?edad ?sexo
        WHERE {
            ?personaje EX:vive "Si" .
            ?personaje EX:sexo ?sexo .
            ?personaje EX:rama ?rama .
            ?personaje EX:edad ?edad .
        }
    """, initNs={"EX": EX})

    # Ejecutar la consulta
    resultados = g.query(query)

    # Convertir los resultados a una lista para facilitar la selección aleatoria
    personajes = list(resultados)

    # Seleccionar aleatoriamente 2 personajes
    personajes_aleatorios = random.sample(personajes, 2)

    return personajes_aleatorios

def pregunta_clasificar(retriever, query: str):
    # Aquí se clasificaría la pregunta importando el vectorizador y el clasificador
    vectorizador = pickle.load(open('vectorizer.pickle', 'rb'))
    clasificador = pickle.load(open('clasificador.pickle', 'rb'))
    print("17"*10)
    vectorized_query = vectorizador.transform([query])
    prediction = clasificador.predict(vectorized_query)
    if prediction[0] == 0:
        #cargar csv con las actividades
        df = pd.read_csv('data_structured/actividades.csv')
        return obtener_actividades_aleatorias(df,2)
         
    elif prediction[0] == 1:
        personajes_aleatorios = obtener_personajes()
       
        # Inicializar un string vacío para almacenar el output
        output_string = ""
       
        # Iterar sobre cada personaje y concatenar sus atributos al string
        for row in personajes_aleatorios:
            # Extraer solo el nombre del enlace
            nombre = (str(row.personaje).split("/")[-1]).replace("_", " ")

            output_string += "Nombre: " + nombre + "\n"
            output_string += "Rama: " + str(row.rama) + "\n"
            # output_string += "Vive: " + str(row.vive) + "\n"
            output_string += "Edad: " + str(row.edad) + "\n"
            output_string += "Sexo: " + str(row.sexo) + "\n\n"

        return output_string
    
    elif prediction[0] == 2: 
        print("--------ESTOY EN EL 2---------")
        respuesta = get_answer(retriever, query)
        print("18"*10)
        return respuesta

from rdflib import Graph, Namespace, Literal
from rdflib.plugins.sparql import prepareQuery
import random

def obtener_personajes():
    # Cargar el grafo RDF
    g = Graph()
    g.parse("./bdd_grafos/graph.ttl", format="turtle")

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

# Imprimir el string con el output
print(output_string)


# Convertir los resultados en una lista de diccionarios
# Convertir los resultados en una lista de diccionarios
# personajes = []
# for row in personajes_aleatorios:
#     # Extraer solo el nombre del enlace
#     nombre = (str(row.personaje).split("/")[-1]).replace("_", " ")
#     personaje = {
#         "Nombre": nombre,
#         "Rama": str(row.rama),
#         "Vive": str(row.vive),
#         "Edad": int(row.edad),
#         "Sexo": str(row.sexo)
#     }
#     personajes.append(personaje)

# # Imprimir los atributos de los personajes
# for personaje in personajes:
#     print("Nombre:", personaje["Nombre"])
#     print("Rama:", personaje["Rama"])
#     print("Vive:", personaje["Vive"])
#     print("Edad:", personaje["Edad"])
#     print("Sexo:", personaje["Sexo"])
#     print()
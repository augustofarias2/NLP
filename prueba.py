# # from rdflib import Graph, Namespace
# # from rdflib.plugins.sparql import prepareQuery

# # # Cargar el grafo RDF desde el archivo Turtle
# # g = Graph()
# # g.parse("bdd_grafos/graph.ttl", format="turtle")

# # # Definir los prefijos necesarios
# # owl = Namespace("http://www.w3.org/2002/07/owl#")
# # rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")

# # # Obtener la categoría específica ingresada por el usuario
# # categoria = input("Ingresa la categoría específica: ")

# # # Construir la consulta SPARQL
# # query = prepareQuery(
# #     """
# #     SELECT ?personaje
# #     WHERE {
# #         ?personaje a owl:NamedIndividual ;
# #                    owl:hasRama ?categoria .
# #         ?categoria rdfs:label ?label .
# #         FILTER(?label = $categoria)
# #     }
# #     """,
# #     initNs={"owl": owl, "rdfs": rdfs}
# # )

# # # Ejecutar la consulta SPARQL
# # resultados = g.query(query, initBindings={"categoria": categoria})

# # # Formatear el resultado
# # output = f"Algunos personajes históricos de la categoría {categoria} son: "
# # for row in resultados:
# #     output += f"\n- {row.personaje}"

# # # Imprimir el resultado
# # print(output)



# import networkx as nx
# import matplotlib.pyplot as plt

# # # Crear un grafo dirigido
# # grafo = nx.DiGraph()

# # # Información de personas y sus áreas
# # informacion = [
# #     ('Lionel_Messi', 'Deporte'), ('Luciana_Aymar', 'Deporte'), ('Angel_Di_Maria', 'Deporte'),
# #     ('Fito_Paez', 'Musica'), ('Nicki_Nicole', 'Musica'), ('Juan_Carlos_Baglietto', 'Musica'),
# #     ('Alberto_Olmedo', 'Humor'), ('Migue_Granados', 'Humor'), ('Roberto_Fontanarrosa', 'Humor'),
# #     ('Ernesto_Che_Guevara', 'Politica'), ('Lisandro_de_la_Torre', 'Politica'), ('Cristian_Newell', 'Politica'),
# #     ('Roberto_Fontanarrosa', 'Literatura'), ('Alberto_Olmedo', 'Literatura'), ('Cristian_Newell', 'Deporte'),
# #     ('Ernesto_Che_Guevara', 'Literatura'), ('Lisandro_de_la_Torre', 'Literatura')
# # ]

# # # Agregar nodos y aristas al grafo
# # for persona, area in informacion:
# #     grafo.add_node(persona)
# #     grafo.add_node(area)
# #     grafo.add_edge(persona, area)

# # # Dibujar el grafo
# # nx.draw(grafo, with_labels=True, node_color='lightblue', node_size=1500, font_size=8, font_weight='bold', edge_color='gray')
# # plt.show()



# from rdflib import Graph, Literal, Namespace, URIRef

# # Crear un grafo vacío
# g = Graph()

# # Definir algunos espacios de nombres y recursos
# n = Namespace("http://example.org/people/")
# EX = Namespace("http://example.org/terms/")

# # Añadir tripletas al grafo
# g.add((n.bob, EX.age, Literal(28)))
# g.add((n.bob, EX.name, Literal("Bob")))
# g.add((n.alice, EX.age, Literal(24)))
# g.add((n.alice, EX.name, Literal("Alice")))



# # Serializar y mostrar el grafo en formato "turtle" (opcional)
# print(g.serialize(format="turtle"))

# # Convertir el grafo RDF a un grafo de NetworkX
# nx_graph = nx.Graph()

# for s, p, o in g:
#     nx_graph.add_edge(s, o)

# # Dibujar el grafo utilizando Matplotlib
# plt.figure(figsize=(8, 6))
# nx.draw(nx_graph, with_labels=True, node_size=2000, font_size=12, font_weight='bold')
# plt.title("Grafo RDF visualizado con Matplotlib")
# plt.show()

# # Definir una consulta SPARQL para obtener todas las personas y sus edades
# q1 = """
#     SELECT ?person ?age WHERE {
#         ?person <http://example.org/terms/age> ?age .
#     }
# """

# # Ejecutar la consulta
# results = g.query(q1)

# # Imprimir los resultados
# print('Query 1:')
# for r in results:
#     print(f"{r['person']} tiene {r['age']} años.")

# # Definir otra consulta SPARQL para obtener personas mayores de 25 años
# q2 = """
#     SELECT ?person WHERE {
#         ?person <http://example.org/terms/age> ?age .
#         FILTER(?age > 25)
#     }
# """

# # Ejecutar la consulta
# results = g.query(q2)

# # Imprimir los resultados
# print('Query 2:')
# for r in results:
#     print(f"{r['person']} es mayor de 25 años.")


import networkx as nx
import matplotlib.pyplot as plt
from rdflib import Graph, Literal, Namespace, URIRef

# Crear un grafo RDF
g = Graph()

# Definir algunos espacios de nombres y recursos
n = Namespace("http://example.org/rosario/")
EX = Namespace("http://example.org/attributes/")

# Tripletas de datos
tripletas = [
    (n.lionel_messi, "Deporte", "Si", 36, "Hombre"),
    (n.luciana_aymar, "Deporte", "Si", 43, "Mujer"),
    (n.alberto_olmedo, "Humor", "No", 54, "Hombre"),
    (n.juan_carlos_baglietto, "Musica", "Si", 60, "Hombre"),
    (n.nicki_nicole, "Musica", "Si", 28, "Mujer"),
    (n.fito_paez, "Musica", "Si", 58, "Hombre"),
    (n.migue_granados, "Humor", "Si", 40, "Hombre"),
    (n.roberto_fontanarrosa, "Humor", "No", 72, "Hombre"),
    (n.angel_di_maria, "Deporte", "Si", 33, "Hombre"),
    (n.ernesto_che_guevara, "Politica", "No", 39, "Hombre"),
    (n.lisandro_de_la_torre, "Politica", "No", 64, "Hombre"),
    (n.cristian_newell, "Politica", "Si", 40, "Hombre")
]

# Añadir tripletas al grafo
for sujeto, rama, vive, edad, sexo in tripletas:
    g.add((sujeto, EX.rama, Literal(rama)))
    g.add((sujeto, EX.vive, Literal(vive)))
    g.add((sujeto, EX.edad, Literal(edad)))
    g.add((sujeto, EX.sexo, Literal(sexo)))

# Convertir el grafo RDF a un grafo de NetworkX
nx_graph = nx.Graph()

for s, p, o in g:
    nx_graph.add_edge(s, o)

# Dibujar el grafo utilizando Matplotlib
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(nx_graph)
nx.draw(nx_graph, pos, with_labels=True, node_size=2000, font_size=12, font_weight='bold', node_color='skyblue')
plt.title("Grafo RDF de personajes históricos de Rosario y sus atributos")
plt.show()
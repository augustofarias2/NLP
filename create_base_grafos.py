import networkx as nx
import matplotlib.pyplot as plt
from rdflib import Graph, Literal, Namespace, URIRef
import os

# Crear un grafo RDF
g = Graph()

# Definir algunos espacios de nombres y recursos
n = Namespace("http://example.org/rosario/")
EX = Namespace("http://example.org/attributes/")

# Tripletas de datos
tripletas = [
    (n.Lionel_Messi, "Deporte", "Si", 36, "Hombre"),
    (n.Luciana_Aymar, "Deporte", "Si", 43, "Mujer"),
    (n.Alberto_Olmedo, "Humor", "No", 54, "Hombre"),
    (n.Juan_Carlos_Baglietto, "Musica", "Si", 67, "Hombre"),
    (n.Nicki_Nicole, "Musica", "Si", 23, "Mujer"),
    (n.Fito_Paez, "Musica", "Si", 58, "Hombre"),
    (n.Migue_Granados, "Humor", "Si", 37, "Hombre"),
    (n.Roberto_Fontanarrosa, "Humor", "No", 72, "Hombre"),
    (n.Angel_Di_Maria, "Deporte", "Si", 35, "Hombre"),
    (n.Ernesto_Che_Guevara, "Politica", "No", 95, "Hombre"),
    (n.Lisandro_De_La_Torre, "Politica", "No", 64, "Hombre"),
    (n.Hermes_Binner, "Politica", "No", 80, "Hombre")
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
# plt.figure(figsize=(12, 8))
# pos = nx.spring_layout(nx_graph)
# nx.draw(nx_graph, pos, with_labels=True, node_size=2000, font_size=12, font_weight='bold', node_color='skyblue')
# plt.title("Grafo RDF de personajes históricos de Rosario y sus atributos")
# plt.show()

#Guardar el grafo en formato tutle en la carpeta bdd_grafos
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bdd_grafos')
g.serialize(destination=os.path.join(path, f'graph.ttl'), format='turtle')
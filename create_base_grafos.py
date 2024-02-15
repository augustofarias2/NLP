import networkx as nx
import matplotlib.pyplot as plt
import os
from rdflib import Graph, URIRef, RDF, RDFS
import urllib.parse

# Creamos un grafo dirigido
G = nx.DiGraph()

# Creamos nodos para las personas históricas de la ciudad de Rosario
personas = ['Lionel_Messi', 'Luciana_Aymar', 'Alberto_Olmedo', 'Juan_Carlos_Baglietto', 'Nicki_Nicole', 'Fito_Paez', 'Migue_Granados', 'Roberto_Fontanarrosa', 'Angel_Di_Maria', 'Ernesto_Che_Guevara', 'Lisandro_de_la_Torre', 'Cristian_Newell']

# Creamos nodos para las ramas en las que se destacaron
ramas = ['Deporte', 'Humor', 'Musica', 'Literatura', 'Politica']

# Agregamos nodos al grafo
G.add_nodes_from(personas, bipartite=0)  # personas
G.add_nodes_from(ramas, bipartite=1)     # ramas

# Creamos relaciones entre personas y ramas
relaciones = [('Lionel_Messi', 'Deporte'), ('Luciana_Aymar', 'Deporte'),
             ('Angel_Di_Maria', 'Deporte'),
             ('Fito_Paez', 'Musica'),
             ('Nicki_Nicole', 'Musica'), ('Juan_Carlos_Baglietto', 'Musica'),
             ('Alberto_Olmedo', 'Humor'), ('Migue_Granados', 'Humor'),
             ('Roberto_Fontanarrosa', 'Humor'), ('Ernesto_Che_Guevara', 'Politica'),
             ('Lisandro_de_la_Torre', 'Politica'), ('Cristian_Newell', 'Politica'),
             ('Roberto_Fontanarrosa', 'Literatura'), ('Alberto_Olmedo', 'Literatura'),
             ('Cristian_Newell', 'Deporte'),
             ('Ernesto_Che_Guevara', 'Literatura'), ('Lisandro_de_la_Torre', 'Literatura')
               ]

# Agregamos relaciones al grafo
G.add_edges_from(relaciones)

#Crear un rdf con los datos
g = Graph()

# Agregamos las personas como instancias de la clase Persona
for persona in personas:
    persona_uri = urllib.parse.quote(persona)
    g.add((URIRef(persona_uri), RDF.type, URIRef('http://www.w3.org/2002/07/owl#NamedIndividual')))
    g.add((URIRef(persona_uri), RDFS.label, URIRef(persona)))

# Agregamos las ramas como instancias de la clase Rama
for rama in ramas:
    rama_uri = urllib.parse.quote(rama)
    g.add((URIRef(rama_uri), RDF.type, URIRef('http://www.w3.org/2002/07/owl#NamedIndividual')))
    g.add((URIRef(rama_uri), RDFS.label, URIRef(rama)))

# Agregamos las relaciones entre personas y ramas
for relacion in relaciones:
    g.add((URIRef(urllib.parse.quote(relacion[0])), URIRef('http://www.w3.org/2002/07/owl#hasRama'), URIRef(urllib.parse.quote(relacion[1])))
    )
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bdd_grafos')

#Guardar el grafo en formato tutle en la carpeta bdd_grafos
g.serialize(destination=os.path.join(path, f'graph.ttl'), format='turtle')

# Imprimir el grafo
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='grey')
# plt.show()

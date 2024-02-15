import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo dirigido
G = nx.DiGraph()

# Creamos nodos para las personas históricas de la ciudad de Rosario
personas = ['Lionel Messi', 'Luciana Aymar', 'Alberto Olmedo', 'Juan Carlos Baglietto','Nicki Nicole','Fito Paez', "Migue Granados","Roberto Fontanarrosa", "Angel Di Maria", "Ernesto Che Guevara", "Lisandro de la Torre", "Cristian Newell"]

# Creamos nodos para las ramas en las que se destacaron
ramas = ['Deporte', 'Humor', 'Musica', 'Literatura', 'Politica']


#luciana messi angel crisne deporte
#che lisandro crisnew politica
#fito nicki baglietto musica
#alberto roberto migue humor

#roberto alberto Che Lisandro literatura

# Agregamos nodos al grafo
G.add_nodes_from(personas, bipartite=0)  # personas
G.add_nodes_from(ramas, bipartite=1)     # ramas

# Creamos relaciones entre personas y ramas
relaciones = [('Lionel Messi', 'Deporte'), ('Luciana Aymar', 'Deporte'),
              ('Angel Di Maria', 'Deporte'),
              ('Fito Paez', 'Musica'),
              ('Nicki Nicole', 'Musica'), ('Juan Carlos Baglietto', 'Musica'),
              ('Alberto Olmedo', 'Humor'), ('Migue Granados', 'Humor'),
              ('Roberto Fontanarrosa', 'Humor'), ('Ernesto Che Guevara', 'Politica'),
              ('Lisandro de la Torre', 'Politica'), ('Cristian Newell', 'Politica'),
              ('Roberto Fontanarrosa', 'Literatura'), ('Alberto Olmedo', 'Literatura'),
              ('Cristian Newell', 'Deporte'),
              ('Ernesto Che Guevara', 'Literatura'), ('Lisandro de la Torre', 'Literatura')
                ]

# Agregamos relaciones al grafo
G.add_edges_from(relaciones)

#Guardar base de datos formato rdf
nx.write_rdf(G, "test.rdf")


# Dibujamos el grafo
pos = nx.bipartite_layout(G, personas)
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue')
plt.title('Grafo de Personas Históricas y sus Ramas de Destaque')
plt.show()
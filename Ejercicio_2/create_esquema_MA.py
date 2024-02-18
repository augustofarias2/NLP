import graphviz

# Crear un objeto Digraph
dot = graphviz.Digraph()

# Añadir los nodos (agentes y entidades)
dot.node('AR', 'Agente de Recepción')
dot.node('AHC', 'Agente de Historia Clínica')
dot.node('AD', 'Agente de Diagnóstico')
dot.node('APR', 'Agente de Programación de Recursos')
dot.node('AS', 'Agente de Seguimiento')
dot.node('Paciente', 'Paciente')
dot.node('Equipo_Medico', 'Equipo Médico')

# Añadir las conexiones entre los nodos
dot.edges([('AR', 'AHC'), ('AR', 'AD'), ('AD', 'AHC'), ('AD', 'APR'), ('APR', 'AS'), ('AS', 'Paciente'), ('APR', 'Equipo_Medico')])

# Visualizar el diagrama
dot.render('diagrama_flujo_clinica', format='png', cleanup=True)

class AgenteRecepcion:
    def __init__(self):
        pass
    
    def atender_paciente(self, paciente):
        print("Atendiendo al paciente:", paciente)
        # Lógica para gestionar citas y registrar información
        #

class AgenteHistoriaClinica:
    def __init__(self):
        pass
    
    def actualizar_historia_clinica(self, paciente, sintomas):
        print("Actualizando historia clínica de", paciente, "con los síntomas:", sintomas)
        # Lógica para gestionar y actualizar la historia clínica
        #

class AgenteDiagnostico:
    def __init__(self):
        pass
    
    def sugerir_pruebas(self, paciente, sintomas):
        print("Sugiriendo pruebas para", paciente, "basado en los síntomas:", sintomas)
        # Lógica para sugerir pruebas médicas
        #

class AgenteProgramacionRecursos:
    def __init__(self):
        pass
    
    def programar_pruebas(self, paciente, pruebas):
        print("Programando pruebas para", paciente, ":", pruebas)
        # Lógica para programar recursos y asignar citas
        #

class AgenteSeguimiento:
    def __init__(self):
        pass
    
    def hacer_seguimiento(self, paciente, tratamiento):
        print("Haciendo seguimiento a", paciente, "sobre el tratamiento:", tratamiento)
        # Lógica para hacer seguimiento post-consulta
        #

# Creamos instancias de los agentes
agente_recepcion = AgenteRecepcion()
agente_historia_clinica = AgenteHistoriaClinica()
agente_diagnostico = AgenteDiagnostico()
agente_programacion_recursos = AgenteProgramacionRecursos()
agente_seguimiento = AgenteSeguimiento()

# Simulamos una interacción entre los agentes
paciente = "Juan"
sintomas = ["dolor de cabeza", "fiebre"]
pruebas = ["análisis de sangre", "radiografía"]
tratamiento = "antibióticos"

agente_recepcion.atender_paciente(paciente)
agente_historia_clinica.actualizar_historia_clinica(paciente, sintomas)
agente_diagnostico.sugerir_pruebas(paciente, sintomas)
agente_programacion_recursos.programar_pruebas(paciente, pruebas)
agente_seguimiento.hacer_seguimiento(paciente, tratamiento)
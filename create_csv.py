#Quiero crear un archivo csv con datos de actividades para hacer en una ciudad
#Quiero que contenga las colunnas: id, actividad, descripcion, ubicacion
#Las actividades las voy a escribir yo
#Las descripciones las voy a escribir yo
#La ubicacion la voy a escribir yo
#
import pandas as pd
import os
import csv
from typing import List, Dict, Any
from datetime import datetime
from dateutil import tz
import pytz
from dateutil import parser
from dateutil.tz import gettz
from dateutil.tz import tzutc

def create_csv():
    # Crear un dataframe con los datos
    data = {
        'id': [1, 2, 3, 4, 5],
        'actividad': ['Cine', 'Cenar', 'Bailar', 'Pasear', 'Playa'],
        'descripcion': ['Ir al cine', 'Ir a cenar', 'Ir a bailar', 'Ir a pasear', 'Ir a la playa'],
        'ubicacion': ['Rosario', 'Rosario', 'Rosario', 'Rosario', 'Rosario']
    }
    df = pd.DataFrame(data)
    # Guardar el dataframe en un archivo csv
    df.to_csv(os.path.dirname(os.path.abspath(__file__)) + "/tabular_data/actividades.csv", index=False)

    #Quiero que sean 15 actividades
    #Quiero que sean 15 descripciones
    #Quiero que sean 15 ubicaciones
    #Quiero que sean 15 id
    # Crear un dataframe con los datos

    data = {
        'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        'Lugar': ['Monumento', 'Teatro el circulo', 'La florida', 'Parque de la Independencia', 'La isla de los inventos', 'Puente Rosario-Victoria', 'Museo de arte decorativo', 'Parque de España', 'Parque Nacional a la Bandera', 'Casino', 'La granja de la infancia', 'Museo de bellas artes', 'Parroquia Natividad del señor', 'Estadio Marcelo Bielsa', 'Estadio Gigante de arroyito'],
        'descripcion': ['Visita guiada y vista de la ciudad desde la cima del monumento',
                        'Es un teatro fundado en 1904, que se destaca por su arquitectura e historia. Allí cantó Caruso, y en 2004 fue cede del Congreso de la Lengua Española. En su subsuelo ("catacumbas")hay un museo de esculturas.Es un lugar único que los viajeros deberían conocer.',
                        'Hermosa playa para disfrutar la vista al rio, practicar deportes náuticos, beach volley o solo tomar mates.',
                        'Ir a pasear', 'Ir a la playa', 'Ir al parque', 'Hacer deporte', 'Ir a discotecas', 'Ir a bares', 'Ir a restaurantes', 'Ir a la isla', 'Hacer deporte', 'El fútbol es el deporte más popular', 'El baloncesto es un deporte de equipo', 'El tenis es un deporte individual'],
        'ubicacion': ['Santa Fe 581','']
    }
    df = pd.DataFrame(data)
    # Guardar el dataframe en un archivo csv
    df.to_csv(os.path.dirname(os.path.abspath(__file__)) + "/tabular_data/actividades.csv", index=False)

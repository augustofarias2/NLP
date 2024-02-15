#Importar librerias
import pandas as pd
import os


def create_csv():
    data = {
        'id': [1, 2, 3, 4, 5, 6, 7],
        'Lugar': ['Monumento', 'Teatro el circulo', 'La florida', 'Parque de la Independencia', 'Puente Rosario-Victoria', 'Museo de arte decorativo', 'Parque de España'],
        'descripcion': ['Visita guiada y vista de la ciudad desde la cima del monumento',
                        'Es un teatro fundado en 1904, que se destaca por su arquitectura e historia. Allí cantó Caruso, y en 2004 fue cede del Congreso de la Lengua Española. En su subsuelo ("catacumbas")hay un museo de esculturas.Es un lugar único que los viajeros deberían conocer.',
                        'Hermosa playa para disfrutar la vista al rio, practicar deportes náuticos, beach volley o solo tomar mates.',
                        'El Parque Independencia, es un hermoso lugar para pasear, disfrutar del verde y la conexion con el agua del laguito, con sus patos y demas animales. Podes pasear en el laguito, con los botes que se alquilan, que es hermoso hacerlo. Hay um bar muy lindo para disfrutar un cafecito o lo que te guste y podes disfrutar del mejor Pororo, ADAD, que es riquisimo.',
                        'Puente que conecta Rosario con la ciudad de Victoria, Entre Ríos. Es el puente más largo de Argentina y uno de los más largos de América Latina. Es un lugar ideal para disfrutar de una vista panorámica de la ciudad y el río Paraná.',
                        'Se ubica a pocos metros de la catedral, en pleno casco histórico. La antigua casona fue donada por la viuda de Estévez a la municipalidad de Rosario para que funcione como museo. Tuvimos la suerte de tener una visita guiada donde nos mostraron las diferentes salas y todos los objetos que fueron coleccionados por el matrimonio. Podemos ver platería, marfiles, tapices, alfombras, cristalería, muebles y varias pinturas europeas, se destaca una obra de Goya',
                        'El parque es un amplio sector aledaño a la línea costera de la barranca del Paraná, con césped y árboles, como pavimentos para pedestres, y un buen lugar de estacionamiento.'
                    ],                    
        'ubicacion': ['Santa Fe 581',
                        'Laprida 1235',
                        'Av. Costanera',
                        'Av. Pellegrini y Bv. Oroño',
                        'Río Paraná',
                        'Santa Fe 748',
                        'Sarmiento y el río',
                        ]
    }

    df = pd.DataFrame(data)

    # Guardar el dataframe en un archivo csv
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data_structured", "actividades.csv")
    df.to_csv(file_path, index=False)


create_csv()
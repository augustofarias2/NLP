from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import nltk

# Descargamos los stopwords que necesitaremos luego
nltk.download('stopwords')
from nltk.corpus import stopwords

# Obtenemos las stopwords para español
spanish_stop_words = stopwords.words('spanish')

labels = [(0, "actividades"), (1, "historia")]
# , (2, "inteligencia artificial"),
        #   (3, "ciberseguridad")]

dataset = []
#textos de "actividades para realizar en pareja"
dataset.append((0, "Me gusta ir al cine con mi pareja."))
dataset.append((0, "Me gusta ir a cenar con mi pareja."))
dataset.append((0, "Me gusta ir a bailar con mi pareja."))
dataset.append((0, "Me gusta ir a pasear con mi pareja."))
dataset.append((0, "Me gusta ir a la playa con mi pareja."))
dataset.append((0, "Me gusta ir al parque con mis amigos."))
dataset.append((0, "Me gusta hacer deporte en familia."))
dataset.append((0, "El deporte es bueno para la salud de la familia."))
dataset.append((0, "Me gusta ir a discotecas con amigos"))
dataset.append((0, "Me gusta ir a bares con amigos"))
dataset.append((0, "Me gusta ir a restaurantes con amigos"))
dataset.append((0, "Me gusta ir a la playa con amigos"))
dataset.append((0, "Me gusta ir a la isla con amigos"))
dataset.append((0, "Me gusta hacer deporte."))
dataset.append((0, "El deporte es bueno para la salud."))
dataset.append((0, "El fútbol es el deporte más popular."))
dataset.append((0, "El baloncesto es un deporte de equipo."))
dataset.append((0, "El baloncesto es un deporte muy completo."))
dataset.append((0, "El tenis es un deporte individual."))
dataset.append((0, "El ajedrez es un deporte mental."))
dataset.append((0, "El atletismo es un deporte olímpico."))
dataset.append((0, "El surf es un deporte acuático."))
dataset.append((0, "El esquí es un deporte de invierno."))
dataset.append((0, "El snowboard es un deporte extremo."))
dataset.append((0, "El atletismo es un deporte olímpico."))
dataset.append((0, "El ciclismo es un deporte de resistencia."))
dataset.append((0, "El boxeo es un deporte de contacto."))
dataset.append((0, "El rugby es un deporte de equipo."))
dataset.append((0, "El golf es un deporte de precisión."))
dataset.append((0, "El pádel es un deporte de raqueta."))
dataset.append((0, "El voleibol es un deporte de equipo."))
dataset.append((0, "El bádminton es un deporte de raqueta."))
dataset.append((0, "El hockey es un deporte con palo y bocha."))
dataset.append((0, "El patinaje es un deporte sobre ruedas."))
dataset.append((0, "El patinaje artístico es un deporte de precisión."))
dataset.append((0, "El patinaje de velocidad es un deporte de resistencia."))
dataset.append((0, "El patinaje sobre hielo es un deporte sobre hielo."))


#textos de "historia de la ciudad de Rosario"
dataset.append((1, "Rosario es una ciudad de Argentina."))
dataset.append((1, "Rosario es la ciudad más grande de la provincia de Santa Fe."))
dataset.append((1, "Rosario es conocida como la cuna de la bandera."))
dataset.append((1, "La bandera de Argentina fue izada por primera vez en Rosario."))
dataset.append((1, "El Monumento a la Bandera es un símbolo de Rosario."))
dataset.append((1, "El Monumento a la Bandera fue inaugurado en 1957."))
dataset.append((1, "El río Paraná atraviesa la ciudad de Rosario."))
dataset.append((1, "El río Paraná es uno de los ríos más importantes de Argentina."))
dataset.append((1, "El Parque Nacional a la Bandera es un lugar de interés turístico."))
dataset.append((1, "El Parque Nacional a la Bandera es un lugar de esparcimiento."))
dataset.append((1, "El Parque Nacional a la Bandera es un lugar de encuentro."))
dataset.append((1, "El Parque Nacional a la Bandera es un lugar de recreación."))
dataset.append((1, "El Parque Nacional a la Bandera es un lugar de paseo."))
dataset.append((1, "El fútbol es el deporte más popular en Rosario."))
dataset.append((1, "De Rosario salieron muchos personajes históricos."))
dataset.append((1, "Rosario es una ciudad con mucha historia."))
dataset.append((1, "Rosario es una ciudad con mucha cultura."))
dataset.append((1, "Rosario es una ciudad con mucha tradición."))
dataset.append((1, "Rosario es una ciudad con mucha identidad."))
dataset.append((1, "Rosario es una ciudad con mucha diversidad."))
dataset.append((1, "Rosario es una ciudad con mucha riqueza."))
dataset.append((1, "Rosario es una ciudad con mucha belleza."))
dataset.append((1, "Rosario es una ciudad con mucha arquitectura."))
dataset.append((1, "Rosario es una ciudad con mucha gastronomía."))
dataset.append((1, "Rosario es una ciudad con mucha música."))
dataset.append((1, "Rosario es una ciudad con mucha literatura."))
dataset.append((1, "Rosario es una ciudad con mucha pintura."))
dataset.append((1, "Rosario es una ciudad con mucha escultura."))



# Preparar X e y
X = [text.lower() for label, text in dataset]
y = [label for label, text in dataset]

# División del dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorización de los textos con eliminación de palabras vacías
vectorizer = TfidfVectorizer(stop_words=spanish_stop_words)
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Creación y entrenamiento del modelo de Regresión Logística con multinomial
modelo_LR = LogisticRegression(max_iter=1000, multi_class='multinomial', solver='lbfgs')
modelo_LR.fit(X_train_vectorized, y_train)

#Guardar modelo
import pickle

pickle.dump(modelo_LR, open("clasificador.pickle", "wb"))
pickle.dump(vectorizer, open("vectorizer.pickle", "wb"))

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

# Definir las etiquetas
labels = [(0, "actividades"), (1, "historia")]

# Crear dataset
dataset = []

#textos que sean parecidos a "actividades para realizar en Rosario"
dataset.append((0, "¿Qué actividades puedo realizar en Rosario?"))
dataset.append((0, "¿Cuáles son las actividades más populares en Rosario?"))
dataset.append((0, "¿Qué lugares puedo visitar en Rosario?"))
dataset.append((0, "¿Cuáles son los lugares más populares en Rosario?"))
dataset.append((0, "¿Qué actividades puedo hacer en Rosario?"))
dataset.append((0, "¿Qué puedo recorrer en Rosario?"))
dataset.append((0, "¿Qué puedo conocer en Rosario?"))
dataset.append((0, "¿Qué puedo visitar en Rosario?"))
dataset.append((0, "¿Qué puedo hacer en Rosario?"))
dataset.append((0, "¿Qué puedo disfrutar en Rosario?"))
dataset.append((0, "Recomendame lugares para pasar el día en Rosario"))
dataset.append((0, "Decime qué puedo hacer en la ciudad"))
dataset.append((0, "Me gustaría conocer lugares históricos de Rosario"))
dataset.append((0, "¿Cuáles son las opciones de entretenimiento en Rosario?"))
dataset.append((0, "¿Qué actividades de ocio ofrece Rosario?"))
dataset.append((0, "¿Cuáles son los sitios de interés turístico en Rosario?"))
dataset.append((0, "¿Qué lugares emblemáticos puedo explorar en Rosario?"))
dataset.append((0, "¿Qué atracciones turísticas son imprescindibles en Rosario?"))
dataset.append((0, "¿Qué experiencias culturales puedo disfrutar en Rosario?"))
dataset.append((0, "¿Dónde puedo encontrar actividades recreativas en Rosario?"))
dataset.append((0, "¿Cuáles son los destinos imperdibles para turistas en Rosario?"))
dataset.append((0, "¿Qué sitios históricos puedo visitar en Rosario?"))
dataset.append((0, "¿Cuáles son las mejores actividades al aire libre en Rosario?"))
dataset.append((0, "¿Qué lugares recomiendas para pasar un día perfecto en Rosario?"))
dataset.append((0, "¿Dónde puedo encontrar información sobre los eventos y actividades en Rosario?"))
dataset.append((0, "¿Cuáles son los puntos de interés más destacados en Rosario?"))
dataset.append((0, "¿Qué circuitos turísticos están disponibles en Rosario?"))
dataset.append((0, "¿Cuáles son las mejores opciones para explorar la ciudad de Rosario?"))

#textos de "personajes históricos de Rosario"
dataset.append((1, "¿Quiénes son los personajes históricos de Rosario?"))
dataset.append((1, "Nombrame personajes históricos de Rosario"))
dataset.append((1, "¿Cuáles son los personajes más importantes de Rosario?"))
dataset.append((1, "¿Quiénes son los personajes destacados de Rosario?"))
dataset.append((1, "¿Quiénes son los personajes ilustres de Rosario?"))
dataset.append((1, "¿Quiénes son los personajes reconocidos de Rosario?"))
dataset.append((1, "¿Quiénes son los personajes famosos de Rosario?"))
dataset.append((1, "¿Quiénes son los personajes históricos de Rosario?"))
dataset.append((1, "Nombrame personajes históricos de Rosario"))
dataset.append((1, "¿Cuáles son los personajes más importantes de Rosario?"))
dataset.append((1, "¿Quiénes son los personajes destacados de Rosario?"))
dataset.append((1, "¿Quiénes son los personajes ilustres de Rosario?"))
dataset.append((1, "¿Quiénes son los personajes reconocidos de Rosario?"))
dataset.append((1, "¿Quiénes son los personajes famosos de Rosario?"))
dataset.append((1, "¿Cuáles son los personajes históricos más importantes de Rosario?"))
dataset.append((1, "¿Quiénes son los personajes destacados en la historia de Rosario?"))
dataset.append((1, "¿Puedes mencionarme algunos personajes relevantes de Rosario?"))
dataset.append((1, "¿Qué figuras históricas son famosas en Rosario?"))
dataset.append((1, "¿Cuáles son los personajes ilustres de la ciudad de Rosario?"))
dataset.append((1, "¿Qué personalidades han dejado una marca en la historia de Rosario?"))
dataset.append((1, "¿Hay algún personaje emblemático que deba conocer en Rosario?"))
dataset.append((1, "¿Quiénes son los héroes locales de Rosario?"))
dataset.append((1, "¿Cuáles son los líderes históricos más destacados de Rosario?"))
dataset.append((1, "¿Me podrías contar acerca de algunas figuras relevantes en la historia de Rosario?"))
dataset.append((1, "¿Qué personajes notables han nacido o vivido en Rosario?"))
dataset.append((1, "¿Quiénes son los personajes más influyentes en la historia cultural de Rosario?"))
dataset.append((1, "¿Cuáles son los nombres más reconocidos en la historia de Rosario?"))
dataset.append((1, "¿Puedes recomendarme algunos personajes históricos para investigar sobre Rosario?"))
dataset.append((1, "¿Hay alguna figura histórica cuya vida sea interesante de conocer en Rosario?"))


# Preparar X e y
X = [text.lower() for _, text in dataset]
y = [label for label, _ in dataset]

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

#Ingresar una frase y ver la prediccion
# frase = "Quiero saber la vida de algun personaje"
# frase_vectorizada = vectorizer.transform([frase.lower()])
# prediccion = modelo_LR.predict(frase_vectorizada)
# print(prediccion)
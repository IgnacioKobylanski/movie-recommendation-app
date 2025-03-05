import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Conexión a la base de datos MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  
        user="root",
        password="root36",
        database="movie_recommendation"
    )

# Función para obtener las películas desde MySQL
def get_movies_from_db():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT title, genre, description FROM movies")
    movies = cursor.fetchall()
    
    conn.close()
    
    return movies

# Convertir las descripciones en vectores de números
def get_recommendations(title):
    movies = get_movies_from_db()
    
    # Si la base de datos está vacía
    if not movies:
        return {"error": "❌ La base de datos de películas está vacía."}
    
    # Verificar si la película existe
    movie_titles = [movie['title'] for movie in movies]
    if title not in movie_titles:
        return {"error": f"❌ La película '{title}' no está en la base de datos."}
    
    # Obtener la descripción de la película seleccionada
    movie = next(movie for movie in movies if movie['title'] == title)
    descriptions = [movie['description'] for movie in movies]
    
    # Convertir las descripciones en vectores numéricos
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(descriptions)
    
    # Calcular la similitud de coseno entre las películas
    idx = movie_titles.index(title)
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix)
    
    # Obtener las puntuaciones de similitud entre la película seleccionada y todas las demás
    sim_scores = list(enumerate(cosine_sim[0]))
    
    # Ordenar las películas por similitud (más alta primero)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Evitar errores si hay menos de 5 películas
    sim_scores = sim_scores[1:6] if len(sim_scores) > 1 else []
    
    # Obtener los índices de las películas recomendadas
    movie_indices = [i[0] for i in sim_scores]
    
    # Crear una lista con los títulos de las películas recomendadas
    recommendations = [movies[i]['title'] for i in movie_indices]
    
    # Devolver las recomendaciones en formato de diccionario
    return {"recommendations": recommendations}






""" import mysql.connector
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Conexión a la base de datos MySQL
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  
        user="root",
        password="root36",
        database="movie_recommendation"
    )


# Función para obtener las películas desde MySQL
def get_movies_from_db():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT title, genre, description FROM movies")
    movies = cursor.fetchall()
    
    conn.close()
    
    return movies

# Convertir las descripciones en vectores de números
def get_recommendations(title):
    movies = get_movies_from_db()
    
    # Si la base de datos está vacía
    if not movies:
        return json.dumps({"error": "❌ La base de datos de películas está vacía."})
    
    # Verificar si la película existe
    movie_titles = [movie['title'] for movie in movies]
    if title not in movie_titles:
        return json.dumps({"error": f"❌ La película '{title}' no está en la base de datos."})
    
    # Obtener la descripción de la película seleccionada
    movie = next(movie for movie in movies if movie['title'] == title)
    descriptions = [movie['description'] for movie in movies]
    
    # Convertir las descripciones en vectores numéricos
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(descriptions)
    
    # Calcular la similitud de coseno entre las películas
    idx = movie_titles.index(title)
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix)
    
    # Obtener las puntuaciones de similitud entre la película seleccionada y todas las demás
    sim_scores = list(enumerate(cosine_sim[0]))
    
    # Ordenar las películas por similitud (más alta primero)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Evitar errores si hay menos de 5 películas
    sim_scores = sim_scores[1:6] if len(sim_scores) > 1 else []
    
    # Obtener los índices de las películas recomendadas
    movie_indices = [i[0] for i in sim_scores]
    
    # Devolver las recomendaciones en formato JSON
    recommendations = [movies[i]['title'] for i in movie_indices]
    
    return json.dumps({"recommendations": recommendations})

# Prueba de la función
print(get_recommendations('The Matrix'))

 """
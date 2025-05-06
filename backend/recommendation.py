import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Conexion con MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  
        user="root",
        password="root36", 
        database="movie_recommendation"
    )

# Función para obtener las películas de la base de datos
def get_movies_from_db():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Seleccionar id, título, descripción e imagen de la película
    cursor.execute("SELECT id, title, genre, description, image_url FROM movies")
    movies = cursor.fetchall()
    
    conn.close()
    
    return movies

# Convertir las descripciones en vectores de números
def get_recommendations(title):
    # Obtener todas las películas de la base de datos
    movies = get_movies_from_db()
    
    # Si no hay películas en la base de datos, devolver un error.
    if not movies:
        return {"error": "❌ The databse is empty."}
    
    # Convertir los títulos a minúsculas para hacer la búsqueda insensible a mayúsculas
    movie_titles = [movie['title'].lower() for movie in movies]
    
    # Verificar si el título existe en la base de datos (sin tener en cuenta mayúsculas)
    if title.lower() not in movie_titles:
        return {"error": f"❌ The movie: '{title}' is not in the database."}
    
    # Obtener la descripción de la película
    movie = next(movie for movie in movies if movie['title'].lower() == title.lower())
    descriptions = [movie['description'] for movie in movies]
    
    # Convertir las descripciones en vectores numéricos
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(descriptions)
    
    # Calcular la similitud de coseno entre la película seleccionada y las demás
    idx = movie_titles.index(title.lower()) 
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix)
    
    # Obtener las puntuaciones de similitud entre la película seleccionada y todas las demás
    sim_scores = list(enumerate(cosine_sim[0]))
    
    # Ordenar las películas por similitud (de alta a baja)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Evitar errores si hay menos de 5 películas
    sim_scores = sim_scores[1:6] if len(sim_scores) > 1 else []
    
    # Obtener los índices de las películas recomendadas
    movie_indices = [i[0] for i in sim_scores]
    
    # Crear una lista con los títulos de las películas recomendadas y sus respectivas URLs de imágenes
    recommendations = [{
        "name": movies[i]['title'],
        "imageUrl": movies[i]['image_url'],
        "description":movies[i]['description']
    } for i in movie_indices]
    
    # Devolver las recomendaciones en formato de diccionario
    return {"recommendations": recommendations}



""" import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Conexion con MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  
        user="root",
        password="root36", 
        database="movie_recommendation"
    )

# Función para obtener las películas de la bbdd
def get_movies_from_db():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT title, genre, description FROM movies")
    movies = cursor.fetchall()
    
    conn.close()
    
    return movies

# Convertir las descripciones en vectores de números
def get_recommendations(title):
    # Obtener todas las películas de la base de datos
    movies = get_movies_from_db()
    
    # Si no hay películas en la base de datos, devolver un error.
    if not movies:
        return {"error": "❌ La base de datos de películas está vacía."}
    
    # Convertir los títulos a minúsculas para hacer la búsqueda insensible a mayúsculas
    movie_titles = [movie['title'].lower() for movie in movies]
    
    # Verificar si el título existe en la base de datos (sin tener en cuenta mayúsculas)
    if title.lower() not in movie_titles:
        return {"error": f"❌ La película '{title}' no está en la base de datos."}
    
    # Imprimir la lista de títulos de películas para depuración
    print("Películas en la base de datos:", movie_titles)  # Verifica qué películas hay en la base de datos
    
    # Obtener la descripción de la película
    movie = next(movie for movie in movies if movie['title'].lower() == title.lower())  # Asegúrate de que no haya problemas con mayúsculas
    descriptions = [movie['description'] for movie in movies]
    
    # Convertir las descripciones en vectores numéricos
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(descriptions)
    
    # Calcular la similitud de coseno entre la película seleccionada y las demás
    idx = movie_titles.index(title.lower()) 
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix)
    
    # Obtener las puntuaciones de similitud entre la película seleccionada y todas las demás
    sim_scores = list(enumerate(cosine_sim[0]))
    
    # Ordenar las películas por similitud (de alta a baja)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Evitar errores si hay menos de 5 películas
    sim_scores = sim_scores[1:6] if len(sim_scores) > 1 else []
    
    # Obtener los índices de las películas recomendadas
    movie_indices = [i[0] for i in sim_scores]
    
    # Crear una lista con los títulos de las películas recomendadas
    recommendations = [movies[i]['title'] for i in movie_indices]
    
    # Devolver las recomendaciones en formato de diccionario
    return {"recommendations": recommendations} """
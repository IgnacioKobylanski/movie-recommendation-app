import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Datos de ejemplo de películas
movies = pd.DataFrame({
    'title': ['The Matrix', 'Interstellar', 'The Dark Knight', 'Inception', 'The Godfather'],
    'genre': ['Sci-Fi, Action', 'Sci-Fi, Drama', 'Action, Drama', 'Sci-Fi, Action', 'Drama, Crime'],
    'description': [
        'A man discovers that the world is a simulation.',
        'A group of astronauts travels through a wormhole to save Earth.',
        'A vigilante fights crime in Gotham City.',
        'A thief enters the dreams of others to steal secrets.',
        'The story of a mafia family in New York.'
    ]
})

# Convertir las descripciones en vectores numéricos
tfidf = TfidfVectorizer(stop_words='english')  # Eliminar las palabras comunes
tfidf_matrix = tfidf.fit_transform(movies['description']) 

# Calcular la similitud de coseno entre las películas
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_recommendations(title, cosine_sim=cosine_sim):
    # Obtener el índice de la película seleccionada
    idx = movies.index[movies['title'] == title].tolist()
    
    # Si el título no se encuentra, se termina la busqueda
    if not idx:
        return f"La película '{title}' no se encuentra en la base de datos."
    
    idx = idx[0]  # Obtener el 1er índice
    
    # Imprimir el índice para depurar
    print(f"Índice de la película '{title}': {idx}")
    
    # Obtener las puntuaciones de similitud entre la película seleccionada y todas las demás
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Imprimir las similitudes para depuración
    print(f"Similitudes calculadas para '{title}': {sim_scores}")
    
    # Ordenar las películas por similitud (más alta primero)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Obtener los índices de las 5 películas más similares (excluyendo la propia película)
    sim_scores = sim_scores[1:6]  # Top 5 más similares
    movie_indices = [i[0] for i in sim_scores]
    
    # Imprimir los índices de las películas más similares para depuración
    print(f"Índices de las películas más similares: {movie_indices}")
    
    # Devolver los títulos de las películas más similares
    return movies['title'].iloc[movie_indices]

# testeo
print(get_recommendations('The Matrix'))

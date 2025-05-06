import mysql.connector
import csv

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",  
            user="root",
            password="root36", 
            database="movie_recommendation"
        )
        print("Conexión a la base de datos exitosa!")
        return conn
    except mysql.connector.Error as err:
        print(f"Error de conexión a la base de datos: {err}")
        return None

def load_movies_from_csv():
    conn = get_db_connection()
    if not conn:
        return  # Si la conexión falla, no continuamos

    cursor = conn.cursor()

    try:
        with open('movies.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                title = row['title']
                genre = row['genre']
                description = row['description']
                image_url = row['image_url']
                
                # Imprimir los datos que estamos intentando insertar
                print(f"Inserting movie: {title}, {genre}, {description}, {image_url}")

                try:
                    cursor.execute('''INSERT INTO movies (title, genre, description, image_url) 
                                      VALUES (%s, %s, %s, %s)''', 
                                   (title, genre, description, image_url))
                    print(f"Película '{title}' insertada correctamente.")
                except mysql.connector.Error as err:
                    print(f"Error al insertar la película '{title}': {err}")

        conn.commit()
        print("Todas las películas fueron insertadas exitosamente!")

    except FileNotFoundError:
        print("El archivo movies.csv no fue encontrado.")
    except Exception as err:
        print(f"Hubo un error inesperado: {err}")
    finally:
        cursor.close()
        conn.close()

load_movies_from_csv()

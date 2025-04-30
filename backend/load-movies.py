import mysql.connector
import csv

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  
        user="root",
        password="root36", 
        database="movie_recommendation"
    )

def load_movies_from_csv():
    conn = get_db_connection()
    cursor = conn.cursor()

    with open('movies.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            title = row['title']
            genre = row['genre']
            description = row['description']
            image_url = row['image_url']
            
            cursor.execute('''INSERT INTO movies (title, genre, description, image_url) 
                              VALUES (%s, %s, %s, %s)''', 
                           (title, genre, description, image_url))

    conn.commit()
    cursor.close()
    conn.close()

load_movies_from_csv()
print("movies successfully uploaded!")

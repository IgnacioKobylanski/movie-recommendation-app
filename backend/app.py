from flask import Flask, request, jsonify
from flask_cors import CORS
from recommendation import get_recommendations  # Asegúrate de tener este archivo 'recommendation.py'

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir que tu frontend pueda hacer peticiones al backend

@app.route('/recommendations', methods=['GET'])
def recommendations():
    # Obtener el parámetro 'title' desde la URL
    title = request.args.get('title')

    # Validar que el título no esté vacío o solo con espacios
    if not title or title.strip() == "":
        return jsonify({"error": "El título de la película no puede estar vacío."}), 400

    try:
        # Obtener las recomendaciones llamando a la función get_recommendations
        recommendations = get_recommendations(title)

        # Verificar si la función devuelve un mensaje de error (en caso de no encontrar la película)
        if "error" in recommendations:
            return jsonify(recommendations), 400

        # Si todo está bien, devolvemos las recomendaciones en formato JSON
        return jsonify({"recommendations": recommendations["recommendations"]})

    except Exception as e:
        # Si ocurre un error inesperado, devolvemos un mensaje de error general
        return jsonify({"error": str(e)}), 500  # Error interno del servidor

if __name__ == '__main__':
    app.run(debug=True)
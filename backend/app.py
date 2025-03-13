from flask import Flask, request, jsonify
from flask_cors import CORS 
from recommendation import get_recommendations

app = Flask(__name__)
CORS(app)  # Habilitar CORS

@app.route('/recommendations', methods=['GET'])
def recommendations():
    # Obtener el parámetro 'title' desde la URL
    title = request.args.get('title')

    if not title:
        # Si no hay título, devuelve un error
        return jsonify({"error": "Por favor, proporciona un título de película usando el parámetro 'title' en la URL."}), 400

    # Obtener las recomendaciones llamando a la función get_recommendations
    recommendations = get_recommendations(title)

    # Verificar si la función devuelve un mensaje de error (en caso de no encontrar la película)
    if "error" in recommendations:
        return jsonify(recommendations), 400

    # Si todo está bien, devolvemos las recomendaciones en formato JSON
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)



""" from flask import Flask, request, jsonify
from recommendation import get_recommendations

app = Flask(__name__)
# Pseudo Main
@app.route('/recommendations')
def recommendations():
    # Obtener el parámetro 'title'
    title = request.args.get('title')

    if not title:
        return "Por favor, proporciona un título de película usando el parámetro 'title' en la URL.", 400 #mensaje para el usuario
    
    # Obtener las recomendaciones seleccionadas
    recommendations = get_recommendations(title)

    # Verificar que la función devuelve.
    if isinstance(recommendations, str):
        return recommendations  # En caso de que sea un mensaje de error

    # Convertir el resultado a una lista y devolverlo como JSON
    return jsonify(recommendations.tolist())  # Usamos .tolist() para convertir el Series a lista

if __name__ == '__main__':
    app.run(debug=True)
 """
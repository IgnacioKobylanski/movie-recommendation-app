from flask import Flask, request, jsonify
from recommendation import get_recommendations

app = Flask(__name__)

@app.route('/recommendations')
def recommendations():
    # Obtener el parámetro 'title' de la URL
    title = request.args.get('title')

    if not title:
        return "Por favor, proporciona un título de película usando el parámetro 'title' en la URL.", 400 #mensaje de holder
    
    # Obtener las recomendaciones seleccionadas
    recommendations = get_recommendations(title)

    # Verificar que la función devuelve algo
    if isinstance(recommendations, str):
        return recommendations  # En caso de que sea un mensaje de error

    # Convertir el resultado a una lista y devolverlo como JSON
    return jsonify(recommendations.tolist())  # Usamos .tolist() para convertir el Series a lista

if __name__ == '__main__':
    app.run(debug=True)

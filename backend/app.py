from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, mundo! Esto es Flask."

if __name__ == '__main__':
    app.run(debug=True)
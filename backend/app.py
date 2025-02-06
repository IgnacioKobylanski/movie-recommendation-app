from flask import Flask
from recommendation import get_recommendations

app = Flask(__name__)

@app.route('/recommendations')
def recommendations():
    return get_recommendations()

if __name__ == '__main__':
    app.run(debug=True)

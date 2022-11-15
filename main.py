from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    model = {'message':"mon api fonctionne",
            'status': 200}
    return jsonify(model)

@app.route('/test', methods=['GET'])
def test():
    model = {'message':"une super réponse",
        'status': 200}
    return jsonify(model)

################################ MAIN ############################################

if __name__ == "__main__":
    app.run()

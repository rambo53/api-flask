from flask import Flask
from flask_json import FlaskJSON, json_response
from flask_cors import CORS


app = Flask(__name__)
FlaskJSON(app)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return json_response("mon api fonctionne")

@app.route('/test', methods=['GET'])
def test():
    return json_response("une super réponse")

################################ MAIN ############################################

if __name__ == "__main__":
    app.run()
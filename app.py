from flask import Flask
from flask import jsonify
import usacorona

app = Flask(__name__)


@app.route('/total', methods=['GET'])
def tot():
    return jsonify(usacorona.f)

@app.route('/')
def index():
    return jsonify(usacorona.d)
if __name__=="__main__":
    app.run(threaded=True, port=5000)

import os

from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from trimmer import Trimmer

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return "hello world"


@app.route('/trim', methods=["POST"])
def trim_post():
    trimmer = Trimmer()
    return jsonify({'text': trimmer.trim(request.get_data(as_text=True))}, 200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

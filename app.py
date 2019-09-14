import os

from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from trimtr.trimmer import Trimmer
from scout_apm.flask import ScoutApm

app = Flask(__name__)
CORS(app)
ScoutApm(app)

app.config["SCOUT_MONITOR"] = os.environ.get("SCOUT_MONITOR")
app.config["SCOUT_KEY"] = os.environ.get("SCOUT_KEY")
app.config["SCOUT_NAME"] = "trimtr"


@app.route('/', methods=['GET'])
def index():
    return "hello world"


@app.route('/trim', methods=["POST"])
def trim_post():
    trimmer = Trimmer.get_instance()
    return jsonify({'text': trimmer.trim(request.get_data(as_text=True))}, 200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

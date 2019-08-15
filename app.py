from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from trimmer import trim

app = Flask(__name__)
CORS(app)


@app.route('/trim', methods=["POST"])
def trim_post():
    return jsonify({'text': trim(request.get_data(as_text=True))}, 200)


if __name__ == '__main__':
    app.run()

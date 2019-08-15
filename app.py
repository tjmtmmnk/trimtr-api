from flask import Flask
from flask import request
from trimmer import trim

app = Flask(__name__)


@app.route('/trim', methods=["POST"])
def trim_post():
    return trim(request.get_data(as_text=True))


if __name__ == '__main__':
    app.run()

from flask import Flask
from flask import request
from trimmer import trim

app = Flask(__name__)


@app.route('/trim', methods=["POST"])
def trim_post():
    trim(request.get_data(as_text=True))
    return request.get_data()


if __name__ == '__main__':
    app.run()

import flask
import time

app = flask.Flask(__name__)


@app.route("/")
def index():
    return "Welcome!!ddddddddd", time.localtime

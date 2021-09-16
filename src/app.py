import flask, time

app = flask.Flask(__name__)


@app.route("/")
def index():
    return "Welcome!!2!test ",time.localtime

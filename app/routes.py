from flask import Flask


app = Flask(__name__)


@app.get("/")
def index():
    me = {
        "first_name": "Vicky",
        "last_name": "Warren",
        "hobbies": "writing children's poetry"
    }
    return me
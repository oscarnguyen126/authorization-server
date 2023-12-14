import gunicorn
from flask import Flask
from database.db import create_tables

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

create_tables()

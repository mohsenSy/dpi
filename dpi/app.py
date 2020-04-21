from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object("dpi.settings")

db = SQLAlchemy(app)

from .models import HTTPrequest

@app.route("/")
def index():
    return render_template("index.html", requests = HTTPrequest.get_requests())

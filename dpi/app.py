from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object("dpi.settings")

db = SQLAlchemy(app)

from .models import HTTPrequest, TCPPacket

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/http")
def http():
    page = request.args.get("page", 0)
    per_page = request.args.get("per_page", 20)
    return render_template("http.html", requests = HTTPrequest.get_requests(page, per_page))

@app.route("/tcps")
def tcp():
    page = request.args.get("page", 0)
    per_page = request.args.get("per_page", 20)
    return render_template("tcp.html", tcps = TCPPacket.get_tcp(page, per_page))

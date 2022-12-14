
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")

@app.route("/g")
def indexc():
    return render_template("ga.html")

@app.route("/ga")
def indexcq():
    return render_template("ququ.html")
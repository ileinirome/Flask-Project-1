# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from model import get_definition
from datetime import datetime


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time=datetime.now())



@app.route("/results", methods = ["GET", "POST"])
def results():
    if request.method == "POST":
        vocab_term = request.form["vocab_term"]
        vocab_def = get_definition(vocab_term)
        return render_template("results.html", time=datetime.now(), vocab_term = vocab_term, vocab_def = vocab_def)
    else:
        return redirect('/')
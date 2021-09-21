from flask import Flask, render_template
from flask.helpers import flash

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("potato.html")

app.run()
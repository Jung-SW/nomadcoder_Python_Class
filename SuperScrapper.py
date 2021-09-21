from flask import Flask
from flask.helpers import flash

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return "Hello! Welcome to mi casa!"

@app.route("/contact")
def contact():
    return "Contact me!"
app.run()
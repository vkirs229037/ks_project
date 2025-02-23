from flask import Flask, render_template, redirect
import os
import db

app = Flask(__name__)
app.config["DATABASE"] = os.path.dirname(os.path.realpath(__file__)) + "/data/books.db"

@app.route("/")
def root():
    return redirect("/library")

@app.route("/library")
def index():
    return render_template("index.html")

@app.route("/library/search")
def search():
    return render_template("search.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    db.init()
    app.run(host="0.0.0.0", port=9000, debug=True)
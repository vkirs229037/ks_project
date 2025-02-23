from flask import Flask, render_template, redirect, request
import os
import db

app = Flask(__name__)

@app.route("/")
def root():
    return redirect("/library")

@app.route("/library")
def index():
    return render_template("index.html")

@app.route("/library/search")
def search():
    return render_template("search.html")

@app.route("/api/search")
def search_lib():
    title = request.args.get('title')
    if title == "": title = None
    author = request.args.get('author')
    if author == "": author = None
    year = request.args.get('year')
    if year == "": year = None
    desc = request.args.get('desc')
    if desc == "": desc = None
    return db.search(title, author, year, desc)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    db.init()
    app.run(host="0.0.0.0", port=9000, debug=True)
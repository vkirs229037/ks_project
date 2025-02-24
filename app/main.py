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

@app.route("/library/<bookid>")
def book(bookid):
    info = db.get(bookid)
    if info is None:
        return redirect("/library/search")
    else: 
        return render_template("book.html", title=info[1], author=info[2], year=info[3], desc=info[4])

@app.route("/api/search")
def search_lib():
    title = request.args.get('title')
    author = request.args.get('author')
    year = request.args.get('year')
    desc = request.args.get('desc')
    print("DEBUG:", title, author, year, desc)
    if title == "": title = None
    if author == "": author = None
    if year == "": year = None
    if desc == "": desc = None
    return db.search(title, author, year, desc)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    db.init()
    app.run(host="0.0.0.0", port=9000, debug=True)
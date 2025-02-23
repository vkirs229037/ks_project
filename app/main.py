from flask import Flask, render_template, redirect

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

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/api/test")
def test():
    return {"My final message": "Change da world... Goodbye..."}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
from flask import Flask

app = Flask(__name__)

@app.route("/app/")
def hello_world():
    return "Hello, world!"

@app.route("/app/number/<num>")
def new(num):
    return f"Число {num}"

if __name__ == "__main__":
    app.run(debug=True)
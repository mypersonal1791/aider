from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "hello world"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return str(a + b)

if __name__ == "__main__":
    app.run(debug=True)

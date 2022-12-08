from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def addition():
    a = int(request.args.get('a', 5))
    b = int(request.args.get('b', 5))
    return str(add(a, b))


@app.route("/sub")
def subtraction(a, b):
    a = int(request.args.get('a', 5))
    b = int(request.args.get('b', 5))
    return str(sub(a, b))


@app.route("/div")
def division(a, b):
    a = int(request.args.get('a', 5))
    b = int(request.args.get('b', 5))
    return str(div(a, b))


@app.route("/mult")
def multiplication(a, b):
    a = int(request.args.get('a', 5))
    b = int(request.args.get('b', 5))
    return str(mult(a, b))

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def addition():
    """Add a and b parameters."""
    a = int(request.args.get('a', 5))
    b = int(request.args.get('b', 5))
    return str(add(a, b))


@app.route("/sub")
def subtraction():
    """substract a and b parameters."""
    a = int(request.args.get('a', 5))
    b = int(request.args.get('b', 5))
    return str(sub(a, b))


@app.route("/div")
def division():
    """Divide a and b parameters."""
    a = int(request.args.get('a', 5))
    b = int(request.args.get('b', 5))
    return str(div(a, b))


@app.route("/mult")
def multiplication():
    """Multiply a and b parameters."""
    a = int(request.args.get('a', 5))
    b = int(request.args.get('b', 5))
    return str(mult(a, b))


@app.route("/math/<operation>")
def calculate(operation):
    """Add,mult,div,sub a and b parameters."""
    operators = {'add': add, 'sub': sub, 'mult': mult, 'div': div}
    a = int(request.args.get('a', 5))
    b = int(request.args.get('b', 5))
    return f'<h1>{a} {operation} {b} = {operators[operation](a,b)}</h1>'
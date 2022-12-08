from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def addition():
    a = int(request.args.get('a', 5))
    b = int(request.args.get('b', 5))
    return str(add(a, b))


@app.route("/sub")
def subtraction():
    a = int(request.args.get('a', 5))
    b = int(request.args.get('b', 5))
    return str(sub(a, b))


@app.route("/div")
def division():
    a = int(request.args.get('a', 5))
    b = int(request.args.get('b', 5))
    return str(div(a, b))


@app.route("/mult")
def multiplication():
    a = int(request.args.get('a', 5))
    b = int(request.args.get('b', 5))
    return str(mult(a, b))


@app.route("/math/<operation>")
def calculate(operation):
    oprtns = {'add': add, 'sub': sub, 'mult': mult, 'div': div}
    a = int(request.args.get('a', 5))
    b = int(request.args.get('b', 5))
    return f'<h1>{a} {operation} {b} = {oprtns[operation](a,b)}</h1>'
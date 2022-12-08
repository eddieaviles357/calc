from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/<operation>")
def calculate(operation):
    oprtns = {'add': add, 'sub': sub, 'mult': mult, 'div': div}
    a = int(request.args.get('a', 5))
    b = int(request.args.get('b', 5))
    return f'<h1>{a} {operation} {b} = {oprtns[operation](a,b)}</h1>'

from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_page():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = add(a, b)
    return str(answer)
    

@app.route('/sub')
def sub_page():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = sub(a, b)
    return str(answer)

@app.route('/mult')
def mult_page():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = mult(a, b)
    return str(answer)


@app.route('/div')
def div_page():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = div(a, b)
    return str(answer)








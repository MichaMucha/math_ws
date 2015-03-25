from flask import Flask, request
from functools import reduce
import json

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.form['values']
    elif request.method == 'GET':
        data = request.args.get('values')

    try:
        values = json.loads(data)
    except:
        return 'Hello! Please send list of values through POST or GET.'

    return json.dumps(math(values))

def math(values):
    result = {
        'sum' : sum(values),
        'product' : reduce(lambda x, y: x*y, values)
    }
    return result

if __name__ == '__main__':
    app.run()

#!/usr/bin/python3
"""Flask web with three routes is launched."""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Route with "Hello HBNB!" message"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """The route with "HBNB" shows"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """print C and the text variables value after that."""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)

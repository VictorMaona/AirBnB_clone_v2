#!/usr/bin/python3
""" Launch an instance of the Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """send back the string Hello HBNB!"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
""" Launching a Flask web application script """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Route that reads 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ The route that shows  'HBNB' """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ Route that shows C and text variable value after """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """Route that shows "Python" and,

    the text variables value cool by default.
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ route that shows 'n is a number' n is an integer """
    return '{} is number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ shows HTML page when <n> is an integer. """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ n is even or odd integer only shows HTML page """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000)

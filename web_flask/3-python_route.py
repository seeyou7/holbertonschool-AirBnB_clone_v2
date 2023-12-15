#!/usr/bin/python3
"""Start a Flask web application on localhost"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display a message when making a request to root"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display message HBNB!"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def dynamic_text(text=None):
    """Display “C ” + var value using dynamic routing """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python',  strict_slashes=False)
@app.route('/python/<string:text>',  strict_slashes=False)
def python_dynamic(text="is cool"):
    """ display  dynamic“Python ”, followed by the value of the text var """
    return "python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    """run app flask"""
    app.run(host='0.0.0.0', port=5000)

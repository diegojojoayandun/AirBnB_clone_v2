#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    display "Hello HBNB!"
    """
    return '{}'.format("Hello HBN")


if __name__ == '__main__':
    app.run(host='0.0.0.0')

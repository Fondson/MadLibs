# -*- coding: utf-8 -*-
"""
    jQuery Example
    ~~~~~~~~~~~~~~
    A simple application that shows how Flask and jQuery get along.
    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/_add_number')
def add_number():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a')
    b = request.args.get('b')
    return jsonify(result=a + " " + b)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A very simple Flask Hello World app for you to get started with...

import flask
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


def gcd(x : 'int', y : 'int') -> 'int' :
    while y != 0 :
        x, y = y, (x % y)
    return (x)

@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/gcd', methods = ['GET'])
def hello_name():
    if request.method == 'GET':
        a_param=request.args.get('a')
        b_param=request.args.get('b')

    c = False
    if a_param==None or b_param==None:
        a_param="0"
        b_param="0"
        c = True

    if not c:
        result = str(gcd(int(a_param), int(b_param)))
    else:
        result = "Введите параметры"

    return flask.render_template(
        'gcd.html',
        gcd=result
    )

if __name__ == '__main__':
   app.run(debug = True)

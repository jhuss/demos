# coding=utf-8
# flask & env demo
__author__ = 'Jesús Jerez <jerezmoreno@gmail.com>'


from os import getenv
from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return '{0}'.format(getenv('MSG'))

    return app
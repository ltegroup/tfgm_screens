import logging
from datetime import datetime

from flask import Flask, render_template, send_from_directory
from flask_simpleldap import LDAP

from settings import *

app = Flask(__name__)
app.secret_key = SECRET_KEY

# make gunicorn and application logging show together
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

@app.route("/")
def index():
    return send_from_directory('static', 'index.html')

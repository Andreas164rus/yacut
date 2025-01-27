from http import HTTPStatus

from flask import render_template, jsonify

from . import app
from .exceptions import InvalidAPIUsage


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code
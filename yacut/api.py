from flask import jsonify, request

from . import app, db
from .models import URLMap
from .error_handlers import InvalidAPIUsage
from .utils import object_short_link, get_unique_short_id
from .validation import validation_short_link
from .constants import (NO_VALID_SHORT_LINK, LINK_IN_DB,
                        REQUIRED_URL, NO_BODY_IN_REQUEST, NO_FOUND)


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_link(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if not url:
        raise InvalidAPIUsage(NO_FOUND, 404)
    return jsonify({'url': url.original})


@app.route('/api/id/', methods=['POST'])
def create_short_link():
    data = request.get_json(silent=True)
    if not data:
        raise InvalidAPIUsage(NO_BODY_IN_REQUEST)
    original_link = data.get('url')
    if not original_link:
        raise InvalidAPIUsage(REQUIRED_URL)
    custom_id = data.get('custom_id')
    if not custom_id:
        custom_id = get_unique_short_id()
    url_map = URLMap.query.filter_by(original=original_link)
    if URLMap.query.filter_by(short=custom_id).first() is not None:
        raise InvalidAPIUsage(LINK_IN_DB)
    if not validation_short_link(custom_id):
        raise InvalidAPIUsage(NO_VALID_SHORT_LINK)
    url_map = object_short_link(original_link, custom_id)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), 201

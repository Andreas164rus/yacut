# what_to_watch/opinions_app/api_views.py

# Импортируем метод jsonify:
from flask import jsonify, request

from . import app, db
from .models import URLMap
from .error_handlers import InvalidAPIUsage
from .utils import object_short_link, short_link_in_db_exists
from .validation import validation_short_link
from .constants import NO_VALID_SHORT_LINK


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_link(short_id):
    if URLMap.query.filter_by(short=short_id).first():
        url = URLMap.query.get(short_id).original
        return jsonify({'url': url}), 200
    raise InvalidAPIUsage('Не найдено', 404)


@app.route('/api/id/', methods=['POST'])
def add_opinion():
    # print(request.data)
    data = request.get_json(silent=True)
    if not data:
        raise InvalidAPIUsage("Отсутствует тело запроса")
    original_link = data.get('url')
    if original_link is None:
        raise InvalidAPIUsage("\"url\" является обязательным полем!")
    short_link = data.get('custom_id')
    url_map = URLMap.query.filter_by(original=original_link)
    if url_map.first() is not None:
        return jsonify(url_map.first().to_dict()), 200
    if short_link_in_db_exists(short_link):
        raise InvalidAPIUsage("Предложенный вариант короткой ссылки уже существует.")
    if short_link:
        if not validation_short_link(short_link):
            raise InvalidAPIUsage(NO_VALID_SHORT_LINK)
        url_map = object_short_link(original_link, short_link)
    else:
        url_map = object_short_link(original_link)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), 201


    print(original_link, short_link)
    return {123}
    # if 'title' not in data or 'text' not in data:
    #     raise 'gay' #InvalidAPIUsage('В запросе отсутствуют обязательные поля')
    
    # # if Opinion.query.filter_by(text=data['text']).first() is not None:
    # #     raise InvalidAPIUsage('Такое мнение уже есть в базе данных')
    # # opinion = Opinion()
    # # opinion.from_dict(data)
    # # db.session.add(opinion)
    # # db.session.commit()
    # return jsonify({'opinion': opinion.to_dict()}), 201
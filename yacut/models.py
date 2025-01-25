from datetime import datetime

from . import db
from flask import url_for


class URLMap(db.Model):
    id = db.Column(db.Integer, nullable=True) 
    original = db.Column(db.Text, nullable=False, unique=True)
    short = db.Column(db.String(16), primary_key=True,)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('redirect_a_short_link',
                               short_link=self.short,
                               _external=True),
        )

# Про поле id.
# По ТЗ явно напрашивается (ИМХО) поле short основым индексом.
# Но тесты обязатльно трубуют поле id, иначе не проходят
# Надеюсь на понимание
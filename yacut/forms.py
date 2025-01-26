from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from .constants import REGEX_VALIDATE


class URLSForm(FlaskForm):
    original_link = URLField(
        'Введите оригинальную ссылку',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = URLField(
        'Ваш вариант корткой ссылки',
        validators=[Length(1, 16), Optional(), Regexp(REGEX_VALIDATE)]
    )
    submit = SubmitField('Создать')
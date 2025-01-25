from flask import flash, redirect, render_template, abort
from .utils import (object_short_link, short_link_in_db_exists,
                    collect_short_link)
from . import app, db
from .forms import URLSForm
from .models import URLMap
from .constants import SHORT_LINK_IN_DB, NO_VALID_SHORT_LINK
from .validation import validation_short_link


@app.route('/', methods=['GET', 'POST'])
def get_unique_short_id():
    form = URLSForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        short_link = form.custom_id.data
        if URLMap.query.filter_by(original=original_link).first() is not None:
            url_map = URLMap.query.filter_by(original=original_link).first()
            flash(f'{collect_short_link(url_map.short)}')
            return render_template('index.html', form=form)
        if short_link_in_db_exists(short_link):
            flash(f'{SHORT_LINK_IN_DB}')
            return render_template('index.html', form=form)
        if short_link:
            if not validation_short_link(short_link):
                flash(NO_VALID_SHORT_LINK)
                return render_template('main.html', form=form)
            url_map = object_short_link(original_link, short_link)
            flash(collect_short_link(url_map.short))
        else:
            url_map = object_short_link(original_link)
            flash(collect_short_link(url_map.short))
        db.session.add(url_map)
        db.session.commit()
    return render_template('main.html', form=form)


@app.route('/<string:short_link>', methods=['GET'])
def redirect_a_short_link(short_link):
    if URLMap.query.filter_by(short=short_link).first():
        link = URLMap.query.get(short_link)
        return redirect(link.original)
    abort(404)

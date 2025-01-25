from flask import flash, redirect, render_template, abort
from .utils import (object_short_link,
                    collect_short_link, get_unique_short_id)
from . import app, db
from .forms import URLSForm
from .models import URLMap
from .constants import SHORT_LINK_IN_DB


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLSForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = get_unique_short_id()
        if URLMap.query.filter_by(short=custom_id).first() is not None:
            flash(f'{SHORT_LINK_IN_DB}')
            return render_template('main.html', form=form)
        url_map = object_short_link(original_link, custom_id)
        flash(f"<a href='{collect_short_link(url_map.short)}'>"
              f"{collect_short_link(url_map.short)}</a>")
        db.session.add(url_map)
        db.session.commit()
    return render_template('main.html', form=form)


@app.route('/<string:short_link>', methods=['GET'])
def redirect_a_short_link(short_link):
    link = URLMap.query.filter_by(short=short_link).first()
    if link:
        return redirect(link.original)
    abort(404)

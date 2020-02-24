from functools import wraps
from flask import url_for
from flask_login import current_user
from werkzeug.utils import redirect
from app import app


def admin_required(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        if current_user.is_anonymous or not current_user.is_admin:
            return redirect(url_for('index'))
        return func(*args, **kwargs)

    return wrapped


@app.template_filter('is_admin')
def is_admin(func):
    if not current_user.is_admin:
        return False
    return True

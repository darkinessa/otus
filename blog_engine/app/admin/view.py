from flask import request, url_for, flash, render_template
from flask_login import current_user
from werkzeug.utils import redirect

from app import app
from app.database import Session
from app.decorators import admin_required
from app.models import User, Rubric, Post


@app.route('/manage_rubrics', methods=['GET', 'POST'])
@admin_required
def manage_rubrics():
    session = Session()
    rubrics = session.query(Rubric).all()
    cheked_rubrics = request.form.getlist('checks')

    for checked_rubric in cheked_rubrics:

        rubric = session.query(Rubric).get(checked_rubric)

        if request.method == 'POST' and 'del' in request.form:

            if session.query(Post).filter_by(rubric_id=int(checked_rubric)).all():
                flash('Нельзя удалить рубрику в которой есть посты')

            session.delete(rubric)
            session.commit()
            flash(f'Рубрика {rubric} удалена')

            return redirect(url_for('manage_rubrics'))

    return render_template('admin/manage_rubrics.html', rubrics=rubrics)


@app.route('/add_rubric', methods=['POST'])
@admin_required
def add_rubric():
    session = Session()
    # user = session.query(User).filter_by(username=current_user.username).first()
    name = request.form.get('name')

    if name == '':
        flash('Заполните поле Название рубрики')
        return redirect(url_for('manage_rubrics'))
    if session.query(Rubric).filter_by(name=name).one_or_none():
        flash('Такая рубрика уже существует')
        return redirect(url_for('manage_rubrics'))
    if request.method == "POST" and name:
        rubric = Rubric(name=name)
        session.add(rubric)
        session.commit()
        flash('Рубрика успешно добавлена')

    return redirect(url_for('manage_rubrics'))


@app.route('/edit_rubric', methods=['POST'])
@admin_required
def edit_rubric():
    session = Session()
    rubrics = session.query(Rubric).all()
    return redirect(url_for('manage_rubrics', rubrics=rubrics))

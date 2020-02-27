import os

from flask import request, url_for, flash, render_template
from flask_login import current_user
from werkzeug.utils import redirect

from app import app
from app.database import Session
from app.decorators import admin_required
from app.models import User, Rubric, Post, Jumbotron
import pathlib


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
    '''здесь будет функционал'''
    session = Session()
    rubrics = session.query(Rubric).all()
    return redirect(url_for('manage_rubrics', rubrics=rubrics))


@app.route('/manage_jambo', methods=['GET', 'POST'])
@admin_required
def manage_jambo():
    session = Session()
    page_title = "Редактировать главный экран"

    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        emphasis = form.get('emphasis')
        text = form.get('text')
        img_link = form.get('img_link')
        error = None

        def check_empty_error(check_function, field_name, error_text):
            if check_function(field_name):
                return render_template('admin/jambo.html', field_with_error=field_name, error=error_text,
                                       title=title, text=text, emphasis=emphasis, img_link=img_link,
                                        page_title=page_title)

        def is_empty(field):
            return form.get(field).strip() == ''

        def check_img(field):
            if field.startswith('http'):
                return True
            file_path = 'app/static/img/' + field
            path = pathlib.Path(file_path)
            return path.is_file() is False


        fields = [
            (is_empty, 'title', 'Заполните поле: Заголовок'),
            (is_empty, 'emphasis', 'Заполните поле: Основная мысль'),
            (is_empty, 'text', 'Заполните поле:  Текст'),
            (is_empty, 'img_link', 'Заполните поле:  Ссылка на картинку'),
            (check_img, img_link, 'Неверная ссылка, такого файла не существует')
        ]

        for field in fields:
            check_f, field_name, error_text = field
            error = check_empty_error(check_f, field_name, error_text)
            if error:
                return error

        jambo = Jumbotron(title=title, emphasis=emphasis, text=text, img_link=img_link)
        session.add(jambo)
        session.commit()
        flash('Новое приветсвие добавленоо')
        return redirect(url_for('manage_jambo'))

    return render_template('admin/jambo.html', page_title=page_title)

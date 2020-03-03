from flask import request, url_for, flash, render_template
from werkzeug.utils import redirect

from app import app
from app.validators import check_img, is_empty
from app.database import Session
from app.decorators import admin_required
from app.models import Rubric, Jumbotron


@app.route('/manage_rubrics', methods=['GET', 'POST'])
@admin_required
def manage_rubrics():
    session = Session()
    rubrics = session.query(Rubric).all()
    cheked_rubrics = request.form.getlist('checks')

    for checked_rubric in cheked_rubrics:

        rubric = session.query(Rubric).get(checked_rubric)

        if request.method == 'POST' and 'del' in request.form:

            if rubric.posts_quantity > 0:
                flash('Нельзя удалить рубрику в которой есть посты')
                return redirect(url_for('manage_rubrics'))

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


@app.route('/add_jumbo', methods=['GET', 'POST'])
@admin_required
def add_jumbo(id=None):
    session = Session()
    form = request.form
    jumbos = session.query(Jumbotron).order_by(Jumbotron.active.desc(), Jumbotron.id.desc(), ).limit(10).all()
    page_title = "Редактировать главный экран"
    id = request.form.get('id')

    if request.method == 'POST' and 'save' in form:

        jumbo_title = form.get('jumbo_title')
        emphasis = form.get('emphasis')
        text = form.get('text')
        img_link = form.get('img_link')
        jumbo_id = form.get('id')
        error = None

        def check_empty_error(check_function, field_name, error_text):
            if check_function(field_name):
                return render_template('admin/jumbo.html', field_with_error=field_name, error=error_text,
                                       jumbo_title=jumbo_title, text=text, emphasis=emphasis, img_link=img_link,
                                       page_title=page_title)

        fields = [
            (is_empty, jumbo_title, 'Заполните поле: Заголовок'),
            (is_empty, emphasis, 'Заполните поле: Основная мысль'),
            (is_empty, text, 'Заполните поле:  Текст'),
            (is_empty, img_link, 'Заполните поле:  Ссылка на картинку'),
            (check_img, img_link, 'Неверная ссылка, такого файла не существует')
        ]

        for field in fields:
            check_f, field_name, error_text = field
            error = check_empty_error(check_f, field_name, error_text)
            if error:
                return error

        if not jumbo_id:
            jumbo = Jumbotron(title=jumbo_title, emphasis=emphasis, text=text, img_link=img_link)
            session.add(jumbo)
            flash('Новое приветсвие добавлено')
        else:
            jumbo = session.query(Jumbotron).get(jumbo_id)
            jumbo.title = jumbo_title
            jumbo.emphasis = emphasis
            jumbo.text = text
            jumbo.img_link = img_link

            flash(f'Приветсвие {jumbo.id} скопировано')

        session.commit()

        return redirect(url_for('add_jumbo'))

    if 'preview' in form:
        jumbo_title = form.get('jumbo_title')
        emphasis = form.get('emphasis')
        text = form.get('text')
        img_link = form.get('img_link')
        page_title = 'Предварительный просмотр'
        return render_template('public/index.html', page_title=page_title, jumbo_title=jumbo_title, text=text,
                               emphasis=emphasis, img_link=img_link)
    return render_template('admin/jumbo.html', page_title=page_title, jumbos=jumbos)


@app.route('/edit_jumbo', methods=['GET', 'POST'])
@admin_required
def edit_jumbo():
    session = Session()
    form = request.form
    jumbos = session.query(Jumbotron).order_by(Jumbotron.active.desc(), Jumbotron.id.desc(), ).limit(10).all()
    page_title = "Редактировать главный экран"
    checked_jumbos = request.form.getlist('checks')

    if 'del' in form:
        for checked_jumbo in checked_jumbos:
            jumbo = session.query(Jumbotron).get(checked_jumbo)
            if jumbo.active:
                flash('Нельзя удалить активный экран, сначала деактивируйте его')
                return redirect(url_for('add_jumbo'))

            session.delete(jumbo)
            flash(f'Приветсвие {jumbo} удалено')
            session.commit()

        return redirect(url_for('edit_jumbo'))

    if 'act' in form:
        for checked_jumbo in checked_jumbos:
            jumbo = session.query(Jumbotron).get(checked_jumbo)
            print(jumbo, jumbo.active)
            jumbo.active = True
            session.commit()
            flash(f'Приветсвие {jumbo} активировано')
            print(jumbo, jumbo.active)
        return redirect(url_for('edit_jumbo'))

    if 'deact' in form:
        for checked_jumbo in checked_jumbos:
            jumbo = session.query(Jumbotron).get(checked_jumbo)
            print(jumbo, jumbo.active)
            jumbo.active = False
            session.commit()
            flash(f'Приветсвие {jumbo} деактивировано')
            print(jumbo, jumbo.active)
        return redirect(url_for('edit_jumbo'))

    if 'copy' in form and len(checked_jumbos) == 1:
        id = checked_jumbos
        jumbo = session.query(Jumbotron).get(id)
        jumbo_title = jumbo.title
        emphasis = jumbo.emphasis
        text = jumbo.text
        img_link = jumbo.img_link

        return render_template('admin/jumbo.html', page_title=page_title, jumbos=jumbos, jumbo_title=jumbo_title,
                               emphasis=emphasis, text=text, img_link=img_link, id=id)

    return render_template('admin/jumbo.html', page_title=page_title, jumbos=jumbos)

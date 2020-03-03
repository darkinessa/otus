from flask import request, render_template, flash
from flask_login import current_user

from app import app
from app.database import Session
from app.decorators import admin_required
from app.models import User, Rubric, Tag, Post
from app.validators import is_empty, check_img, validate_form


@app.route('/add_post', methods=['GET', 'POST'])
@admin_required
def add_post():
    session = Session()
    user = session.query(User).filter_by(username=current_user.username).first()
    rubrics = session.query(Rubric).all()
    page_title = 'Создание нового поста'
    form = request.form
    rubric_id = form.get('selected_rubric')
    title = form.get('post_title')
    meta_description = form.get('meta_description')
    meta_keywords = form.get('meta_keywords')
    description = form.get('post_description')
    body = form.get('post_body')
    img_link = form.get('prew_img_link')
    url_path = form.get('post_slug')
    post_tags = form.get('tags')
    tags = []
    if post_tags:
        tags = post_tags.split(',')

    error = None

    fields = [
        (is_empty, title, 'Заполните поле: Заголовок'),
        (is_empty, description, 'Заполните поле: Краткое описание'),
        (is_empty, body, 'Заполните поле:  Текст'),
        (is_empty, rubric_id, 'Заполните поле:  Рубрика'),
        (is_empty, img_link, 'Заполните поле:  Ссылка на картинку'),
        (check_img, img_link, 'Неверная ссылка, такого файла не существует')
    ]

    def check_form_error(check_function, field_name, error_text):
        if check_function(field_name):
            return render_template('admin/manage_post.html', field_with_error=field_name, error=error_text,
                                   post_title=title, post_body=body, rubrics=rubrics, tags=tags,
                                   prew_img_link=img_link, meta_description=meta_description,
                                   meta_keywords=meta_keywords, post_description=description,
                                   page_title=page_title, post_slug=url_path)

    def add_tag(tags_list):
        tags_post = []
        for tag in tags_list:
            ex_tag = session.query(Tag).filter_by(name=tag).one_or_none()
            if not ex_tag:
                tag = Tag(name=tag)
                session.add(tag)
                session.flush()
                tags_post.append(tag)
            else:
                tags_post.append(ex_tag)
        return tags_post

    if request.method == "POST":
        post_rubric = session.query(Rubric).get(rubric_id)
        if 'preview' in form:
            return render_template('public/post.html', post_title=title, post_body=body,
                                   post_rubric=post_rubric, tags=tags)

        elif 'save' in form and (validate_form(check_form_error, fields) is None):
            tgs = add_tag(tags)
            post = Post(user_id=user.id, rubric_id=rubric_id, title=title, meta_description=meta_description,
                        meta_keywords=meta_keywords, description=description, body=body, img_link=img_link,
                        url_path=url_path, tags=tgs)
            session.add(post)
            flash('Черновик сохранен')

        elif 'pub' in form and (validate_form(check_form_error, fields) is None):
            tgs = add_tag(tags)
            post = Post(user_id=user.id, rubric_id=rubric_id, title=title, meta_description=meta_description,
                        meta_keywords=meta_keywords, description=description, body=body, img_link=img_link,
                        url_path=url_path, tags=tgs, is_published=True)
            session.add(post)
            flash('Пост опубликован')

        elif validate_form(check_form_error, fields):
            return validate_form(check_form_error, fields)
        session.commit()

    return render_template('admin/manage_post.html', rubrics=rubrics, page_title=page_title)


@app.route('/edit_post', methods=['GET', 'POST'])
@admin_required
def edit_post(id):
    '''здесь будет функционал'''
    session = Session()
    post = session.query(Post).get(id)
    return render_template('manage_post', post=post)

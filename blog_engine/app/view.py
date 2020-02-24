from flask import render_template, flash, url_for, request
from flask_login import current_user, login_user, logout_user
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash

from app import app
from app.database import Session
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    return render_template('public/index.html')


@app.route('/static-template')
def static_template():
    return render_template('public/static-template.html')


@app.route('/contacts')
def contacts():
    return render_template('public/contacts.html')


@app.route('/post')
def post():
    return render_template('public/post.html')


@app.route('/blog')
def blog():
    print(current_user)
    return render_template('public/blog.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    session = Session()
    form = request.form
    if request.method == 'POST':
        username = form.get('username')
        name = form.get('name')
        email = form.get('email')
        password = form.get('password')
        error = None

        def check_empty_error(check_function, field_name, error_text):
            if check_function(field_name):
                return render_template('admin/reg.html', field_with_error=field_name, error=error_text,
                                       username=username, name=name, email=email, password=password)

        def is_empty(field):
            return form.get(field).strip() == ''

        def is_exist(field):
            current_username = form.get(field)
            return session.query(User).filter_by(username=current_username).one_or_none() is not None

        fields = [
            (is_empty, 'username', 'Заполните поле: username'),
            (is_exist, 'username', 'Данное имя занято, выберите другоое'),
            (is_empty, 'email', 'Заполните поле: email'),
            (is_empty, 'password', 'Заполните поле:  password'),
        ]

        for field in fields:

            check_f, field_name, error_text = field
            error = check_empty_error(check_f, field_name, error_text)
            if error:
                return error

        user = User(username=username, name=name, email=email)
        user.set_password(password)
        session.add(user)
        session.commit()
        flash('Вы успешно зарегистрировались!')

        return redirect(url_for('registration'))

    return render_template('admin/reg.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    session = Session()
    form = request.form

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        current_username = form.get('username')
        password = form.get('password')
        user = session.query(User).filter_by(username=current_username).one_or_none()

        def validate_form(field_username, field_password):
            flash_text = None

            if not field_username:
                flash_text = 'Поле логин не заполнено'

            elif user is None:
                flash_text = 'Неверный логин'

            elif not field_password:
                flash_text = 'Поле пароль не заполнено'

            elif not user.check_password(field_password):
                flash_text = 'Неверный пароль'

            return flash_text

        if validate_form(current_username, password):
            flash(validate_form(current_username, password))
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('post'))

    return render_template('admin/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

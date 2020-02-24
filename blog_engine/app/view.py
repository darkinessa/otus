from flask import render_template, flash, url_for, request
from werkzeug.utils import redirect

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

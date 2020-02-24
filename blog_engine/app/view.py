from flask import render_template
from app import app


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
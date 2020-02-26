from flask import Flask
from flask_login import LoginManager

from config import Config

app = Flask(__name__)

app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'


from app import view

from app.admin import blueprint as admin_blueprint

app.register_blueprint(admin_blueprint, url_prefix='/admin')

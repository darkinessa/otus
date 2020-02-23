from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    TESTING = getenv('TESTING')
    DEBUG = getenv('DEBUG')
    SECRET_KEY = getenv('SECRET_KEY')
    SESSION_COOKIE_NAME = getenv('SESSION_COOKIE_NAME')

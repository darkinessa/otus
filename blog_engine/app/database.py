from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app import app

engine = create_engine('sqlite:///blog.db', convert_unicode=True)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
Base = declarative_base()


@app.teardown_request
def remove_session(ex=None):
    Session.remove()

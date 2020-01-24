from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///my_blog.db')

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

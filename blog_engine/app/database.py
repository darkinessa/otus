from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite://blog.db', convert_unicode=True)

session_factory = sessionmaker(bing=engine)
Session = scoped_session(session_factory)
Base = declarative_base()

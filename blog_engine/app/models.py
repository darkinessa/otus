from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship

from werkzeug.security import generate_password_hash, check_password_hash

from app import login
from app.database import Base, engine, Session

bind_posts_tags = Table('bind_posts_tags', Base.metadata,
                        Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True),
                        Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
                        )


class User(UserMixin, Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(24), unique=True, nullable=False)
    name = Column(String(48))
    email = Column(String(48), nullable=False)
    password = Column(String(128), nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    posts = relationship('Post', back_populates='author')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_admin(self):
        return self.is_admin

    def __repr__(self):
        return f'<User {self.username}>'


@login.user_loader
def load_user(id):
    session = Session()
    return session.query(User).get(id)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    rubric_id = Column(Integer, ForeignKey('rubrics.id'), nullable=False)
    title = Column(String(128), nullable=False)
    meta_description = Column(String(160))
    meta_keywords = Column(String(160))
    description = Column(String(320), nullable=False)
    body = Column(Text, nullable=False)
    img_link = Column(String(128))
    date = Column(DateTime, nullable=False, default=datetime.utcnow)
    url_path = Column(String(64))
    is_published = Column(Boolean, nullable=False, default=False)
    author = relationship('User', back_populates='posts', lazy='joined')
    rubric = relationship('Rubric', back_populates='posts', lazy='joined')
    tags = relationship('Tag', secondary=bind_posts_tags, back_populates='posts')

    def __repr__(self):
        return f'Post №{self.id}. {self.title}'


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, unique=True, index=True)
    posts = relationship('Post', secondary=bind_posts_tags, back_populates='tags')

    def __repr__(self):
        return f'{self.name}'


class Rubric(Base):
    __tablename__ = 'rubrics'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, unique=True, index=True)
    posts = relationship('Post', back_populates='rubric')
    is_active = Column(Boolean, nullable=False, default=True)


class Jumbotron(Base):
    __tablename__ = 'jumbotron'

    id = Column(Integer, primary_key=True)
    emphasis = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    img_link = Column(String(128), nullable=False)


class Static(Base):
    __tablename__ = 'static'

    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    meta_description = Column(String(160))
    meta_keywords = Column(String(160))
    page = Column(Text)
    is_active = Column(Boolean, nullable=False, default=False)

# Base.metadata.create_all(bind=engine)

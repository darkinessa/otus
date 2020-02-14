from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, String, Text, Boolean, DateTime, Table
from sqlalchemy.orm import relationship

from Models.settings import Base

bind_posts_tags = Table('bind_posts_tags', Base.metadata,
                        Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True),
                        Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
                        )


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(24), unique=True, index=True, nullable=False)
    posts = relationship('Post', back_populates='author')

    def __repr__(self):
        return f'<User {self.username}>'


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(128), nullable=False)
    description = Column(String(320), nullable=False)
    body = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.utcnow)
    is_published = Column(Boolean, nullable=False, default=False)
    author = relationship('User', back_populates='posts', lazy='joined')
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

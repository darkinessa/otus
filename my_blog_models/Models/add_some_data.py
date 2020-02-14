from Models.settings import Session
from Models.sql_alchemy_models import User, Tag, Post


def add_user(text):
    session = Session()
    if session.query(User).filter_by(username=text).one_or_none():
        massage = f'user: {text} already exists in db'
        return massage
    else:
        user = User(username=text)
        session.add(user)
        session.commit()
        massage = f'User: {text} was successfully added'
        return massage


def add_post(post):
    session = Session()
    if post and len(post) == 6:

        try:
            user_id = session.query(User.id).filter(User.username == post['User']).scalar()

            if not user_id:
                massage = f"User {post['User']} not found"
                return massage
            for key, value in post.items():
                if key == 'tags':
                    continue
                elif not value:
                    massage = f'Expected date for {key}'
                    return massage

            post_tags = []
            for tag in post['tags']:
                ex_tag = session.query(Tag).filter_by(name=tag).one_or_none()
                if not ex_tag:
                    tag = Tag(name=tag)
                    session.add(tag)
                    session.flush()
                    post_tags.append(tag)
                else:
                    post_tags.append(ex_tag)
            post = Post(user_id=user_id, title=post['Title'], description=post['Description'],
                        body=post['Body'], is_published=post['is_published'], tags=post_tags)

            session.add(post)
            session.commit()
            return 'Post was successfully added'

        except Exception as e:
            massage = f'Occur {e}'
            return massage

    else:
        massage = 'Received data not match expected '
        return massage


def multiple_add(func, data):
    [func(something) for something in data]
    return

from Models.settings import Session
from Models.sql_alchemy_models import User, Tag, Post


def add_user(text):
    session = Session()
    if session.query(User).filter_by(username=text).one_or_none():
        message = f'user: {text} already exists in db'

    else:
        user = User(username=text)
        session.add(user)
        session.commit()
        message = f'User: {text} was successfully added'

    return message


def add_post(post):
    session = Session()
    if post and len(post) == 6:

        try:
            user_id = session.query(User.id).filter(User.username == post['User']).scalar()

            if not user_id:
                message = f"User {post['User']} not found"
                return message
            for key, value in post.items():
                if key == 'tags':
                    continue
                elif not value:
                    message = f'Expected date for {key}'
                    return message

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
            message = f'Occur {e}'
            return message

    else:
        message = 'Received data not match expected '
        return message


def multiple_add(func, data):
    [func(something) for something in data]
    return

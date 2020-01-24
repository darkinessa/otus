from settings import Session
from sqlalchemy import func
from sql_alchemy_models import User, Tag, Post, bind_posts_tags


def choose_posts_by_user(user_id):
    print('Найти все посты пользователя')
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    posts = session.query(Post).join(User).filter(User.id == user_id).all()
    print(f'{user}, found: {len(posts)}')
    for post in posts:
        print(post)

    return 'done'


def choose_posts_by_tag(tag):
    print('Найти все посты по заданному тегу')
    session = Session()
    tag_id = session.query(Tag.id).filter(Tag.name == tag).scalar()
    posts = session.query(Post).join(bind_posts_tags).filter(bind_posts_tags.c.tag_id == tag_id).all()

    print(f'{tag}, found: {len(posts)}')
    for post in posts:
        print(post, post.author)
    return 'done'


def choose_posts_by_user_with_tag(user, tag):
    print("Найти по заданному тегу все посты пользователя")

    session = Session()
    t_id = session.query(Tag.id).filter_by(name=tag).scalar()
    posts = session.query(Post).join(User).join(bind_posts_tags).filter(User.username == user).filter(
        bind_posts_tags.c.tag_id == t_id).all()

    print(f'{user}, tag: {tag}, found: {len(posts)}')
    [print(post) for post in posts]
    return 'done'


def choose_posts_by_user_with_tags(user, tags):
    print("Найти все посты пользователя c заданными тегами")

    session = Session()

    tgs = session.query(Tag).filter(Tag.name.in_(tags)).all()

    request = session.query(Post).join(User).filter_by(username=user).join(bind_posts_tags).filter(
        bind_posts_tags.c.tag_id == tgs[0].id and bind_posts_tags.c.tag_id == tgs[1].id).all()

    posts = []

    for p in request:
        have_tags = True
        for t in tgs:
            if t not in p.tags:
                have_tags = False
        if have_tags:
            posts.append(p)
    [print(r, r.tags, r.author) for r in posts]

    return 'done'


def choose_posts_by_user_with_two_random_tags(user):
    print(" все посты конкретного пользователя с 2-мя любыми тегами")
    session = Session()
    posts = session.query(Post).join(bind_posts_tags).join(User).filter_by(
        username=user).group_by(Post.id) \
        .having(func.count(Post.id) == 2).all()
    [print(r, r.tags, r.author) for r in posts]
    return 'done'


# print(choose_posts_by_user('1'))
# print(choose_posts_by_tag('questions'))
#
# print(choose_posts_by_user_with_tag('morpheus', 'matrix'))
# print(choose_posts_by_user_with_tags('Trinity', ['matrix', 'rabbit']))
# print(choose_posts_by_user_with_two_random_tags('Neo'))

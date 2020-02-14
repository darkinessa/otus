from Models.add_some_data import add_user, add_post, multiple_add
from Models.example_data import users, posts
from Models.get_some_data import choose_posts_by_user_with_two_random_tags, print_posts
from Models.settings import engine, Base


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    multiple_add(add_user, users)
    multiple_add(add_post, posts)
    print_posts(choose_posts_by_user_with_two_random_tags('Neo'))

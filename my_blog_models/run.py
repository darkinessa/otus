from add_some_date import add_some_data
from get_some_date import choose_posts_by_user_with_two_random_tags
from settings import engine, Base


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    add_some_data()
    choose_posts_by_user_with_two_random_tags('Neo')



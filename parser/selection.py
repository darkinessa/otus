from text import *


def user_input(text):
    user_input = input(text)
    return user_input


def selection_options():
    print(text_1)

    select_engines = user_input(text_choose_engine).lower()
    print(select_engines)

    while select_engines not in dict.values(search_engines_dict):
        select_engines = user_input(text_choose_engine).lower()

    print(text_2)

    select_quantity_links = int(user_input(text_quantity_links))

    while select_quantity_links not in [i for i in range(1, 51)]:
        select_quantity_links = int(user_input(text_quantity_links))

    print(text_3)
    select_double_links = user_input(text_double_links).lower()
    while select_double_links.capitalize() not in ['Y', 'N']:
        select_double_links = user_input(text_double_links)

    return select_engines, select_quantity_links, select_double_links

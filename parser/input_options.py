from text import *


def user_input(text):
    user_input = input(text)
    return user_input


def input_options():
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
    select_search_query = user_input(text_search_query).lower()
    if len(select_search_query) > 48:
        select_search_query = user_input(text_search_query)

    return select_engines, select_quantity_links, select_search_query


def prepare_query_text(query_text):
    if len(query_text.split()) > 1:
            text = '+'.join(query_text.split())
    else:
        text = query_text

    return text


def search_depth(quantity_links):
    if quantity_links >= 6:
        quantity_links = quantity_links + 10
    search_depth_list = [i for i in range((quantity_links // 10) + 1)]
    return search_depth_list

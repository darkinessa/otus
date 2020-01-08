from text import *


def user_input(text):
    user_input = input(text)
    return user_input


def select_engines():
    print(text_1)  # выбор поисковика

    select_engines = user_input(text_choose_engine).lower()

    while select_engines not in dict.keys(search_engines_dict):
        select_engines = user_input(text_choose_engine).lower()

    return search_engines_dict[select_engines]


def select_quantity_links():
    print(text_2)  # количество поисковой выдачи
    (select_quantity_links, is_int) = validate_user_input_int(text_quantity_links)

    while not is_int:
        (select_quantity_links, is_int) = validate_user_input_int(text_quantity_links)

    while select_quantity_links not in [i for i in range(1, 51)]:
        (select_quantity_links, is_int) = validate_user_input_int(text_quantity_links)

    return select_quantity_links


def validate_user_input_int(value):
    val = user_input(value)
    try:
        return int(val), True
    except ValueError:
        return val, False


def select_search_depth():
    print(text_3)
    (select_search_depth, is_int) = validate_user_input_int(text_search_depth)

    while not is_int:
        (select_search_depth, is_int) = validate_user_input_int(text_search_depth)

    while select_search_depth not in [True, False]:
        (select_search_depth, is_int) = validate_user_input_int(text_search_depth)

    return select_search_depth


def select_search_query():
    print(text_4)  # текст поискового запроса
    select_search_query = user_input(text_search_query).lower()

    while len(select_search_query) not in [i for i in range(3, 49)]:
        select_search_query = user_input(text_search_query).lower()
        print(f'Количество символов вашего запроса {len(select_search_query)}')

    return select_search_query


def input_options():
    # 1. получаем результат выбоора поисковика
    search_engine = select_engines()
    print(search_engine)

    # 2. получаем количество нужных ссылок
    quantity_links = select_quantity_links()
    print(quantity_links)

    # 3. рекурсивный поиск
    search_depth = select_search_depth()
    print(search_depth)

    # 4. получаем текст поискового запроса
    query_text = select_search_query()
    print(query_text)

    return search_engine, quantity_links, search_depth, query_text


def prepare_query_text(query_text):
    if len(query_text.split()) > 1:
        text = '+'.join(query_text.split())
    else:
        text = query_text

    return text

print(prepare_query_text(1))

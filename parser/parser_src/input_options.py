from parser_src.text import *


def select_engines():
    print(text_1)  # выбор поисковика

    try:
        selected_engine_key = key_from_user_input()

        while selected_engine_key not in dict.keys(search_engines_dict):
            selected_engine_key = key_from_user_input()
    except EOFError as err:
        print(f'{err} error occurred')
        return
    return search_engines_dict[selected_engine_key]


def key_from_user_input():
    return input(text_choose_engine).lower()


def select_quantity_links():
    print(text_2)  # количество поисковой выдачи
    try:
        (selected_quantity_links, is_int) = validate_user_input_int(text_quantity_links)

        while not is_int:
            (selected_quantity_links, is_int) = validate_user_input_int(text_quantity_links)

        while selected_quantity_links not in [i for i in range(1, 51)]:
            (selected_quantity_links, is_int) = validate_user_input_int(text_quantity_links)
    except EOFError as err:
        print(f'{err} error occurred')
        return

    return selected_quantity_links


def validate_user_input_int(value):
    val = input(value)
    try:
        return int(val), True
    except ValueError:
        return val, False


def select_search_depth():
    print(text_3)
    try:
        (select_search_depth, is_int) = validate_user_input_int(text_search_depth)

        while not is_int:
            (select_search_depth, is_int) = validate_user_input_int(text_search_depth)

        while select_search_depth not in [0, 1]:
            (select_search_depth, is_int) = validate_user_input_int(text_search_depth)
    except EOFError as err:
        print(f'{err} error occurred')
        return

    return select_search_depth


def select_search_query():
    print(text_4)  # текст поискового запроса
    try:
        select_search_query = input(text_search_query).lower()

        while len(select_search_query) not in [i for i in range(3, 49)]:
            select_search_query = input(text_search_query).lower()
            print(f'Количество символов вашего запроса {len(select_search_query)}')

    except EOFError as err:
        print(f'{err} error occurred')
        return

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

    return search_engine, int(quantity_links), search_depth, query_text


def prepare_query_text(query_text):
    # подготовить текст для создания url
    if len(query_text.split()) > 1:
        text = '+'.join(query_text.split())
    else:
        text = query_text

    return text

from parser_src.google import get_google_results
from parser_src.input_options import input_options
from parser_src.yandex import get_yandex_results

query_text = 'купить куклу'
quantity = '5'
search_engine = 'g'
rec = False


# param = query_text, quantity_links, search_engine, rec

def get_results():
    user_input = input_options()
    print(user_input, user_input['search_engine'], user_input['quantity_links'],user_input['search_depth'], user_input['query_text'])

    results = []
    # google_results = get_google_results(query_text, quantity_links)
    # links = get_yandex_results(query_text, quantity_links)

    if user_input['search_engine']== 'google':
        results.append('google_results')

    if user_input['search_engine'] == 'yandex':
        links = 'get_yandex_results(query_text, quantity_links)'
        results.append(links)

    if search_engine == 'both':
        results = 'google_results' + links

    return results


# print(get_results())

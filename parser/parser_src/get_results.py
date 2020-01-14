from parser_src.extra_links import get_results_with_extra_link
from parser_src.google import get_google_results
from parser_src.input_options import input_options
from parser_src.print_options import print_extra_results, print_results
from parser_src.yandex import get_yandex_results


def get_results():
    user_input = input_options()

    search_engine = user_input['search_engine']
    query_text = user_input['query_text']
    search_depth = int(user_input['search_depth'])
    quantity_links = int(user_input['quantity_links'])

    results = []

    if search_engine == 'google':
        google_results = get_google_results(query_text, quantity_links)
        results = google_results

    if search_engine == 'yandex':
        yandex_results = get_yandex_results(query_text, quantity_links)
        results = yandex_results

    if search_engine == 'both':
        if quantity_links % 2 == 0:
            new_quantity = quantity_links / 2
        if quantity_links % 2 != 0:
            new_quantity = (quantity_links + 1) / 2

        results = get_google_results(query_text, new_quantity) + get_yandex_results(query_text, new_quantity)

    if search_depth == 1:
        new_results = get_results_with_extra_link(results, quantity_links, query_text)
        print(print_extra_results(new_results, quantity_links))

    else:
        print(print_results(results, quantity_links))


if __name__ == '__main__':
    get_results()

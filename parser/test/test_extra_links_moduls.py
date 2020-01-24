from parser_src.extra_links import get_extra_links_soup, get_extra_results, get_pages_extra_results, \
    get_combined_results
from parser_src.print_options import print_extra_results

from test.mock.mock_html_pages import html_mock
from test.mock.mock_variable_value import expected_yandex_results, \
    mock_expected_extra_links_with_yandex_html, expected_combined_results_with_yandex_results, \
    expected_google_results, expected_extra_results_with_google_results, expected_combined_results_with_google_results


def test_got_extra_links_with_wrong_value():
    try:
        output = get_extra_links_soup('что-то пошло не так c get_html, код ошибки 502', ['1', 2])
    except TypeError:
        assert False, 'Got wrong parameter'

    assert output == [], 'Should be emty list'


def test_got_extra_links():
    results = html_mock
    text_query = 'python'
    expected = expected_extra_results_with_google_results


    output = get_extra_results(results, text_query)
    print(output)
    assert output == expected, 'Should be list with results'


def test_got_combined_results():
    results_1 = expected_yandex_results
    extra_results_1 = mock_expected_extra_links_with_yandex_html
    expected_1 = expected_combined_results_with_yandex_results

    results_2 = expected_google_results
    extra_results_2 = expected_extra_results_with_google_results
    expected_2 = expected_combined_results_with_yandex_results

    try:
        output_1 = get_combined_results(results_1, extra_results_1)
        output_2 = get_combined_results(results_2, extra_results_2)
        print(print_extra_results(output_2, 8))
        print(print_extra_results(output_1, 10))
    except ValueError:
        assert False, 'Got wrong parameters'


# def test_got_pages_extra_results():
# # лезет парсить результаты по живому
#     results = expected_yandex_results
#     # text = 'ирисы'
#     quantity = 7
#     output = get_pages_extra_results(results, quantity)
#     print(output)
#     assert output != [], 'Should be list with results'
#     assert len(output) == quantity



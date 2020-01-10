from parser_src.extra_links import get_extra_links_soup, get_extra_results, get_pages_extra_results, \
    get_combined_results
from test.mock.mock_html_pages import html_mock
from test.mock.mock_variable_value import  expected_yandex_results, \
    mock_expected_extra_links_with_yandex_html, expected_combined_results_with_yandex_results, expected_extra_link_with_google_results


def test_got_extra_links_with_wrong_value():
    try:
        output = get_extra_links_soup('', ['1', 2])
    except TypeError:
        assert False, 'Got wrong parameter'

    assert output == [], 'Should be None'


def test_got_extra_links():
    results = html_mock
    text_query = 'python'
    expected = expected_extra_link_with_google_results
    output = get_extra_results(results, text_query)
    print(output)
    assert output == expected, 'Should be list with results'


def test_got_combined_results():
    results = expected_yandex_results
    extra_results = mock_expected_extra_links_with_yandex_html
    expected = expected_combined_results_with_yandex_results
    try:
        output = get_combined_results(results, extra_results)
    except ValueError:
        assert False, 'Got wrong parameters'

    assert output == expected

# def test_got_pages_extra_results():
# лезет парсить результаты по живому
#     results = expected_yandex_results
#     # text = 'ирисы'
#     output = get_pages_extra_results(results)
#     assert output != [] 'Should be list with results'

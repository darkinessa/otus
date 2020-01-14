import io

from parser_src.extra_links import get_combined_results
from parser_src.get_results import get_results
from parser_src.input_options import input_options
from parser_src.print_options import print_extra_results
from test.mock.mock_variable_value import expected_google_results, expected_yandex_results, \
    expected_extra_results_with_google_results, mock_expected_extra_links_with_yandex_html, \
    expected_combined_results_with_yandex_results


def test_get_results(monkeypatch):
    assume_stdin(monkeypatch, 'y\n8\n1\nPython')
    user_input = input_options()
    print(user_input)
    results = []
    expexted = expected_combined_results_with_yandex_results

    print(len(expexted))

    if user_input['search_engine'] == 'google':
        g_results = expected_google_results
        results.append(g_results)

    if user_input['search_engine'] == 'yandex':
        links = expected_yandex_results
        results.append(links)

    if user_input['search_engine'] == 'both':
        g = expected_google_results
        y = expected_yandex_results
        results.append(g)
        results.append(y)

    if user_input['search_depth'] == 1:
        extra_results = mock_expected_extra_links_with_yandex_html
        current_results = expected_yandex_results
        results = get_combined_results(current_results, extra_results)
    print(results)

    assert results == expexted


def assume_stdin(monkeypatch, stdin_input):
    monkeypatch.setattr('sys.stdin', io.StringIO(stdin_input))

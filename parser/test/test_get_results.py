import io

from parser_src.get_results import get_results


def test_got_results(monkeypatch):
    assume_stdn(monkeypatch, 'y\n45\n0\nfas')
    expected_user_input = {'search_engine': 'yandex', 'quantity_links': 45, 'search_depth': 0, 'query_text': 'fas'}
    output = get_results()
    assert output == ['get_yandex_results(query_text, quantity_links)']


def assume_stdn(monkeypatch, stdin_input):
    monkeypatch.setattr('sys.stdin', io.StringIO(stdin_input))


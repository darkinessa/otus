import io

from parser_src.input_options import select_search_depth, select_search_query, select_engines, select_quantity_links, \
    input_options, prepare_query_text


def test_chooses_search_engine_based_on_stdin(monkeypatch):
    assume_stdin(monkeypatch, 'G')
    output = select_engines()
    assert output == 'google', 'Should be google'


def test_deals_with_unknown_search_engine_with_error(monkeypatch):
    assume_stdin(monkeypatch, "Я\n")
    output = select_engines()
    assert output is None, 'Should be None'


def test_deals_with_empty_search_engine_with_error(monkeypatch):
    assume_stdin(monkeypatch, "")
    try:
        output = select_engines()
    except KeyError:
        assert False, 'Got key error'

    assert output is None, 'Should be None'


def test_type_output_quantity_links(monkeypatch):
    assume_stdin(monkeypatch, '12')
    output = select_quantity_links()
    assert type(output) is int, "Should be <class 'int'>"


def test_deals_quantity_links(monkeypatch):
    assume_stdin(monkeypatch, '16')
    output = select_quantity_links()
    assert output == 16, 'Should be integer'


def test_deals_quantity_links_with_type_error(monkeypatch):
    assume_stdin(monkeypatch, 'one')
    try:
        output = select_quantity_links()
    except TypeError:
        assert False, 'Got type error'

    assert output is None, 'Should be None'


def test_deals_quantity_links_with_quantity_error(monkeypatch):
    assume_stdin(monkeypatch, '51')
    output = select_quantity_links()
    assert output is None, 'Should be None'


def test_choose_search_depth(monkeypatch):
    assume_stdin(monkeypatch, '1')
    output = select_search_depth()
    assert output == 1, 'Should be 1'


def test_choose_type_search_depth(monkeypatch):
    assume_stdin(monkeypatch, 'False')
    output = select_search_depth()
    assert output is None, 'Should be None'


def test_choose_search_query_with_quantity_symbols_error(monkeypatch):
    assume_stdin(monkeypatch, 'output is None, Should be None output is None, Should be None')
    output = select_search_query()
    assert output is None, 'Should be None'


def test_choose_search_query(monkeypatch):
    query = 'Fashion Royalty Agness'
    assume_stdin(monkeypatch, query)
    output = select_search_query()
    assert output == query.lower(), 'Should be string with query text'


def test_returned_input_options_correct(monkeypatch):
    assume_stdin(monkeypatch, 'y\n12\n1\nFashion Royalty Agness')
    opts = input_options()
    assert ('yandex', 12, 1, 'fashion royalty agness') == opts, "Should be ('yandex', 12, 1, 'fashion royalty agness')"


def test_prepare_query_text():
    output_1 = prepare_query_text('fashion royalty agness')
    output_2 = prepare_query_text('python')
    assert output_1 == 'fashion+royalty+agness'
    assert output_2 == 'python'


def assume_stdin(monkeypatch, stdin_input):
    monkeypatch.setattr('sys.stdin', io.StringIO(stdin_input))

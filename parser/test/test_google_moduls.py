import os
from parser_src.google import create_google_url, get_google_results, get_google_soup_results


def test_return_type_created_google_url():
    output = create_google_url('python unit test', 12)
    assert type(output) is list, 'Should be list'


def test_return_quantity_created_google_url():
    output_1 = create_google_url('python unit test', 22)
    output_2 = create_google_url('python', 1)

    assert len(output_1) == 3, 'Should be 3'
    assert len(output_2) == 1, 'Should be 1'


def test_created_google_url_with_wrong_value():
    try:
        output = create_google_url('python unit test', '12.1')
    except ValueError:
        assert False, 'Got wrong parameters'

    assert output is None, 'Should be None'


def test_got_google_links_with_wrong_value():
    try:
        output = get_google_soup_results(' jj')
    except TypeError:
        assert False, 'Got wrong parameter'

    assert output is None


def test_got_google_results_with_wrong_value():
    # Осторожно лезет в сеть (сетевые штуки в другом модуле тестируются)
    # и можно бан получить, если часто с правильными резульатами гонять.
    try:
        output = get_google_results('', '')
    except TypeError:
        assert False, 'Got wrong parameters'

    assert output is None


def test_got_google_soup_results():
    mock_path = 'test/mock/goodle_mock.html'
    link = get_test_page(mock_path)
    output = get_google_soup_results(link)
    print(output)
    expected = [('Введение в PyTest - Alexander Demura - Medium',
                 'https://medium.com/@dmrlx/%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-pytest-cc6175c7d0dc'),
                ('PyTest / Хабр - Habr', 'https://habr.com/ru/post/269759/'),
                ('Погружаемся в основы и нюансы тестирования Python-кода', 'https://proglib.io/p/python-testing/'),
                ('PyTest - Python Дайджест', 'https://pythondigest.ru/view/7436/'), (
                'Все точки над И - разбираем фикстуры pytest - python ...',
                'https://automated-testing.info/t/vse-tochki-nad-i-razbiraem-fikstury-pytest/8051'),
                ("Блог gigimon'а ← Немного про py.test", 'https://it4it.ru/2016/02/11/pytest-1/'), (
                'Тестирование в Python [unittest]. Часть 1. Введение',
                'https://devpractice.ru/unit-testing-in-python-part-1/'),
                ('Нескучное тестирование с pytest - SlideShare', 'https://www.slideshare.net/imankulov/pytest-testing'),
                ('Test-Driven Development в Python для начинающих, часть ...',
                 'https://shepetko.com/ru/blog/beginning-test-driven-development-in-python-2')]
    assert output == expected, 'Should be list with expected results'


def get_test_page(my_path):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    link = os.path.join(BASE_DIR, my_path)
    with open(link, "r", encoding='utf-8') as f:
        return f.read()



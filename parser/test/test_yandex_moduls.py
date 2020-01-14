from parser_src.yandex import create_yandex_url, get_yandex_results, get_yandex_soup_results
from test.test_google_moduls import get_test_page


def test_return_type_created_yandex_url():
    output = create_yandex_url('python unit test', 1)
    print(output)
    assert type(output) is list, 'Should be list'


def test_return_quantity_created_yandex_url():
    output_1 = create_yandex_url('python unit test', 12)
    print(output_1)
    output_2 = create_yandex_url('python', 5)  # TypeError
    # output_3 = create_google_url(['python unit test', 12], 12)  # AttributeError: TypeError
    assert len(output_1) == 2, 'Should be 2'
    assert len(output_2) == 1, 'Should be 1'


def test_created_yandex_url_with_wrong_value():
    try:
        output = create_yandex_url('python unit test', '12.1')
    except ValueError:
        assert False, 'Got wrong parameters'

    assert output is None, 'Should be None'


def test_got_yandex_links_with_wrong_value():
    try:
        output = get_yandex_soup_results('aaa ')
        print(output)
    except TypeError:
        assert False, 'Got wrong parameter'

    assert output == [], 'Should be empty list'


def test_got_yandex_links_with_empty_value():
    try:
        output = get_yandex_soup_results(' ')
    except TypeError:
        assert False, 'Got wrong parameter'

    assert output== [], 'Should be empty list'


def test_got_yandex_soup_results():
    mock_path = 'test/mock/yandex_mock.html'
    link = get_test_page(mock_path)
    output = get_yandex_soup_results(link)
    print(output)
    expected = [('1 000+ Бесплатные Ирисы & Цветок изображения - Pixabay',
                 'https://pixabay.com/ru/images/search/%D0%B8%D1%80%D0%B8%D1%81%D1%8B/'),
                ('«Ирис» — сеть цветочных салонов', 'https://iris-flowers.ru/'),
                ('Ирисы | Natural Museum',
                 'https://natural-museum.ru/flora/%D0%B8%D1%80%D0%B8%D1%81%D1%8B'),
                ('Ирисы: 130 фото цветка и идей по украшению сада...',
                 'http://landshaftadvice.ru/irisy/'),
                ('Карликовые ирисы: сорта, описание, фото, посадка и уход',
                 'https://www.syl.ru/article/333595/karlikovyie-irisyi-sorta-opisanie-foto-posadka-i-uhod'),
                ('Садовая классификация ирисов',
                 'https://www.greeninfo.ru/grassy/iris_hybrida.html/Article/_/aID/4985'),
                ('Цветы бородатые ирисы: лучшие сорта, фото и названия...',
                 'https://kvetok.ru/tsvety-dlya-sada/iris-borodaty-j'),
                ('Ирис - мифы, легенды, история происхождения',
                 'https://mifflow.ru/iris.html'),
                ('Ирис',
                 'http://www.plantopedia.ru/encyclopaedia/garden-plants/details/i/iris/'),
                ('Ирисы - история, значение, советы',
                 'https://cyber-florist.ru/news/irisy-istoriia-znachieniie-soviety/')]

    assert output == expected, 'Should be list with expected results'


def test_got_yandex_results_with_wrong_value():
    # Осторожно лезет в сеть (сетевые штуки в другом модуле тестируются)
    # и можно бан получить, если часто с правильными резульатами гонять.
    try:
        output = get_yandex_results('python unit test', '12.1')
    except TypeError:
        assert False, 'Got wrong parameters'

    assert output is None


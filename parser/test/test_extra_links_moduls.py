from parser_src.extra_links import get_extra_links_soup, get_extra_results, get_pages_extra_results, \
    get_combined_results
from test.mock.html_parse_google_mock import html_mock_gopgle_res
from test.mock.mock_html_pages import html_mock
from test.mock.mock_variable_value import expected_yandex_results, \
    mock_expected_extra_links_with_yandex_html, expected_combined_results_with_yandex_results, \
    expected_extra_link_with_google_results, expected_google_results


def test_got_extra_links_with_wrong_value():
    try:
        output = get_extra_links_soup('', ['1', 2])
    except TypeError:
        assert False, 'Got wrong parameter'

    assert output == [], 'Should be None'


def test_got_extra_links():
    print("asdasdasda " + str(len(html_mock)))
    results = html_mock_gopgle_res
    text_query = 'python'
    expected = expected_extra_link_with_google_results
    output = get_extra_results(results, text_query)
    print(output)
    assert output == expected, 'Should be list with results'


def test_got_combined_results():
    results_1 = expected_yandex_results
    extra_results_1 = mock_expected_extra_links_with_yandex_html
    expected_1 = expected_combined_results_with_yandex_results

    results_2 = expected_google_results
    extra_results_2 = expected_extra_link_with_google_results
    expected_2 = expected_combined_results_with_yandex_results
    print(len(results_2), len(extra_results_2))
    try:
        output_1 = get_combined_results(results_1, extra_results_1)
        output_2 = get_combined_results(results_2, extra_results_2)
        print(output_2)
    except ValueError:
        assert False, 'Got wrong parameters'

    assert output_1 == expected_1
    assert output_2 == False


# def test_got_pages_extra_results():
# лезет парсить результаты по живому
#     results = expected_yandex_results
#     # text = 'ирисы'
#     output = get_pages_extra_results(results)
#     assert output != [] 'Should be list with results'


def test_t():
    l = [[],
         [('Python', 'https://habr.com/ru/hub/python/'),
          ('python', 'https://habr.com/ru/search/?q=%5Bpython%5D&target_type=posts'), (
              '                    Python Testing с pytest. Builtin Fixtures, Глава 4                  ',
              'https://habr.com/ru/post/448792/'), (
              '                    Python Testing с pytest. ГЛАВА 3 pytest Fixtures                  ',
              'https://habr.com/ru/post/448786/'), (
              '                    Python Testing с pytest. Глава 2, Написание тестовых функций                  ',
              'https://habr.com/ru/post/448788/'), (
              '                    Python Testing с pytest. Начало работы с pytest, Глава 1                  ',
              'https://habr.com/ru/post/448782/'), (
              '                    Python Testing with pytest. Просто, Быстро, Эффективно и Масштабируемо. Предисловие и Ведение                  ',
              'https://habr.com/ru/post/426699/'), (
              'Преподаватель PythonМосковская школа программистовМосквадо 100\xa0000',
              'https://career.habr.com/vacancies/1000055443'), (
              'Программист PythonFirstVDSИркутскот 50\xa0000до 90\xa0000',
              'https://career.habr.com/vacancies/1000055649'), (
              'Программист PythonСтроительный ДворМоскваот 150\xa0000до 200\xa0000',
              'https://career.habr.com/vacancies/1000054566'), (
              'Team Lead Python DeveloperYLabТольяттиМожно удаленноот 180\xa0000',
              'https://career.habr.com/vacancies/1000055915'), (
              'Python-разработчикОнлайн-кинотеатр iviМоскваот 140\xa0000до 190\xa0000',
              'https://career.habr.com/vacancies/11035166'),
          ('www.slideshare.net/imankulov/pytest-testing', 'http://www.slideshare.net/imankulov/pytest-testing'),
          ('Новые фичи Python 3.8 и самое время перейти с Python 2', 'https://habr.com/ru/post/483276/')],
         [('книги по Python', 'https://proglib.io/p/python-best-books/'),
          ('Инструменты для анализа кода Python. Часть 1', 'https://proglib.io/p/python-code-analysis/'),
          ('Инструменты для анализа кода Python. Часть 2', 'https://proglib.io/p/python-code-analysis-tools/'),
          ('13 лучших книг по Python для начинающих и продолжающих', 'https://proglib.io/p/python-best-books/'),
          ('ТОП-10 книг по Python: эффективно, емко, доходчиво', 'https://proglib.io/p/python-books/'),
          ('Realpython', 'https://realpython.com/python-testing/')],
         [('ffmpeg-python - FFmpeg binding с поддержкой фильтрации', 'http://github.com/kkroening/ffmpeg-python'),
          ('Функции-таймеры в Python', 'https://realpython.com/python-timer/')],
         [('python', 'https://automated-testing.info/tags/python'),
          ('http://habrahabr.ru/company/yandex/blog/242795/', 'http://habrahabr.ru/company/yandex/blog/242795/'), (
              ' Python',
              'http://lessons2.ru/python-for-testers?utm_source=atinfo&utm_medium=top_menu&utm_term=link&utm_campaign=reference'),
          (' Python',
           'http://lessons2.ru/python-for-testers?utm_source=atinfo&utm_medium=top_menu&utm_term=link&utm_campaign=reference')],
         [],
         [('Книга “Линейная алгебра на Python”', 'https://devpractice.ru/book-linalg-python/'),
          ('Книга “Python. Уроки”', 'https://devpractice.ru/book-python-lessons/'),
          ('Книга “Python. unittest”', 'https://devpractice.ru/book-python-unittest/'),
          ('Python', 'https://devpractice.ru/python/'), ('Python. Уроки', 'https://devpractice.ru/python-lessons/'),
          ('Python [unittest]. Уроки', 'https://devpractice.ru/python-unittest-lessons/'),
          ('Python-разработчику', 'https://devpractice.ru/category/python/py-dev/'),
          ('Python', 'https://devpractice.ru/category/python/'),
          ('Тестирование в Python', 'https://devpractice.ru/category/python/testing-in-python/'),
          ('Python', 'https://devpractice.ru/tag/python/'), ('Тестирование в Python',
                                                             'https://devpractice.ru/tag/%d1%82%d0%b5%d1%81%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5-%d0%b2-python/'),
          ('← Python. Урок 15. Итераторы и генераторы',
           'https://devpractice.ru/python-lesson-15-iterators-and-generators/'), (
              'Тестирование в Python [unittest]. Часть 2. TestCase →',
              'https://devpractice.ru/unit-testing-in-python-part-2/'),
          ('Python', 'https://devpractice.ru/category/python/'),
          ('Python-разработчику', 'https://devpractice.ru/category/python/py-dev/'),
          ('Тестирование в Python', 'https://devpractice.ru/category/python/testing-in-python/'),
          ('Уроки по Python', 'https://devpractice.ru/category/python/python-lessons/'), (
              'Линейная алгебра на Python',
              'https://devpractice.ru/category/machine-learning-and-data-analysis/linalg-on-py/'), (
              'Python. Урок 21. Работа с контекстным менеджером',
              'https://devpractice.ru/python-lesson-21-context-manager/'),
          ('Python', 'https://devpractice.ru/category/python/')],
         [(
             'http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137',
             'http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137'),
             (
                 '#Python', 'https://shepetko.com/ru/tag/python'),
             ('Декораторы в Python, часть 2',
              'https://shepetko.com/ru/blog/python-decorators-2'),
             ('Декораторы в Python, часть 1',
              'https://shepetko.com/ru/blog/python-decorators-1'),
             ('Абстрактные базовые классы в Python',
              'https://shepetko.com/ru/blog/abstraktnye-bazovye-klassy-v-python'),
             (
                 'Асинхронное программирование в Python, часть вторая',
                 'https://shepetko.com/ru/blog/asinkhronnoe-programmirovanie-v-python-2'),
             (
                 'Асинхронное программирование в Python, часть первая',
                 'https://shepetko.com/ru/blog/asinkhronnoe-programmirovanie-v-python-1'),
             ('#Python',
              'https://shepetko.com/ru/tag/python')]
         ]

    print(len(l))

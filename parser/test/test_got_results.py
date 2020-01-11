import io

from parser_src.extra_links import get_combined_results
from parser_src.get_results import get_results
from parser_src.input_options import input_options
from parser_src.print_options import print_extra_results
from test.mock.mock_variable_value import expected_google_results, expected_yandex_results, \
    expected_extra_link_with_google_results


def test_get_results(monkeypatch):
    assume_stdin(monkeypatch, 'g\n9\n1\nPython')
    user_input = input_options()
    print(user_input)
    results = []

    expexted = [([[('Введение в PyTest - Alexander Demura - Medium', 'https://medium.com/@dmrlx/%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-pytest-cc6175c7d0dc'), ('PyTest / Хабр - Habr', 'https://habr.com/ru/post/269759/'), ('Погружаемся в основы и нюансы тестирования Python-кода', 'https://proglib.io/p/python-testing/'), ('PyTest - Python Дайджест', 'https://pythondigest.ru/view/7436/'), ('Все точки над И - разбираем фикстуры pytest - python ...', 'https://automated-testing.info/t/vse-tochki-nad-i-razbiraem-fikstury-pytest/8051'), ("Блог gigimon'а ← Немного про py.test", 'https://it4it.ru/2016/02/11/pytest-1/'), ('Тестирование в Python [unittest]. Часть 1. Введение', 'https://devpractice.ru/unit-testing-in-python-part-1/'), ('Нескучное тестирование с pytest - SlideShare', 'https://www.slideshare.net/imankulov/pytest-testing'), ('Test-Driven Development в Python для начинающих, часть ...', 'https://shepetko.com/ru/blog/beginning-test-driven-development-in-python-2')]], [[], [('Python', 'https://habr.com/ru/hub/python/'), ('python', 'https://habr.com/ru/search/?q=%5Bpython%5D&target_type=posts'), ('                    Python Testing с pytest. Builtin Fixtures, Глава 4                  ', 'https://habr.com/ru/post/448792/'), ('                    Python Testing с pytest. ГЛАВА 3 pytest Fixtures                  ', 'https://habr.com/ru/post/448786/'), ('                    Python Testing с pytest. Глава 2, Написание тестовых функций                  ', 'https://habr.com/ru/post/448788/'), ('                    Python Testing с pytest. Начало работы с pytest, Глава 1                  ', 'https://habr.com/ru/post/448782/'), ('                    Python Testing with pytest. Просто, Быстро, Эффективно и Масштабируемо. Предисловие и Ведение                  ', 'https://habr.com/ru/post/426699/'), ('Преподаватель PythonМосковская школа программистовМосквадо 100\xa0000', 'https://career.habr.com/vacancies/1000055443'), ('Программист PythonFirstVDSИркутскот 50\xa0000до 90\xa0000', 'https://career.habr.com/vacancies/1000055649'), ('Программист PythonСтроительный ДворМоскваот 150\xa0000до 200\xa0000', 'https://career.habr.com/vacancies/1000054566'), ('Team Lead Python DeveloperYLabТольяттиМожно удаленноот 180\xa0000', 'https://career.habr.com/vacancies/1000055915'), ('Python-разработчикОнлайн-кинотеатр iviМоскваот 140\xa0000до 190\xa0000', 'https://career.habr.com/vacancies/11035166'), ('www.slideshare.net/imankulov/pytest-testing', 'http://www.slideshare.net/imankulov/pytest-testing'), ('Новые фичи Python 3.8 и самое время перейти с Python 2', 'https://habr.com/ru/post/483276/')], [('книги по Python', 'https://proglib.io/p/python-best-books/'), ('Инструменты для анализа кода Python. Часть 1', 'https://proglib.io/p/python-code-analysis/'), ('Инструменты для анализа кода Python. Часть 2', 'https://proglib.io/p/python-code-analysis-tools/'), ('13 лучших книг по Python для начинающих и продолжающих', 'https://proglib.io/p/python-best-books/'), ('ТОП-10 книг по Python: эффективно, емко, доходчиво', 'https://proglib.io/p/python-books/'), ('Realpython', 'https://realpython.com/python-testing/')], [('ffmpeg-python - FFmpeg binding с поддержкой фильтрации', 'http://github.com/kkroening/ffmpeg-python'), ('Функции-таймеры в Python', 'https://realpython.com/python-timer/')], [('python', 'https://automated-testing.info/tags/python'), ('http://habrahabr.ru/company/yandex/blog/242795/', 'http://habrahabr.ru/company/yandex/blog/242795/'), (' Python', 'http://lessons2.ru/python-for-testers?utm_source=atinfo&utm_medium=top_menu&utm_term=link&utm_campaign=reference'), (' Python', 'http://lessons2.ru/python-for-testers?utm_source=atinfo&utm_medium=top_menu&utm_term=link&utm_campaign=reference')], [], [('Книга “Линейная алгебра на Python”', 'https://devpractice.ru/book-linalg-python/'), ('Книга “Python. Уроки”', 'https://devpractice.ru/book-python-lessons/'), ('Книга “Python. unittest”', 'https://devpractice.ru/book-python-unittest/'), ('Python', 'https://devpractice.ru/python/'), ('Python. Уроки', 'https://devpractice.ru/python-lessons/'), ('Python [unittest]. Уроки', 'https://devpractice.ru/python-unittest-lessons/'), ('Python-разработчику', 'https://devpractice.ru/category/python/py-dev/'), ('Python', 'https://devpractice.ru/category/python/'), ('Тестирование в Python', 'https://devpractice.ru/category/python/testing-in-python/'), ('Python', 'https://devpractice.ru/tag/python/'), ('Тестирование в Python', 'https://devpractice.ru/tag/%d1%82%d0%b5%d1%81%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5-%d0%b2-python/'), ('← Python. Урок 15. Итераторы и генераторы', 'https://devpractice.ru/python-lesson-15-iterators-and-generators/'), ('Тестирование в Python [unittest]. Часть 2. TestCase →', 'https://devpractice.ru/unit-testing-in-python-part-2/'), ('Python', 'https://devpractice.ru/category/python/'), ('Python-разработчику', 'https://devpractice.ru/category/python/py-dev/'), ('Тестирование в Python', 'https://devpractice.ru/category/python/testing-in-python/'), ('Уроки по Python', 'https://devpractice.ru/category/python/python-lessons/'), ('Линейная алгебра на Python', 'https://devpractice.ru/category/machine-learning-and-data-analysis/linalg-on-py/'), ('Python. Урок 21. Работа с контекстным менеджером', 'https://devpractice.ru/python-lesson-21-context-manager/'), ('Python', 'https://devpractice.ru/category/python/')], [('http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137', 'http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137'), ('#Python', 'https://shepetko.com/ru/tag/python'), ('Декораторы в Python, часть 2', 'https://shepetko.com/ru/blog/python-decorators-2'), ('Декораторы в Python, часть 1', 'https://shepetko.com/ru/blog/python-decorators-1'), ('Абстрактные базовые классы в Python', 'https://shepetko.com/ru/blog/abstraktnye-bazovye-klassy-v-python'), ('Асинхронное программирование в Python, часть вторая', 'https://shepetko.com/ru/blog/asinkhronnoe-programmirovanie-v-python-2'), ('Асинхронное программирование в Python, часть первая', 'https://shepetko.com/ru/blog/asinkhronnoe-programmirovanie-v-python-1'), ('#Python', 'https://shepetko.com/ru/tag/python')]])]
    print(len(expexted))
    # user_input['search_engine'], user_input['quantity_links'], user_input['search_depth'],
    # user_input['query_text'],

    # google_results = get_google_results(query_text, quantity_links)
    # links = get_yandex_results(query_text, quantity_links)

    if user_input['search_engine'] == 'google':
        g_results = [expected_google_results]
        results.append(g_results)

    if user_input['search_engine'] == 'yandex':
        links = expected_yandex_results
        results.append(links)

    if user_input['search_engine'] == 'both':
        results = [expected_google_results + expected_yandex_results]

    if user_input['search_depth'] == 1:
        extra_results = [expected_extra_link_with_google_results]
        current_results = expected_google_results
        results = get_combined_results(expected_google_results, extra_results)

    print(len(expexted), len(results))


    print(print_extra_results(expexted, 8))



    assert results==expexted


def test_got_results(monkeypatch):
    assume_stdin(monkeypatch, 'y\n45\n0\nfas')
    expected_user_input = {'search_engine': 'yandex', 'quantity_links': 45, 'search_depth': 0, 'query_text': 'fas'}
    output = get_results()
    assert output == ['get_yandex_results(query_text, quantity_links)']


def assume_stdin(monkeypatch, stdin_input):
    monkeypatch.setattr('sys.stdin', io.StringIO(stdin_input))

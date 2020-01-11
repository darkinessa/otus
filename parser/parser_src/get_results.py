# -*- coding: utf-8 -*-
import io

from parser_src.extra_links import get_combined_results
from parser_src.google import get_google_results
from parser_src.input_options import input_options
from parser_src.yandex import get_yandex_results

query_text = 'купить куклу'
quantity = '5'
search_engine = 'g'
rec = False
expected_google_results = [('Введение в PyTest - Alexander Demura - Medium',
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
expected_yandex_results = [('1 000+ Бесплатные Ирисы & Цветок изображения - Pixabay',
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

expected_extra_link_with_google_results = [[], [('Python', 'https://habr.com/ru/hub/python/'), ('python', 'https://habr.com/ru/search/?q=%5Bpython%5D&target_type=posts'), ('                    Python Testing с pytest. Builtin Fixtures, Глава 4                  ', 'https://habr.com/ru/post/448792/'), ('                    Python Testing с pytest. ГЛАВА 3 pytest Fixtures                  ', 'https://habr.com/ru/post/448786/'), ('                    Python Testing с pytest. Глава 2, Написание тестовых функций                  ', 'https://habr.com/ru/post/448788/'), ('                    Python Testing с pytest. Начало работы с pytest, Глава 1                  ', 'https://habr.com/ru/post/448782/'), ('                    Python Testing with pytest. Просто, Быстро, Эффективно и Масштабируемо. Предисловие и Ведение                  ', 'https://habr.com/ru/post/426699/'), ('Преподаватель PythonМосковская школа программистовМосквадо 100\xa0000', 'https://career.habr.com/vacancies/1000055443'), ('Программист PythonFirstVDSИркутскот 50\xa0000до 90\xa0000', 'https://career.habr.com/vacancies/1000055649'), ('Программист PythonСтроительный ДворМоскваот 150\xa0000до 200\xa0000', 'https://career.habr.com/vacancies/1000054566'), ('Team Lead Python DeveloperYLabТольяттиМожно удаленноот 180\xa0000', 'https://career.habr.com/vacancies/1000055915'), ('Python-разработчикОнлайн-кинотеатр iviМоскваот 140\xa0000до 190\xa0000', 'https://career.habr.com/vacancies/11035166'), ('www.slideshare.net/imankulov/pytest-testing', 'http://www.slideshare.net/imankulov/pytest-testing'), ('Новые фичи Python 3.8 и самое время перейти с Python 2', 'https://habr.com/ru/post/483276/')], [('книги по Python', 'https://proglib.io/p/python-best-books/'), ('Инструменты для анализа кода Python. Часть 1', 'https://proglib.io/p/python-code-analysis/'), ('Инструменты для анализа кода Python. Часть 2', 'https://proglib.io/p/python-code-analysis-tools/'), ('13 лучших книг по Python для начинающих и продолжающих', 'https://proglib.io/p/python-best-books/'), ('ТОП-10 книг по Python: эффективно, емко, доходчиво', 'https://proglib.io/p/python-books/'), ('Realpython', 'https://realpython.com/python-testing/')], [('ffmpeg-python - FFmpeg binding с поддержкой фильтрации', 'http://github.com/kkroening/ffmpeg-python'), ('Функции-таймеры в Python', 'https://realpython.com/python-timer/')], [('python', 'https://automated-testing.info/tags/python'), ('http://habrahabr.ru/company/yandex/blog/242795/', 'http://habrahabr.ru/company/yandex/blog/242795/'), (' Python', 'http://lessons2.ru/python-for-testers?utm_source=atinfo&utm_medium=top_menu&utm_term=link&utm_campaign=reference'), (' Python', 'http://lessons2.ru/python-for-testers?utm_source=atinfo&utm_medium=top_menu&utm_term=link&utm_campaign=reference')], [], [('Книга “Линейная алгебра на Python”', 'https://devpractice.ru/book-linalg-python/'), ('Книга “Python. Уроки”', 'https://devpractice.ru/book-python-lessons/'), ('Книга “Python. unittest”', 'https://devpractice.ru/book-python-unittest/'), ('Python', 'https://devpractice.ru/python/'), ('Python. Уроки', 'https://devpractice.ru/python-lessons/'), ('Python [unittest]. Уроки', 'https://devpractice.ru/python-unittest-lessons/'), ('Python-разработчику', 'https://devpractice.ru/category/python/py-dev/'), ('Python', 'https://devpractice.ru/category/python/'), ('Тестирование в Python', 'https://devpractice.ru/category/python/testing-in-python/'), ('Python', 'https://devpractice.ru/tag/python/'), ('Тестирование в Python', 'https://devpractice.ru/tag/%d1%82%d0%b5%d1%81%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5-%d0%b2-python/'), ('← Python. Урок 15. Итераторы и генераторы', 'https://devpractice.ru/python-lesson-15-iterators-and-generators/'), ('Тестирование в Python [unittest]. Часть 2. TestCase →', 'https://devpractice.ru/unit-testing-in-python-part-2/'), ('Python', 'https://devpractice.ru/category/python/'), ('Python-разработчику', 'https://devpractice.ru/category/python/py-dev/'), ('Тестирование в Python', 'https://devpractice.ru/category/python/testing-in-python/'), ('Уроки по Python', 'https://devpractice.ru/category/python/python-lessons/'), ('Линейная алгебра на Python', 'https://devpractice.ru/category/machine-learning-and-data-analysis/linalg-on-py/'), ('Python. Урок 21. Работа с контекстным менеджером', 'https://devpractice.ru/python-lesson-21-context-manager/'), ('Python', 'https://devpractice.ru/category/python/')], [('http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137', 'http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137'), ('#Python', 'https://shepetko.com/ru/tag/python'), ('Декораторы в Python, часть 2', 'https://shepetko.com/ru/blog/python-decorators-2'), ('Декораторы в Python, часть 1', 'https://shepetko.com/ru/blog/python-decorators-1'), ('Абстрактные базовые классы в Python', 'https://shepetko.com/ru/blog/abstraktnye-bazovye-klassy-v-python'), ('Асинхронное программирование в Python, часть вторая', 'https://shepetko.com/ru/blog/asinkhronnoe-programmirovanie-v-python-2'), ('Асинхронное программирование в Python, часть первая', 'https://shepetko.com/ru/blog/asinkhronnoe-programmirovanie-v-python-1'), ('#Python', 'https://shepetko.com/ru/tag/python')]]

# param = query_text, quantity_links, search_engine, rec

def get_results():

    user_input = input_options()
    print(user_input, user_input['search_engine'], user_input['quantity_links'], user_input['search_depth'],
          user_input['query_text'])
    results = []

    # google_results = get_google_results(query_text, quantity_links)
    # links = get_yandex_results(query_text, quantity_links)

    if user_input['search_engine'] == 'google':
        g_results = [expected_google_results]
        results.append(g_results)


    if user_input['search_engine'] == 'yandex':
        links = expected_yandex_results
        results.append(links)

    if user_input['search_engine'] == 'both':
        results = google_extra_soup + expected_yandex_results

    if user_input['search_depth'] == 1:
        extra_results = [expected_extra_link_with_google_results]
        current_results = results
        print(current_results)
        print(len(extra_results), len(current_results), len(expected_google_results))

        results = get_combined_results(current_results, extra_results)

    return



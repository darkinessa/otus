from bs4 import BeautifulSoup

from parser_src.network_request import get_pages, get_html
from parser_src.print_options import print_extra_results


def get_extra_links_soup(html, query_text):
    try:
        soup = BeautifulSoup(html, 'lxml')
        links = soup.find_all('a')
        links_list = []
        for line in links:
            text = line.text
            link = line.get('href')
            if type(text) is str:
                new_text = text.lower()
                if link:
                    if set(new_text).issuperset(set(query_text.lower())):
                        if link.startswith('http'):
                            text = text.replace('\n', '')
                            results = text, link
                            links_list.append(results)
        return links_list

    except Exception as e:
        print(f'Something wrong with get_extra_links_soup, occurred {e}')
        return


def get_extra_results(html, query_text):
    new_results = []
    for page in html:
        print(len(html))
        extra_links = get_extra_links_soup(page, query_text)
        new_results.append(extra_links)
        # через append, что бы сохранить пустые результаты и len extra_results и results из поисковика совпадала
    return new_results


# def get_extra_results(html, query_text):
#     try:
#         new_results = []
#         for page in html:
#             print(len(html))
#             print(len(page))
#             extra_links = get_extra_links_soup(page[0], query_text)
#             new_results.append(extra_links)
#             # через append, что бы сохранить пустые результаты и len extra_results и results из поисковика совпадала
#         return new_results
#
#     except Exception as e:
#         print(f'Something wrong with get_extra_results, occurred {e}')
#         return


def get_pages_extra_results(search_results_list):
    try:
        html_list = []
        c = 1
        for line in search_results_list:
            print(line, len(line))
            indx = c
            link = line[
                1]  # почему список? разобраться, без  [] результатах пусто потому что функция get_pages ждет список
            html = get_pages([link])
            print(html)
            html_list += html
            c += 1
        return html_list

    except Exception as e:
        print(f'Something wrong with get_pages_extra_results, occurred {e}')
        return


expected_google_results = [('Введение в PyTest - Alexander Demura - Medium',
                            'https://medium.com/@dmrlx/%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-pytest-cc6175c7d0dc'),
                           ('PyTest / Хабр - Habr', 'https://habr.com/ru/post/269759/'),
                           ('Погружаемся в основы и нюансы тестирования Python-кода',
                            'https://proglib.io/p/python-testing/'),
                           ('PyTest - Python Дайджест', 'https://pythondigest.ru/view/7436/'), (
                               'Все точки над И - разбираем фикстуры pytest - python ...',
                               'https://automated-testing.info/t/vse-tochki-nad-i-razbiraem-fikstury-pytest/8051'),
                           ("Блог gigimon'а ← Немного про py.test", 'https://it4it.ru/2016/02/11/pytest-1/'), (
                               'Тестирование в Python [unittest]. Часть 1. Введение',
                               'https://devpractice.ru/unit-testing-in-python-part-1/'),
                           ('Нескучное тестирование с pytest - SlideShare',
                            'https://www.slideshare.net/imankulov/pytest-testing'),
                           ('Test-Driven Development в Python для начинающих, часть ...',
                            'https://shepetko.com/ru/blog/beginning-test-driven-development-in-python-2')]

html = get_pages_extra_results(expected_google_results)

extra_results = get_extra_results(html, 'python')
print(extra_results, len(extra_results))


def get_combined_results(search_results_list, extra_results):
    try:
        if len(search_results_list) == len(extra_results):
            new_results = []
            for i, j in zip(search_results_list, extra_results):
                results = i, j
                new_results.append(results)
            return new_results
        else:
            raise ValueError

    except Exception as e:
        print(f'Something wrong with get_combined_results , occurred {e}')
        return


res = get_combined_results(expected_google_results, extra_results)

print(print_extra_results(res, 9))

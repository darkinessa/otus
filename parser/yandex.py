import quopri

import requests
import re
from bs4 import BeautifulSoup

from input_options import search_depth, prepare_query_text
from tmp_test import get_test_page

# y_local_link = ''
# y_lll = []
# y_page = get_test_page(y_local_link)


text_new = 'pyhton metod сеть магазинов цветов split'


def get_utf_string(query_text):
    russian_letter = re.compile("[а-яА-Я]+")
    query_words_list = query_text.split()
    new_query_text = []

    for word in query_words_list:
        russian = [symbol for symbol in filter(russian_letter.match, word)]
        if russian:
            encode_symbols = []
            for symbol in russian:
                encode_symbol = quopri.encodestring(bytes(symbol, 'UTF-8')).decode('UTF-8')
                encode_symbol = str(encode_symbol).replace("=", "%")
                encode_symbols.append(encode_symbol)

            new_query_text.append(''.join(encode_symbols))

        else:
            new_query_text.append(word)
    return ' '.join(new_query_text)

print(prepare_query_text(get_utf_string(text_new)))

def create_yandex_url(query_text, quantity_links):

    urls = []
    text = prepare_query_text(get_utf_string(query_text))
    base_url = 'https://yandex.ru/search/?text='

    if quantity_links >= 8:
        quantity_links = quantity_links + 10

    for start in [i for i in range((quantity_links // 10) + 1)]:
        if start == 0:
            url = str(base_url + text + '&win=310&lr=213')
        else:
            text_new = text.replace('+', '%20')
            url = str(base_url + text_new +'&win=310&lr=213'+ '&p=' + str(start))

        urls.append(url)
    return urls

quant = 12
print(create_yandex_url(text_new,quant))

def print_results(result, quantity):
    с = 1
    for i in result[0:quantity]:
        print(с, i[0])
        print(i[1])
        с += 1
        print()


def get_yandex_links(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('a')
    new_links = []
    results = []

    for line in range(len(links)):
        if links[line].find('div', class_='organic__url-text') is not None:
            new_links.append(links[line])

    for line in new_links:
        link = line.get('href')
        if re.findall(r'yabs', link):
            # remove ads
            continue
        else:
            text = line.text.strip()
            rs = text, link
            results.append(rs)

    return results


def get_yandex_results(links_list):
    results = []
    for line in links_list:
        page = get_test_page(line)
        results_y = get_yandex_links(page)
        results += results_y
    return results

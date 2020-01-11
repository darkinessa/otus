import re
import quopri

from bs4 import BeautifulSoup

from parser_src.input_options import prepare_query_text
from parser_src.network_request import get_pages


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


def create_yandex_url(query_text, quantity_links):
    try:
        quantity_links = int(quantity_links)
    except Exception as err:
        print(f'Something wrong, occurred {err}')
        return

    urls = []
    text = prepare_query_text(get_utf_string(query_text))
    base_url = 'https://yandex.ru/search/?text='

    if int(quantity_links) >= 8:
        quantity_links = int(quantity_links) + 10

        for start in [i for i in range(quantity_links // 10)]:
            if start == 0:
                url = str(base_url + text + '&win=310&lr=213')
            else:
                text_new = text.replace('+', '%20')
                url = str(base_url + text_new + '&win=310&lr=213' + '&p=' + str(start))

            urls.append(url)
    else:
        url = str(base_url + text + '&win=310&lr=213')
        urls.append(url)

    return urls


def get_yandex_soup_results(html):
    try:
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
            if link.startswith('http'):
                text = line.text.strip()
                result = text, link
                results.append(result)

        return results

    except Exception as e:
        print(f'Something wrong, occurred {e}')
        return


def get_yandex_results(query_text, quantity_links):
    try:
        results = []
        urls = create_yandex_url(query_text, int(quantity_links))

        pages = get_pages(urls)

        for page in pages:
            results_yandex = get_yandex_soup_results(page)
            results += results_yandex

        return results
    except Exception as e:
        print(f'Something wrong, occurred {e}')

#done
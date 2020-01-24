import re

from bs4 import BeautifulSoup

from parser_src.network_request import get_pages
from parser_src.urls_settings import create_yandex_url, validate_url_address


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

            text = line.text.strip()
            result = text, validate_url_address(link)
            results.append(result)

        return results

    except Exception as e:
        print(f'Something wrong with get_yandex_soup_results, occurred {e}')
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
        print(f'Something wrong with get_yandex_results, occurred {e}')
        return

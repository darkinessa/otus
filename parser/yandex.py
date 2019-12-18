import requests
from bs4 import BeautifulSoup
from tmp_test import get_test_page

y_local_link = ''
y_page = get_test_page(y_local_link)


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
        text = line.text.strip()
        rs = text, link
        results.append(rs)

    return results

# https://yandex.ru/search/?text=%D0%92%D1%8B%D0%B1%D0%B8%D1%80%D0%B8%D1%82%D0%B5%20%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%BE%D0%B2%D1%83%D1%8E%20%D0%BC%D0%B0%D1%88%D0%B8%D0%BD%D1%83&clid=2227211&win=310&lr=213

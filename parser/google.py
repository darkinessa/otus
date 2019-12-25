import requests as r
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

from input_options import search_depth, prepare_query_text
from tmp_test import get_test_page



# headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
headers = {'accept': '*/*',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
           'content-length': '0',
           'content-type': 'text/plain;charset=UTF-8',
           "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

query_text_1 = 'python first love'
quantity = 13


def create_google_url(query_text, quantity_links):
    base_url = 'https://www.google.com/search?q='
    urls = []
    text = prepare_query_text(query_text)

    if quantity_links >= 6:
        quantity_links = quantity_links + 10

    for start in [i * 10 for i in range((quantity_links // 10) + 1)]:
        if start == 0:
            url = str(base_url + text + '&newwindow=1' + '&sourceid=chrome&ie=UTF-8')
        else:
            url = str(base_url + text + '&newwindow=1' + '&start=' + str(start) + '&biw=1680&bih=819')
        urls.append(url)
    return urls


print(create_google_url(query_text_1, quantity))

# session = r.session()
# request = session.get(base_url, headers=headers)

url1 = "https://www.google.com/search?newwindow=1&biw=1680&bih=821&q=user+agent+parser+python"

def get_google_links(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find('div', id="search").find_all('a')
    new_links = []
    results = []

    for h in range(len(links)):
        if links[h].find('h3', class_='LC20lb') is not None:
            new_links.append(links[h])

    for r in new_links:
        link = r.get('href')
        head = r.find('h3').string
        rs = head, link
        results.append(rs)

    return results


def get_google_results(links_list):
    results = []
    for line in links_list:
        page = get_test_page(line)
        results_g = get_google_links(page)
        results += results_g
    return results
#

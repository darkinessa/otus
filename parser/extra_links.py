from bs4 import BeautifulSoup

from network_request import get_pages


def get_extra_links(html, query_text):
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


def get_extra_results(results, query_text):
    new_results = []
    for line in results:
        link = [line[1]]
        html = get_pages(link)
        extra_links = get_extra_links(html[0], query_text)
        new_results.append(extra_links)
    return new_results


def get_combine_results(results, extra_results):
    new_results = []
    for i, j in zip(results, extra_results):
        results = i, j
        new_results.append(results)
    return new_results

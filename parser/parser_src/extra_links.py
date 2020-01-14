from bs4 import BeautifulSoup

from parser_src.network_request import get_pages


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
                            results = text[0:300], link
                            links_list.append(results)
        return links_list

    except Exception as e:
        print(f'Something wrong with get_extra_links_soup, occurred {e}')
        return


def get_extra_results(html, query_text):
    try:
        new_results = []
        for page in html:
            extra_links = get_extra_links_soup(page, query_text)
            new_results.append(extra_links)
            # через append, что бы сохранить пустые результаты и len extra_results и results из поисковика совпадала
        return new_results

    except Exception as e:
        print(f'Something wrong with get_extra_results, occurred {e}')
        return


def get_pages_extra_results(search_results_list, quantity):
    try:
        html_list = []
        for line in search_results_list[0:quantity]:
            link = line[1]
            html = get_pages([link])  # [link]  потому что функция get_pages ждет список
            html_list += html
        return html_list

    except Exception as e:
        print(f'Something wrong with get_pages_extra_results, occurred {e}')
        return


def get_combined_results(search_results_list, extra_results, quantity):
    try:
        if len(search_results_list[0:(quantity)]) == len(extra_results):
            new_results = []
            for i, j in zip(search_results_list[0:quantity], extra_results):
                results = i, j
                new_results.append(results)
            return new_results
        else:
            print(len(search_results_list), len(extra_results))
            raise ValueError

    except Exception as e:
        print(f'Something wrong with get_combined_results , occurred {e}')
        return


def get_results_with_extra_link(search_results_list, quantity, query_text):
    html = get_pages_extra_results(search_results_list, quantity)
    extra_results = get_extra_results(html, query_text)
    combined_results = get_combined_results(search_results_list, extra_results, quantity)
    return combined_results

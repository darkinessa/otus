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
                            results = text, link
                            links_list.append(results)
        return links_list

    except Exception as e:
        print(f'Something wrong, occurred {e}')
        return


def get_extra_results(html, query_text):
    try:
        new_results = []
        for page in html:
            extra_links = get_extra_links_soup(page[0], query_text)
            new_results.append(extra_links)
            # через append, что бы сохранить пустые результаты и len extra_results и results из поисковика совпадала
        return new_results

    except Exception as e:
        print(f'Something wrong, occurred {e}')
        return


def get_pages_extra_results(results):
    try:
        pages = []
        for line in results:
            link = [line[1]]
            html = get_pages(link)
            pages.append(html)
        return pages

    except Exception as e:
        print(f'Something wrong, occurred {e}')
        return


def get_combined_results(results, extra_results):
    try:
        if len(results) == len(extra_results):
            new_results = []
            for i, j in zip(results, extra_results):
                results = i, j
                new_results.append(results)
            return new_results
        else:
            raise ValueError

    except Exception as e:
        print(f'Something wrong, occurred {e}')
        return

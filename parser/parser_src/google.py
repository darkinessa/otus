from bs4 import BeautifulSoup
from parser_src.network_request import get_pages
from parser_src.urls_settings import validate_url_address, create_google_url


def get_google_soup_results(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        links = soup.find('div', id="search").find_all('a')
        new_links = []
        results = []

        for heads in range(len(links)):
            if links[heads].find('h3', class_='LC20lb') is not None:
                new_links.append(links[heads])

        for line in new_links:
            link = line.get('href')
            head = line.find('h3').string
            result = head, validate_url_address(link)
            results.append(result)

        return results

    except Exception as e:
        print(f'Something wrong with get_google_soup_results, occurred {e}')
        return


def get_google_results(query_text, quantity_links):
    try:
        results = []
        urls = create_google_url(query_text, quantity_links)
        pages = get_pages(urls)
        for page in pages:
            results_google = get_google_soup_results(page)
            results += results_google
        return results
    except Exception as e:
        print(f'Something wrong with get_google_results, occurred {e}')
        return

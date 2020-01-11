from bs4 import BeautifulSoup
from parser_src.input_options import prepare_query_text
from parser_src.network_request import get_pages


def create_google_url(query_text, quantity_links):
    try:
        quantity_links = int(quantity_links)
    except ValueError as e:
        print('{e}')
        return

    base_url = 'https://www.google.com/search?q='
    urls = []
    text = prepare_query_text(query_text)

    if quantity_links >= 6:
        quantity_links = int(quantity_links) + 10

        for start in [i * 10 for i in range(quantity_links // 10)]:
            if start == 0:
                url = str(base_url + text + '&newwindow=1' + '&sourceid=chrome&ie=UTF-8')
            if start != 0:
                url = str(base_url + text + '&newwindow=1' + '&start=' + str(start) + '&biw=1680&bih=819')

            urls.append(url)

    else:
        url = str(base_url + text + '&newwindow=1' + '&sourceid=chrome&ie=UTF-8')
        urls.append(url)

    return urls


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
            result = head, link
            results.append(result)

        return results

    except Exception as e:
        print(f'Something wrong, occurred {e}')
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
        print(f'Something wrong, occurred {e}')
        return
#done
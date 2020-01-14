import requests
from user_agent import generate_user_agent


def get_html(link):
    headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
    session = requests.Session()
    try:
        page_response = session.get(link, headers=headers, timeout=(5, 10))
        page_response.encoding = 'utf-8'
        html = page_response.text
        if page_response.status_code == 200:
            response = html
        elif page_response.status_code != 200:
            response = f'что-то пошло не так c get_html, код ошибки {page_response.status_code}'

        else:
            raise Exception

    except Exception as e:
        response = f'что-то пошло не так c get_html: \n  {e}'

    return response


def get_pages(urls):
    pages = []
    for url in urls:
        page = get_html(url)
        pages.append(page)
    return pages

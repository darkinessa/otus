import quopri
import re


def validate_url_address(some_text):
    link = some_text

    if some_text and link.startswith('http'):
        if len(link.split()) == 1:
            return link
        else:
            return ''.join(link.split())
    else:
        return


def prepare_query_text(query_text):
    # подготовить текст для создания url
    if len(query_text.split()) > 1:
        text = '+'.join(query_text.split())
    else:
        text = query_text

    return text


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


def create_google_url(query_text, quantity_links):
    try:
        quantity_links = int(quantity_links)
    except ValueError as e:
        print(f'{e}')
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


def create_yandex_url(query_text, quantity_links):
    try:
        quantity_links = int(quantity_links)
    except Exception as err:
        print(f'Something wrong with  create_yandex_url, occurred {err}')
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

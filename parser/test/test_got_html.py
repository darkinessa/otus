from parser_src.network_request import get_html
from test.mock.get_respose_mocks import output_response


def test_got_html():
    link = 'https://httpbin.org/'
    exp = output_response
    output = get_html(link)
    print(output)
    assert output == exp

def test_got_html_with_bad_getway():
    link = "https://httpbin.org/status/502"
    exp = 'что-то пошло не так c get_html, код ошибки 502'
    output = get_html(link)
    print(output)
    assert output == exp


from google import get_google_links, g_page
from selection import selection_options
from yandex import get_yandex_links, y_page


def print_results(result, quantity):
    с = 1
    for i in result[0:quantity]:
        print(с, i[0])
        print(i[1])
        с += 1
        print()


def main():
    issues = list(selection_options())
    quantity = issues[1]
    google_results = get_google_links(g_page)
    yandex_results = get_yandex_links(y_page)

    print(issues[0])
    print()

    if issues[0] == 'y':

        if len(yandex_results) >= issues[1]:
            print_results(yandex_results, quantity)

    if issues[0] == 'g':
        google_results = get_google_links(g_page)
        print_results(google_results, quantity)

    if issues[0] == 'b':
        if len(google_results) + len(yandex_results) >= quantity:
            if quantity % 2 == 0:
                results = google_results[0:(int(quantity / 2))] + yandex_results[0:(int(quantity / 2))]
            else:
                results = google_results[0:(int(quantity / 2) + 1)] + yandex_results[0:(int(quantity / 2))]

        print_results(results, quantity)


if __name__ == "__main__":
    main()

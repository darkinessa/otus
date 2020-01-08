from google import g_lll, get_google_results
from input_options import input_options
from yandex import y_lll, get_yandex_results





def print_results(result, quantity):
    counter = 1
    for line in result[0:quantity]:
        print(counter, line[0])
        print(line[1])
        counter += 1
        print()


def main():
    issues = list(input_options())
    search_engine = issues[0]
    quantity = issues[1]
    google_link_list = g_lll
    yandex_link_list = y_lll

    if search_engine == 'g':
        google_results = get_google_results(google_link_list)
        print_results(google_results, quantity)

    if search_engine == 'y':
        yandex_results = get_yandex_results(yandex_link_list)
        print_results(yandex_results, quantity)

    if search_engine == 'b':
        google_results = get_google_results(google_link_list)
        yandex_results = get_yandex_results(yandex_link_list)
        results = list(set(google_results + yandex_results))
        print_results(results, quantity)

    print(issues[0])
    print()

    # if issues[0] == 'y':
    #
    #     if issues[1] < 10:
    #         print_results(yandex_results, quantity)
    #     if issues[1] >= 10:
    #         yandex_results = get_several_page(y_lll)
    #
    #         print_results(yandex_results, quantity)
    #
    # if issues[0] == 'g':
    #     google_results = get_several_page(g_lll)
    #     print(quantity)
    #     print_results(google_results, quantity)
    #     print(len(google_results))

    # if issues[0] == 'b':
    #     results = []
    #     if len(google_results) + len(yandex_results) >= quantity:
    #         if quantity % 2 == 0:
    #             results = google_results[0:(int(quantity / 2))] + yandex_results[0:(int(quantity / 2))]
    #         else:
    #             results = google_results[0:(int(quantity / 2) + 1)] + yandex_results[0:(int(quantity / 2))]

    # print_results(results, quantity)


if __name__ == "__main__":
    main()

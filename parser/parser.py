from google import get_google_links
from selection import selection_options
from yandex import get_yandex_links, page


def main():
    issues = list(selection_options())
    print(issues[0])
    print()

    if issues[0] == 'y':

        results = get_yandex_links(page)
        if len(results) >= issues[1]:
            for tupl in results[0:(issues[1])]:
                print(tupl[0], tupl[1])
                print(tupl[2])
                print()
    else:
        print('noooo')

    if issues[0] == 'g':
        results = get_google_links(page)



if __name__ == "__main__":
    main()

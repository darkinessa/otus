def print_results(result, quantity):
    с = 1
    if not result:
        print('Упс! Кажется нас забанили. Поопробуйте другую поисковую систему или смените IP')

    for line in result[0:quantity]:
        if len(line) == 2:
            print(с, line[0])
            print(line[1])
        else:
            continue
        с += 1

    return 'done'


def print_extra_results(results, quantity):
    if results:
        c = 1
        for result in results[0:quantity]:
            print()
            main_result = result[0]
            extra_results = result[1]
            print(f'{c}.  {main_result[0]}')
            print(main_result[1])
            print()
            print(f'Дополнительно: {len(extra_results)}')

            if len(extra_results) > 0:
                for i in extra_results:
                    print(i[0], i[1])
            c += 1
        return 'done'
    else:
        return "Кажется нас забанили, попробуте сменить IP иои выберать другой пооисковик "

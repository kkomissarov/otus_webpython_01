import argparse

def get_args():
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)
    group.description = 'В какой поисковой системе искать ваш запрос'
    group.add_argument('-y', '--yandex', action="store_true")
    group.add_argument('-g', '--google', action="store_true")

    parser.add_argument(
        '-q',
        '--query',
        type=str,
        help='Запрос, по которому будет выполняться поиск',
        required=True
    )

    parser.add_argument(
            '-c',
            '--count',
            type=int,
            help='Сколько ссылок нужно найти',
        )

    parser.add_argument(
        '-r',
        '--recursive',
        help='Если параметр указан, программа будет заходить на страыницы',
        action='store_true'
    )

    parser.set_defaults(recursive=False, count=10)
    args = parser.parse_args()

    return args

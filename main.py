import requests
from tools.terminal import get_args
from tools.urls import get_url_params, get_startpoint, get_all_links


def get_and_print_links(url, params=None):
    response = requests.get(url, params=params)
    links = get_all_links(response)
    for link in links:
        print(link)
    return links

def main():
    args = get_args()
    startpoint = get_startpoint(args)
    url_params = get_url_params(args)
    links = get_and_print_links(startpoint, url_params)

    if args.recursive:
        for link in links:
            get_and_print_links(link)

if __name__ == '__main__':
    main()

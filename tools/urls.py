from bs4 import BeautifulSoup as bs
from .config import (
    yandex_default_params,
    google_default_params,
    yandex_path,
    google_path
)

def get_url_params(args):
    if args.yandex:
        url_params = {**yandex_default_params, 'text': args.query}
    elif args.google:
        url_params = {**google_default_params, 'q': args.query}
    return url_params


def get_startpoint(args):
    if args.yandex:
        startpoint = yandex_path
    elif args.google:
        startpoint = google_path
    return startpoint


def get_domain(url):
    return url.split('//')[0] + '//' + url.split('//')[1].split('/')[0]


def get_full_url(link, domain, base):
    if link.startswith('https://') or link.startswith('http://'):
        result = link
    elif link.startswith('/'):
        result = domain + link
    elif ':' in link or '#' in link:
        result = None
    elif base:
        result = base + link
    else:
        result = domain + link
    return result


def get_all_links(response):
    html = response.text
    soup = bs(html, 'lxml')
    all_links = {link.attrs['href'] for link in soup.find_all('a', href=True)}
    base_url = soup.find('base').attrs['href'] if soup.find('base') else None
    domain = get_domain(response.url)

    cleaned_links = set()
    for link in all_links:
        cleaned_link = get_full_url(link, domain, base_url)
        if cleaned_link:
            cleaned_links.add(cleaned_link)
    return cleaned_links


import sys
import argparse
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
#from _version import version

# version number
version = 2.01

def init() ->list:
    sysargs = argparse.ArgumentParser(description="Loads passed url to file after initial cleaning (munging).")
    sysargs.add_argument("-v", "--version", action="version", version=f"Current version is {version}")
    sysargs.add_argument("-url", "-URL", action="append", help="program -url <firsturl> -url <secondurl> -url <n-url>")
    args = sysargs.parse_args()

    if args.url:
        return args.url #if there are urls return it
    return[] #if there is not urls return empy list


def get_response(uri):
    if not uri.lower().startswith('http'):
        uri = f'https://{uri}'

        # get website url and provides response
        # if error - exits with exception
    try:
        response = requests.get(uri)
        response.raise_for_status()

    except HTTPError as httperr:
        print(f"Http error: {httperr}")
        sys.exit(1)
    except Exception as err:
        print(f"Someting went really wrong!: {err}")
        sys.exit(1)
    return response.text


if __name__ == '__main__':
    urls = init()
    for u in urls:

        soup = BeautifulSoup(get_response(u), 'html.parser')
        # print(f"Worked! \n\n{soup.prettify()}")
        for link in soup.findAll("h3"):
            print(link.div.string)


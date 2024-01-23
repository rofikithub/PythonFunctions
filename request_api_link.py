# pip install requests

import requests


def request_api_link(link):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept-Encoding": "*",
        "Connection": "keep-alive",
        'Content-Type': 'application/json',
    }

    res = requests.get(link, headers=headers)

    print(res.json())


def main():
    link = "https://examgallery.com/api/option.php?id=442"
    request_api_link(link)


if __name__ == "__main__":
    main()

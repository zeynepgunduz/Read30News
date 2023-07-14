"""
It reads the first 30 news from https://news.ycombinator.com/.
"""
import requests
from bs4 import BeautifulSoup

target_url = "https://news.ycombinator.com/"
foundLinks = []


# print(requests.get(target_url).status_code)

def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def read_news(q):
    s = make_request(q)
    trs = s.find_all('tr', class_=['athing'])
    for tdd in trs:
        print(tdd.text)

read_news(target_url)


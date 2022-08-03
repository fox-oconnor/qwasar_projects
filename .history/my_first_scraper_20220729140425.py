
#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
    
def request_github_trending(url):
    r = requests.get(url)
    return r.text

def extract(page):
    soup = BeautifulSoup(page)
    soup.find


print(request_github_trending('https://github.com/trending'))

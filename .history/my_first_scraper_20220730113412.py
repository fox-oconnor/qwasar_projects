
#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
    
def request_github_trending(url):
    r = requests.get(url)
    return r

def extract(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    soup = soup.encode("utf-8")
    div =  soup.find_all('html')
    return div.encode


url = request_github_trending('https://github.com/trending')


print(extract(url))

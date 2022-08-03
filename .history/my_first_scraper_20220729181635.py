
#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
    
def request_github_trending(url):
    r = requests.get(url)
    return r

def extract(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find_all('div', class_="Box-row")


url = request_github_trending('https://github.com/trending')


print(extract(url))

#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
    
def request_github_trending(url):
    r = requests.get(url)
    return r

def extract(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    #div =  soup.find_all('article', class_="Box-row")
    div = soup.find_all('a', href)
    return div


url = request_github_trending('https://github.com/trending')


print(extract(url))


#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
    
def request_github_trending(url):
    r = requests.get(url)
    con = r.content
    return con

def extract(page):
    soup = BeautifulSoup(page, 'html.parser')
    print(soup.find_all('a', class_="Box-row"))


url = request_github_trending('https://github.com/trending')
print(url)
extract(url)

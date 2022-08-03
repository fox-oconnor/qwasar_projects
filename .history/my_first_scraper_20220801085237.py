#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
    
def request_github_trending(url):
    r = requests.get(url)
    return r

def extract(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    developer =  soup('span', class_="text-normal")
    stars = soup('span', class_="d-inline-block")
    repo = soup
    return developer


url = request_github_trending('https://github.com/trending')


print(extract(url))

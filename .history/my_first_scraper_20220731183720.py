#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
    
def request_github_trending(url):
    r = requests.get(url)
    return r

def extract(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    developer =  soup.find_all('span', class_="text-normal")
    stars = soup.find_all('span', class_="d-inline-block")
    repo = soup.find_all()
    return stars


url = request_github_trending('https://github.com/trending')


print(extract(url))

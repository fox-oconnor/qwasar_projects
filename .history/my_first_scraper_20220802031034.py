#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
    
def request_github_trending(url):
    r = requests.get(url)
    return r

def extract(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    trending_repos = soup("article", class_="Box-row")
    for repo in trending_repos:
        dev = repo.find("h1", class_="h3 1h-condensed")
        stars = repo.find("span", class_="d-inline-block float-sm-right")
        print(dev)
        #print(stars)


url = request_github_trending('https://github.com/trending')


print(extract(url))

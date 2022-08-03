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
        dev = repo.find("span", class_="text-normal")
        repo_name = repo.find()
        stars = repo.find("a", class_="Link--muted.d-inline-block.mr3")
        print(stars.text.strip())

def transform(html_repos):
    print("something here")

url = request_github_trending('https://github.com/trending')


print(extract(url))

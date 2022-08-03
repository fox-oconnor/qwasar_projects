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
        repo_name = repo.select("h1 a")
        stars = repo.find("span", class_="d-inline-block float-sm-right")
        print(repo_name.text)

def transform(html_repos):
    print("something here")

url = request_github_trending('https://github.com/trending')


print(extract(url))

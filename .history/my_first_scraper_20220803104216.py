#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
    
def request_github_trending(url):
    r = requests.get(url)
    return r

def extract(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    trending_repos = soup("article", class_="Box-row")
    return trending_repos  

def transform(html_repos):
    repo_listing = []
    for repo in html_repos:
        dev = repo.find("span", class_="text-normal")
        repo_name = repo.find("h1", class_="h3 lh-condensed", recursive=False)
        stars = repo.find("a", class_="Link--muted d-inline-block mr-3")
        repo_listing.append({'developer': dev.text})
        repo_listing.append({'repository_name': repo_name.text.replace("\n", "")})
        repo_listing.append({'nbr_star': stars.text.replace("\n", "").strip()})
    return repo_listing
    
    return html_repos
        


url = request_github_trending('https://github.com/trending')
repos = extract(url)

print(transform(repos))

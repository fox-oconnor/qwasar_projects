#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
    
def request_github_trending(url):
    r = requests.get(url)
    return r

def extract(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    trending_repos = soup("article", class_="Box-row")
    repo_listing = []
    for repo in trending_repos:
        #dev = repo.find("span", class_="text-normal")
        repo_name = repo.find("h1", class_="h3 lh-condensed", recursive=False)
        stars = repo.find("a", class_="Link--muted d-inline-block mr-3")
        #repo_listing.append(dev)
        repo_listing.append(repo_name)
        repo_listing.append({'nbr_star':stars.text})
    return repo_listing    

def transform(html_repos):
    data = []
    i = 0
    for item in html_repos:
        #html_repos[i] = item.text.strip().replace("/", "").replace("\n", "").split()
        i += 1 
    
    return html_repos
        


url = request_github_trending('https://github.com/trending')
repos = extract(url)

print(transform(repos))

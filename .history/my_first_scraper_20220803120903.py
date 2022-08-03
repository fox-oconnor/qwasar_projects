#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import io
import csv
    
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
        dev = dev.text.replace("/", "").strip()
        repo_name = repo_name.text.replace("\n", "").split("/")[1].strip()
        stars = stars.text.replace("\n", "").strip()
        repo_listing.append({'developer': dev, 'repository_name' : repo_name, 'nbr_stars' : stars})
    return repo_listing
        
def format(repositories_data):
    output = io.StringIO()
    file = open("data.csv", "w")
    csv = csv.writer(file, output)
    for ele in repositories_data:
        for new_key, new_value in ele.items():
            csv.writerow([new_key, new_value])
    con_csv = output.getvalue()
    file.close()        
    return csv

url = request_github_trending('https://github.com/trending')
repos = extract(url)

print(transform(repos))

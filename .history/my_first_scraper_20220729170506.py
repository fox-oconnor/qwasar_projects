
#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
    
def request_github_trending(url):
    r = requests.get(url)
    con = r.content

def extract(page):
    soup = BeautifulSoup(page, 'html.parser')
    soup.find



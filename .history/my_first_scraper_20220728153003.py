#! /usr/bin/env python3
import requests

def request_github_trending(url):
    #Return the result of the request

def extract(page):
    #find_all instances of the html code of the repo rows and return
    #use beautifulsoup4

def transform(html_repos):
    #takes an array of all the instances of html code of repo row
    #it will return an array of hash follow this format: 
    #  [{'developer': NAME, 'repository_name': REPO_NAME, 'nrb_stars': NBR_STARS}]


def format(repositories_data_):
    #takes a repo array of hash and transforms it and returns it into a csv string
    #each column will be separated by , and each line by \n
    #the columns will be: Developer, Repository Name, Number of Stars 
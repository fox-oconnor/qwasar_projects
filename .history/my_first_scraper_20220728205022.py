#! /usr/bin/env python3
#-*- coding: utf-8 -*-
import requests

r = requests.get('https://api.github.com/events')
r.text    
print(r.text)
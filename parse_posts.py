#!/usr/bin/env python3
from bs4 import BeautifulSoup
posts_html = ''
with open('../facebook-entoijevoisdemain/posts/posts_1.html', 'r') as f:
    posts_html = f.read()

soup = BeautifulSoup(posts_html, 'html.parser')
print(soup.prettify())

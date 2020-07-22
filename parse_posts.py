#!/usr/bin/env python3
from bs4 import BeautifulSoup
posts_html = ''
with open('../facebook-entoijevoisdemain/posts/posts_1.html', 'r') as f:
    posts_html = f.read()

soup = BeautifulSoup(posts_html, 'html.parser')


for pub in list(soup.body.find_all('div', class_='pam')):
    print("*New post:")
    pc = pub.find('div', class_='_2pin')
    with_media = pc.find('div', class_='_3-95') is not None
    csv_image = ''
    csv_video = ''
    csv_content = ''
    csv_date = ''

    if with_media:
        image = pc.find('img')
        if image is not None:
            csv_image = image['src']
            print(f'|-image: {csv_image}')

        video = pc.find('video')
        if video is not None:
            csv_video = video['src']
            print(f'|-video: {csv_video}')

        content = pc.find('div', class_='_3-95')
        csv_content = content.text
    else:
        csv_content = pc.text

    print(f'|-content: {csv_content}')

    date = pub.find('div', class_='_3-94')
    if date is not None:
        csv_date = date.text
        print(f'|-date: {csv_date}')

    print('')

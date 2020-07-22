#!/usr/bin/env python3
from bs4 import BeautifulSoup
def from_fr_month(m):
    c = {
            'janv.': '01',
            'févr.': '02',
            'mars': '03',
            'avr.': '04',
            'mai': '05',
            'juin': '06',
            'jui.': '07',
            'aou.': '08',
            'sep.': '09',
            'oct.': '10',
            'nov.': '11',
            'déc.': '12'
        }
    return c[m]

out = open('output.csv', 'w')
out.write('date_iso,date,title,content,image,video\n')

posts_html = ''
with open('posts.html', 'r') as f:
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

    lines = csv_content.split('\n')
    csv_title = lines[0]
    if len(csv_title) > 120:
        csv_title = csv_title[:117] + '...'
    print(f'|-title: {csv_title}')
    csv_content = csv_content.replace('\n', '\\n')
    csv_content = csv_content.replace('"', '""')
    csv_title = csv_title.replace('"', '""')

    date = pub.find('div', class_='_3-94')
    if date is not None:
        csv_date = date.text
        print(f'|-date: {csv_date}')
        ds = csv_date.split(' ')
        y = ds[2]
        m = from_fr_month(ds[1])
        d = ds[0].zfill(2)
        t = ds[4]
        csv_isodate = f'{y}-{m}-{d}T{t}:00'
        print(f'|-iso date: {csv_isodate}')

    print('')

    out.write(f'{csv_isodate},"{csv_date}","{csv_title}","{csv_content}","{csv_image}","{csv_video}"\n')

out.close()

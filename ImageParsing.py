import os
import shutil
import requests
from bs4 import BeautifulSoup
from urllib import request


URL = 'https://music.bugs.co.kr/chart/track/day/total'
PATH = os.getcwd() + '/static/images/'


# Scrapping html code
def get_html(target_url):
    _html = ""
    response = requests.get(target_url)
    if response.status_code == 200:
        _html = response.text
    return _html


# parse image url and save in list
def get_image_url():
    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')
    img_url = []

    for image in soup.select('a.thumbnail > img'):
        if image.has_attr('src'):
            img_url.append(image.get('src'))
        else:
            continue
    return img_url


# download album art in static/images directory
def download_album_arts():
    images = get_image_url()
    for i in range(0, 100):
        url = images[i]
        file_name = PATH + str(i + 1) + '.png'
        request.urlretrieve(url, file_name)


# delete all album art
def delete_album_art():
    path = os.getcwd() + '/static/images'
    if os.path.exists(path):
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        os.mkdir(path)


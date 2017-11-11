from bs4 import BeautifulSoup
from urllib import request
import requests
import os
import shutil


URL = 'https://music.bugs.co.kr/chart/track/day/total'
PATH = os.getcwd() + '/static/images/'


# Scrapping html code
def get_html(target_url):
    _html = ""
    response = requests.get(target_url)
    if response.status_code == 200:
        _html = response.text
    return _html


# return today's chart information with jsonArray
def get_chart_info():
    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')

    title = []
    for SongTitle in soup.select('p.title > a'):
        title.append(SongTitle.text.strip())

    artist = []
    for ArtistName in soup.select('p.artist > a'):
        if ArtistName.has_attr('class'):
            continue
        else:
            artist.append(ArtistName.text.strip())

    current_chart = []
    for i in range(0, 100):
        song_info = {
            'title': title[i],
            'artist': artist[i]
        }
        current_chart.append(song_info)

    return current_chart


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

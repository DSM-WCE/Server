from bs4 import BeautifulSoup
from urllib import request
import requests
import os
import shutil


URL = 'https://music.bugs.co.kr/chart/track/day/total'
PATH = os.getcwd() + '/static/images/'


# 전체 html 코드를 스크래핑하는 함수
def get_html(target_url):
    _html = ""
    response = requests.get(target_url)
    if response.status_code == 200:
        _html = response.text
    return _html


# 일별 차트의 정보를 반환하는 함수
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


# 이미지 url을 파싱해서 list 형태로 반환하는 함수
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


# 앨범아트를 다운로드해서 저장하는 함수
def download_album_arts():
    images = get_image_url()
    for i in range(0, 100):
        url = images[i]
        file_name = PATH + str(i + 1) + '.jpg'
        request.urlretrieve(url, file_name)


# 디렉토리의 저장된 모든 앨범아트를 지우는 함수
def delete_album_art():
    path = os.getcwd() + '/static/images'
    if os.path.exists(path):
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        os.mkdir(path)



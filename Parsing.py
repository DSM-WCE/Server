from bs4 import BeautifulSoup
from collections import OrderedDict
import json
import requests


URL = 'https://music.bugs.co.kr/chart/track/day/total'


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
        song_info = OrderedDict()
        song_info['title'] = title[i]
        song_info['artist'] = artist[i]
        current_chart.append(json.dumps(song_info, ensure_ascii=False, indent='\t'))

    return current_chart

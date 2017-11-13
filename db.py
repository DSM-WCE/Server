from pymongo import MongoClient
from collections import OrderedDict
import json
import os

import Parsing

PATH = os.path.join(os.getcwd(), 'static', 'images')
CONNECTION = MongoClient('localhost', 27017)
DB = CONNECTION.wce


# DB에 일별 차트의 가수, 아티스트, 순위 등의 정보를 저장하는 함수
def insert_chart():
    collection = DB['chart_info']
    chart_info = Parsing.get_chart_info()
    docs = []

    for i in range(0, 100):
        song_name = chart_info[i]['title']
        singer = chart_info[i]['artist']
        req_path = '/static/images/' + str(i+1) + '.jpg'
        insert_data = {
            'rank': i+1,
            'title': song_name,
            'artist': singer,
            'request_url': req_path
        }
        docs.append(insert_data)

    collection.insert_many(docs)


# DB에 저장되어있던 일별 차트의 정보 json 배열로 리턴하는 함수
def get_chart():
    collection = DB['chart_info']
    result = collection.find()
    chart = []
    for doc in result:
        chart_info = OrderedDict()
        chart_info['rank'] = doc['rank']
        chart_info['title'] = doc['title']
        chart_info['artist'] = doc['artist']
        chart_info['request_url'] = doc['request_url']
        chart.append(chart_info)

    return json.dumps(chart, ensure_ascii=False, indent='\t')


# 컬렉션의 모든 도큐먼트를 삭제하는 함수
def remove_documents():
    collection = DB['chart_info']
    collection.remove()

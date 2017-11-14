from pymongo import MongoClient
from collections import OrderedDict
from apscheduler.schedulers.blocking import BlockingScheduler
import json
import os

import Parsing

PATH = os.path.join(os.getcwd(), 'static', 'images')
CONNECTION = MongoClient('mongodb://wce_club:asd456852!@ds257495.mlab.com:57495/wce')
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
    data = OrderedDict()
    chart = []
    for doc in result:
        chart_info = OrderedDict()
        chart_info['rank'] = doc['rank']
        chart_info['title'] = doc['title']
        chart_info['artist'] = doc['artist']
        chart_info['request_url'] = doc['request_url']
        chart.append(chart_info)
    data['key'] = chart

    return json.dumps(data, ensure_ascii=False, indent='\t')


# 컬렉션의 모든 도큐먼트를 삭제하는 함수
def remove_documents():
    collection = DB['chart_info']
    collection.remove()


# DB를 초기화하고 정보를 다시 받아오는 함수(스케줄링할 때)
def update_db():
    collection = DB['chart_info']
    if collection.count() is 0:
        insert_chart()
        Parsing.delete_album_art()
        Parsing.download_album_arts()
    else:
        remove_documents()
        insert_chart()
        Parsing.delete_album_art()
        Parsing.download_album_arts()


# update_db()를 매일 0시에 업데이트하는 함수
def scheduled_update():
    scheduler = BlockingScheduler()

    scheduler.add_job(update_db, 'cron', month='1-12', day='*', hour='0', minute='0', second='0')

    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemExit):
        print('end')
        pass

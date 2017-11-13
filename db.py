from pymongo import MongoClient
import gridfs
import os

import Parsing

PATH = os.getcwd() + '/static/images/'
CONNECTION = MongoClient('localhost', 27017)
DB = CONNECTION.wce

def insert_chart():
    collection = DB['chart_info']
    chart_info = Parsing.get_chart_info()
    docs = []

    for i in range(0, 100):
        song_name = chart_info[i]['title']
        singer = chart_info[i]['artist']
        insert_data = {
            'rank': i+1,
            'title': song_name,
            'artist': singer
        }
        docs.append(insert_data)

    collection.insert_many(docs)


def insert_image():
    for i in range(0, 100):
        file_name = PATH + str(i+1) + '.jpg'
        data_file = open(file_name, 'rb').read()

        fs = gridfs.GridFS(DB)
        fs.put(data_file, rank=i+1, fileName=str(i+1) + '.jpg')


# stored = fs.get_last_version(fileName='1.jpg')
# output_data = stored.read()
#
# with open(os.getcwd() + '/1.jpg', 'wb') as output:
#     output.write(output_data)


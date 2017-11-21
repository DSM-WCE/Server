from flask import Flask
from flask import send_from_directory
import os
import threading

import db


app = Flask(__name__)
static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/static/<path:path>', methods=['GET'])
def send(path):
    return send_from_directory(static_file_dir, path)


@app.route('/chart/', methods=['GET'])
def get_chart_info():
    return db.get_chart()


def update():
    db.scheduled_update()


if __name__ == '__main__':
    thread = threading.Thread(target=update)
    thread.start()

    app.run(host='0.0.0.0', port=5000)


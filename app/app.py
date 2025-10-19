from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# 使用 Docker Compose 服務名稱作為主機名。
# 埠號 27017 是 MongoDB 的預設埠號。
# 我們會在 docker-compose.yml 中命名資料庫服務為 'mongodb'。
mongo_client = MongoClient('mongodb', 27017)
db = mongo_client.website_db
counter_collection = db.access_counter


@app.route('/')
def hello_world():
    # 每次訪問時，將計數器加 1
    counter_collection.update_one(
        {'name': 'page_access'},
        {'$inc': {'count': 1}},
        upsert=True
    )

    # 讀取當前計數器
    data = counter_collection.find_one({'name': 'page_access'})

    count = data.get('count', 0) if data else 0

    return jsonify({
        'message': 'Hello from Dockerized Python App!',
        'access_count': count
    })


if __name__ == '__main__':
    # Flask 預設運行在 5000 埠號
    app.run(host='0.0.0.0', port=5000)

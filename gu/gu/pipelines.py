# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import redis
from scrapy.conf import settings


class GuPipeline(object):
    def __init__(self):
        mongo_port = settings['MONGO_PORT']
        mongo_host = settings['MONGO_HOST']
        mongo_db = settings['MONGO_DB']
        clice = pymongo.MongoClient(port=mongo_port, host=mongo_host)
        db = clice[mongo_db]
        self.post = db[settings['MONGO_TABLE']]

    def process_item(self, item, spider):
        item1 = dict(item)
        self.post.insert_one(item1)
        return item


class Redispip(object):
    def __init__(self):
        self.redis = redis.Redis(db=0)

    def redis(self, item, spider):
        self.redis.set(item['ip'], dict(item))
        return item


from bson import ObjectId
from pymongo import MongoClient

from extractor import config


def mongo_client():
    return MongoClient(config.property('mongo.host'))


def get_video(video_id):
    collection = mongo_client()['einszwo_internal']['assets']
    return collection.find_one({'_id': ObjectId(video_id)})

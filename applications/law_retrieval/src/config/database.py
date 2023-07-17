from .settings import settings
import pymongo
from src.models.indexes import createIndex

mongo_client = pymongo.MongoClient(settings.get_mongo_database_url())

mongo_db = mongo_client.thlogistic

createIndex(mongo_db)

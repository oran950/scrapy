

import pymongo
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings
settings = get_project_settings()


class UniversityPipeline(object):
    def __init__(self):
        self.conn=pymongo.MongoClient(
            settings.get('MONGO_CONNECTION_STRING')
        )
        db=self.conn['IDC']
        self.collection = db[settings['MONGO_COLLECTION_NAME']]


    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item

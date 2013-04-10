import pymongo


class Processor(object):

    def __init__(self, connection=None):
        db = connection.test_database
        self.document_collection = db.documents

    def run_process(self):
        self.document_collection.save({
          '_type': '1', 
          '_id': 1,
          '_source': {'body': 'test', 'id': 1, 'dtyp': '1'},
          '_index': ''})

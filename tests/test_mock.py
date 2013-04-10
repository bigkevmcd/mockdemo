import unittest

import mock

from dougal.processor import Processor


class MockTestCase(unittest.TestCase):

    @mock.patch('pymongo.Connection')
    def setUp(self, pymongo_mock):
        self.p = Processor(connection=pymongo_mock)

    def test_add(self):
        self.p.run_process()
        self.p.document_collection.save.assert_called_with({
            '_type': '1',
            '_id': 1,
            '_source': {'body': 'test', 'id': 1,
                        'dtyp': '1'}, '_index': ''})

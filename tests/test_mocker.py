import mocker
import pymongo

from dougal.processor import Processor


class MockTestCase(mocker.MockerTestCase):

    def test_add(self):
        mock_connection = self.mocker.replace(pymongo.Connection)
        mock_connection.test_database

        mock_db = self.mocker.mock()
        self.mocker.result(mock_db)

        mock_db.documents.save({
            '_type': '1',
            '_id': 1,
            '_source': {'body': 'test', 'id': 1,
                        'dtyp': '1'}, '_index': ''})
        self.mocker.replay()

        p = Processor(connection=mock_connection)
        p.run_process()

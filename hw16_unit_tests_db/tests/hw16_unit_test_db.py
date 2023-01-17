import io
import unittest
from unittest.mock import patch

from hw16_unit_tests_db.hw16_database.hw16_db import DataBase, DataBaseDTO, DatabaseVerify


class TestDatabase(unittest.TestCase):
    def setUp(self) -> None:
        self.db_name = 'postgres'
        self.user = 'user'
        self.password = 'qwertyR1!'
        self.host = '127.0.0.1'
        self.port = '5001'
        self.table = 'customers'
        self.data = 'some data'
        self.database_verify = DatabaseVerify
        self.database_dto = DataBaseDTO(
            self.db_name,
            self.user,
            self.password,
            self.host,
            self.port
        )

        self.db = DataBase(self.database_dto)

    def tearDown(self) -> None:
        del self.db

    def test_1_connect_to_DataBase(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.db.connect()
            self.assertEqual(fake_out.getvalue(), f'Connect to DB: {self.db_name}\n')









if __name__ == '__main__':
    unittest.main()
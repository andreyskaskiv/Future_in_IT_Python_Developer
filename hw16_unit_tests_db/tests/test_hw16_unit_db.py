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

    def test_01_delete_DataBase_instance(self):
        self.db.__del__()
        self.assertEqual(DataBase.instance(), None)

    def test_02_enter_DataBase(self):
        pass

    def test_03_exit_DataBase(self):
        pass

    def test_04_connect_to_DataBase(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.db.connect()
            self.assertEqual(fake_out.getvalue(), f'Connect to DB: {self.db_name}\n')

    def test_05_close_to_DataBase(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.db.close()
            self.assertEqual(fake_out.getvalue(), f'Close connect to DB: {self.db_name}\n')

    def test_06_read_to_DataBase(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.db.read(self.table)
            self.assertEqual(
                fake_out.getvalue(),
                f'Read data from database: {self.db_name} from table: {self.table}\n')

    def test_07_write_to_DataBase(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.db.write(self.table, self.data)
            self.assertEqual(
                fake_out.getvalue(),
                f'Write {self.data} to DB: {self.db_name} table: {self.table}\n')


if __name__ == '__main__':
    unittest.main()

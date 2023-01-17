import io
import unittest
from unittest.mock import patch

from hw16_unit_tests_db.hw16_database.hw16_db import DataBase, DataBaseDTO, DatabaseVerify, DataBaseException


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

    # Positive tests
    def tearDown(self) -> None:
        del self.db

    def test_01_delete_DataBase_instance(self):
        self.db.__del__()
        self.assertEqual(DataBase.instance(), None)

    def test_02_enter_DataBase(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.db.__enter__()
            self.assertEqual(fake_out.getvalue(), f'Connect to DB: {self.db_name}\n')

    def test_03_exit_DataBase(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            exc_type, exc_val, exc_tb = None, None, None
            self.db.__exit__(exc_type, exc_val, exc_tb)
            self.assertEqual(fake_out.getvalue(), f'Close connect to DB: {self.db_name}\n')

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

    def test_08_correct_instance_data(self):
        self.assertEqual(self.db_name, self.db.db_name)
        self.assertEqual(self.user, self.db.user)
        self.assertEqual(self.password, self.db.password)
        self.assertEqual(self.host, self.db.host)
        self.assertEqual(self.port, self.db.port)

    def test_09_set_db_name(self):
        db_name = 'mysql'
        self.db.db_name = db_name
        self.assertEqual(db_name, self.db.db_name)

    def test_10_set_user(self):
        user = 'user'
        self.db.user = user
        self.assertEqual(user, self.db.user)

    def test_11_set_password(self):
        password = 'QWE123!ww'
        self.db.password = password
        self.assertEqual(password, self.db.password)

    def test_12_set_host(self):
        host = '127.0.0.1'
        self.db.host = host
        self.assertEqual(host, self.db.host)

    def test_13_set_port(self):
        port = '2222'
        self.db.port = port
        self.assertEqual(port, self.db.port)

    # Negative tastes
    def test_incorrect_db_name_type(self):
        wrong_type = 100
        with self.assertRaises(TypeError) as context:
            self.db.db_name = wrong_type
        self.assertEqual(str(context.exception), f'{wrong_type} must be a string')


if __name__ == '__main__':
    unittest.main()

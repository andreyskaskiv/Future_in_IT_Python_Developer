import io
import unittest
from unittest.mock import patch

from tests_example.hw16_database.hw16_db import DataBase, DataBaseDTO, DataBaseException


class TestDataBase(unittest.TestCase):
    def setUp(self) -> None:
        self.db_name = 'postgres'
        self.user = 'user'
        self.password = 'qwertyR1!'
        self.host = '127.0.0.1'
        self.port = '5000'
        self.table = 'customers'
        self.customers_data = 'some customers data'

        self.database_exception = DataBaseException
        self.dto = DataBaseDTO
        self.data_postgres = self.dto(
            self.db_name,
            self.user,
            self.password,
            self.host,
            self.port
        )

        self.database = DataBase
        self.database_instance = self.database(self.data_postgres)
        print(' ' * 20 + f'***{self._testMethodName}***')

    def tearDown(self) -> None:
        del self.data_postgres
        del self.database

    """Positive tests"""

    def test_init_database_correct_data(self):
        self.assertEqual(self.data_postgres.db_name, self.database_instance.db_name)
        self.assertEqual(self.data_postgres.user, self.database_instance.user)
        self.assertEqual(self.data_postgres.password, self.database_instance.password)
        self.assertEqual(self.data_postgres.host, self.database_instance.host)
        self.assertEqual(self.data_postgres.port, self.database_instance.port)

    def test_delete_database_instance(self):
        self.database_instance.__del__()
        self.assertEqual(self.database.instance(), None)

    def test_singleton_database_pattern(self):
        data_mysql = self.dto('mysql', 'user', 'passwordW!9', '127.0.0.1', '3000')
        database_mysql = self.database(data_mysql)

        print(id(database_mysql), id(self.database_instance))
        print(data_mysql.db_name, self.database_instance.db_name)

        self.assertEqual(id(database_mysql), id(self.database_instance))

    def test_connect_to_database(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.database_instance.connect()
        self.assertEqual(fake_out.getvalue(), f'Connect to DB: {self.db_name}\n')

    def test_close_connect_to_database(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.database_instance.close()
        self.assertEqual(fake_out.getvalue(), f'Close connect to DB: {self.db_name}\n')

    def test_read_from_database(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.database_instance.read(self.table)
        self.assertEqual(fake_out.getvalue(), f'Read data from database: {self.db_name}'
                                              f' from table: {self.table}\n')

    def test_write_to_database(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.database_instance.write(self.table, self.customers_data)
        self.assertEqual(fake_out.getvalue(), f'Write {self.customers_data} to DB: {self.db_name}'
                                              f' table: {self.table}\n')

    def test_set_correct_db_name(self):
        correct_db_name = 'mysql'
        self.database_instance.db_name = correct_db_name
        self.assertEqual(correct_db_name, self.database_instance.db_name)

    def test_set_correct_user(self):
        correct_username = 'user_john'
        self.database_instance.user = correct_username
        self.assertEqual(correct_username, self.database_instance.user)

    def test_set_correct_password(self):
        correct_password = 'mysql!12RE'
        self.database_instance.password = correct_password
        self.assertEqual(correct_password, self.database_instance.password)

    def test_set_correct_host(self):
        correct_host = '8.8.8.8'
        self.database_instance.host = correct_host
        self.assertEqual(correct_host, self.database_instance.host)

    def test_set_correct_port(self):
        correct_port = '5001'
        self.database_instance.port = correct_port
        self.assertEqual(correct_port, self.database_instance.port)

    """Negative tastes"""

    def test_with_wrong_types(self):
        data = self.dto(None, None, None, None, None)
        with self.assertRaises(TypeError) as error_context:
            self.database(data)
        self.assertEqual('None must be a string', str(error_context.exception))

    def test_with_wrong_db_name(self):
        wrong_db_name = 'oracle'
        with self.assertRaises(self.database_exception) as error_context:
            self.database_instance.db_name = wrong_db_name
        self.assertEqual(
            f'Unsupported DB: {wrong_db_name}. Use these names: {self.database_instance.databases}',
            str(error_context.exception)
        )

    def test_username_with_superuser_root(self):
        root = 'root'
        with self.assertWarns(Warning) as warning_context:
            self.database_instance.user = root
        self.assertEqual(f'Use {root} user is dangerous', str(warning_context.warning))

    def test_host_with_wrong_ipaddress(self):
        wrong_host = '10.3.10.270'
        with self.assertRaises(self.database_exception) as error_context:
            self.database_instance.host = wrong_host
        self.assertEqual(
            "'10.3.10.270' does not appear to be an IPv4 or IPv6 address",
            str(error_context.exception)
        )

    def test_host_with_unreachable_host(self):
        unreachable_host = '192.168.0.99'
        with self.assertRaises(self.database_exception) as error_context:
            self.database_instance.host = unreachable_host
        self.assertEqual(
            f'{unreachable_host} is not avaliable',
            str(error_context.exception)
        )

    def test_port_with_not_numeric_value(self):
        not_numeric_port = 'wrong'
        with self.assertRaises(self.database_exception) as error_context:
            self.database_instance.port = not_numeric_port
        self.assertEqual(
            f'Port must contains numbers not {not_numeric_port}',
            str(error_context.exception)
        )

    def test_port_with_under_min_value(self):
        port_zero = '0'
        with self.assertRaises(self.database_exception) as error_context:
            self.database_instance.port = port_zero
        self.assertEqual(
            'Port must be between 0-65000',
            str(error_context.exception)
        )

    def test_port_with_over_max_value(self):
        port_over_max = '65000'
        with self.assertRaises(self.database_exception) as error_context:
            self.database_instance.port = port_over_max
        self.assertEqual(
            'Port must be between 0-65000',
            str(error_context.exception)
        )

    def test_database_context_manager(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with self.database(self.data_postgres) as db:
                db.write(self.table, self.customers_data)
        self.assertEqual(
            fake_out.getvalue(), f'Connect to DB: {db.db_name}\n'
                                 f'Write {self.customers_data} to DB: {db.db_name} table: {self.table}\n'
                                 f'Close connect to DB: {db.db_name}\n'
        )

    def test_password_with_not_enough_value(self):
        not_enough_password = 'asd!5'
        with self.assertRaises(self.database_exception) as error_context:
            self.database_instance.password = not_enough_password
        self.assertEqual(
            'Password must be at least 8 chars include Upper, Lower, Digit, Punctuation',
            str(error_context.exception)
        )

    def test_password_with_empty_value(self):
        empty_value = '   '
        with self.assertRaises(ValueError) as error_context:
            self.database_instance.password = empty_value
        self.assertEqual(
            'Empty string in values',
            str(error_context.exception)
        )


if __name__ == '__main__':
    unittest.main()

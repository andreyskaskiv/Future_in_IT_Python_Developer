from collections import namedtuple

import pytest

from tests_example.hw16_database.hw16_db import DataBase, DataBaseDTO, DataBaseException


class TestDatabase:
    def setup(self) -> None:
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

    def teardown(self) -> None:
        del self.data_postgres
        del self.database

    """Positive tests"""

    def test_00_singleton_database_pattern(self):
        data_mysql = DataBaseDTO('mysql', 'user', 'passwordW!9', '127.0.0.1', '3000')
        database_mysql = DataBase(data_mysql)

        assert id(database_mysql) == id(self.database_instance)

    def test_01_delete_database_instance(self):
        self.database_instance.__del__()
        assert self.database.instance() is None

    def test_02_enter_database(self, capsys):
        self.database_instance.__enter__()
        captured = capsys.readouterr()
        assert captured.out == f"Connect to DB: {self.db_name}\n"

    def test_03_exit_database(self, capsys):
        exc_type, exc_val, exc_tb = None, None, None
        self.database_instance.__exit__(exc_type, exc_val, exc_tb)
        captured = capsys.readouterr()
        assert captured.out == f'Close connect to DB: {self.db_name}\n'

    def test_04_connect_to_database(self, capsys):
        self.database_instance.connect()
        captured = capsys.readouterr()
        assert captured.out == f'Connect to DB: {self.db_name}\n'

    def test_05_close_to_database(self, capsys):
        self.database_instance.close()
        captured = capsys.readouterr()
        assert captured.out == f'Close connect to DB: {self.db_name}\n'

    def test_06_read_to_database(self, capsys):
        self.database_instance.read(self.table)
        captured = capsys.readouterr()
        assert captured.out == f'Read data from database: {self.db_name} from table: {self.table}\n'

    def test_07_write_to_database(self, capsys):
        self.database_instance.write(self.table, self.customers_data)
        captured = capsys.readouterr()
        assert captured.out == f'Write {self.customers_data} to DB: {self.db_name} table: {self.table}\n'

    def test_08_correct_instance_data(self):
        assert self.data_postgres.db_name == self.database_instance.db_name
        assert self.data_postgres.user == self.database_instance.user
        assert self.data_postgres.password == self.database_instance.password
        assert self.data_postgres.host == self.database_instance.host
        assert self.data_postgres.port == self.database_instance.port

    def test_09_set_db_name(self):
        db_name = 'mysql'
        self.database_instance.db_name = db_name
        assert db_name == self.database_instance.db_name

    def test_10_set_user(self):
        user = 'user'
        self.database_instance.user = user
        assert user == self.database_instance.user

    def test_11_set_password(self):
        password = 'QWE123!ww'
        self.database_instance.password = password
        assert password == self.database_instance.password

    def test_12_set_host(self):
        host = '8.8.8.8'
        self.database_instance.host = host
        assert host == self.database_instance.host

    def test_13_set_port(self):
        port = '2222'
        self.database_instance.port = port
        assert port == self.database_instance.port

    """Negative tastes"""

    def test_14_incorrect_db_name_type(self):
        data = self.dto(None, None, None, None, None)
        with pytest.raises(TypeError) as context:
            self.database(data)
        assert str(context.value) == f'None must be a string'

    def test_15_incorrect_db_name_empty_field(self):
        wrong_value = ''
        with pytest.raises(ValueError) as context:
            self.database_instance.db_name = wrong_value
        assert str(context.value) == 'Empty string in values'

    def test_16_incorrect_db_name(self):
        wrong_value = 'oracle'
        with pytest.raises(self.database_exception) as context:
            self.database_instance.db_name = wrong_value
        assert str(context.value) == \
               f'Unsupported DB: {wrong_value}. Use these names: {self.database_instance.databases}'

    def test_17_incorrect_user(self):
        root = 'root'
        with pytest.warns(UserWarning) as context:
            self.database_instance.user = root
        assert context[0].message.args[0] == 'Use root user is dangerous'

    def test_18_incorrect_password(self):
        db_exception = 'Password must be at least 8 chars include Upper, Lower, Digit, Punctuation'
        Case = namedtuple('Case', 'wrong_password actual')

        CASES = (
            Case('1234567', db_exception),  # length_error
            Case('qwerty', db_exception),  # length_error
            Case('QWERTY', db_exception),  # length_error
            Case('12QWqw', db_exception),  # length_error

            Case('123456789', db_exception),  # digit_error
            Case('QWERTYUIO', db_exception),  # uppercase_error
            Case('qwertyuio', db_exception),  # lowercase_error

            Case('$%_`{|}~', db_exception),  # symbol_error
            Case('$%sss&\_`{|}~', db_exception),  # symbol_error
            Case('qwertyR158jgiop876', db_exception),  # symbol_error
        )

        for case in CASES:
            with pytest.raises(self.database_exception) as context:
                self.database_instance.password = case.wrong_password
                assert str(context.value) == case.actual

    def test_19_incorrect_host(self):
        wrong_host = '10.3.10.270'
        with pytest.raises(self.database_exception) as context:
            self.database_instance.host = wrong_host
        assert str(context.value) == f"'{wrong_host}' does not appear to be an IPv4 or IPv6 address"

    def test_20_host_with_unreachable_host(self):
        unreachable_host = '192.168.0.99'
        with pytest.raises(self.database_exception) as error_context:
            self.database_instance.host = unreachable_host
        assert f'{unreachable_host} is not avaliable' == str(error_context.value)

    def test_21_incorrect_port(self):
        Case = namedtuple('Case', 'wrong_port actual')

        CASES = (
            Case('5001ww', f'Port must contains numbers not 5001ww'),
            Case('0', f'Port must be between 0-65000'),
            Case('0000', f'Port must be between 0-65000'),
            Case('65001', f'Port must be between 0-65000'),
            Case('65555', f'Port must be between 0-65000'),
        )

        for case in CASES:
            with pytest.raises(Exception) as context:
                self.database_instance.port = case.wrong_port
            assert context.value.args[0] == case.actual

    def test_22_database_context_manager(self, capsys):
        with self.database(self.data_postgres) as db:
            db.write(self.table, self.customers_data)

        captured = capsys.readouterr()
        assert captured.out == f'Connect to DB: {db.db_name}\n'\
                               f'Write {self.customers_data} to DB: {db.db_name} table: {self.table}\n'\
                               f'Close connect to DB: {db.db_name}\n'


if __name__ == '__main__':
    pytest.main()

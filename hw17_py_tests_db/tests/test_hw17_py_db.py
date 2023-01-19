from collections import namedtuple

import pytest

from hw17_py_tests_db.hw17_database.hw17_db import DataBase, DataBaseDTO, DatabaseVerify


class TestDatabase:
    db_name = 'postgres'
    user = 'user'
    password = 'qwertyR1!'
    host = '127.0.0.1'
    port = '5001'
    table = 'customers'
    data = 'some data'
    databases = ('postgres', 'mysql', 'sqlite')
    database_verify = DatabaseVerify
    database_dto = DataBaseDTO(
        db_name,
        user,
        password,
        host,
        port
    )

    db = DataBase(database_dto)

    """Positive tests"""

    def test_01_delete_DataBase_instance(self):
        self.db.__del__()
        assert DataBase.instance() == None

    def test_02_enter_DataBase(self, capsys):
        self.db.__enter__()
        captured = capsys.readouterr()
        assert captured.out == f"Connect to DB: {self.db_name}\n"

    def test_03_exit_DataBase(self, capsys):
        exc_type, exc_val, exc_tb = None, None, None
        self.db.__exit__(exc_type, exc_val, exc_tb)
        captured = capsys.readouterr()
        assert captured.out == f'Close connect to DB: {self.db_name}\n'

    def test_04_connect_to_DataBase(self, capsys):
        self.db.connect()
        captured = capsys.readouterr()
        assert captured.out == f'Connect to DB: {self.db_name}\n'

    def test_05_close_to_DataBase(self, capsys):
        self.db.close()
        captured = capsys.readouterr()
        assert captured.out == f'Close connect to DB: {self.db_name}\n'

    def test_06_read_to_DataBase(self, capsys):
        self.db.read(self.table)
        captured = capsys.readouterr()
        assert captured.out == f'Read data from database: {self.db_name} from table: {self.table}\n'

    def test_07_write_to_DataBase(self, capsys):
        self.db.write(self.table, self.data)
        captured = capsys.readouterr()
        assert captured.out == f'Write {self.data} to DB: {self.db_name} table: {self.table}\n'

    def test_08_correct_instance_data(self):
        assert self.db_name == self.db.db_name
        assert self.user == self.db.user
        assert self.password == self.db.password
        assert self.host == self.db.host
        assert self.port == self.db.port

    def test_09_set_db_name(self):
        db_name = 'mysql'
        self.db.db_name = db_name
        assert db_name == self.db.db_name

    def test_10_set_user(self):
        user = 'user'
        self.db.user = user
        assert user == self.db.user

    def test_11_set_password(self):
        password = 'QWE123!ww'
        self.db.password = password
        assert password == self.db.password

    def test_12_set_host(self):
        host = '127.0.0.1'
        self.db.host = host
        assert host == self.db.host

    def test_13_set_port(self):
        port = '2222'
        self.db.port = port
        assert port == self.db.port

    """Negative tastes"""

    def test_14_incorrect_db_name_type(self):
        wrong_type = 100
        with pytest.raises(TypeError) as context:
            self.db.db_name = wrong_type
        assert str(context.value) == f'{wrong_type} must be a string'

    def test_15_incorrect_db_name_empty_field(self):
        wrong_value = ''
        with pytest.raises(ValueError) as context:
            self.db.db_name = wrong_value
        assert str(context.value) == 'Empty string in values'

    def test_16_incorrect_db_name(self):
        wrong_value = 'qwqwqwqwqwqw'
        with pytest.raises(Exception) as context:
            self.db.db_name = wrong_value
        assert str(context.value) == f'Unsupported DB: {wrong_value}. Use these names: {self.databases}'

    def test_17_incorrect_user(self):
        wrong_value = 'root'
        with pytest.warns(UserWarning) as context:
            self.db.user = wrong_value
        assert context[0].message.args[0] == 'Use root user is dangerous'

    def test_18_incorrect_password(self):
        database_exception = 'Password must be at least 8 chars include Upper, Lower, Digit, Punctuation'
        Case = namedtuple('Case', 'wrong_password actual')

        CASES = (
            Case('1234567', database_exception),  # length_error
            Case('qwerty', database_exception),  # length_error
            Case('QWERTY', database_exception),  # length_error
            Case('12QWqw', database_exception),  # length_error

            Case('123456789', database_exception),  # digit_error
            Case('QWERTYUIO', database_exception),  # uppercase_error
            Case('qwertyuio', database_exception),  # lowercase_error

            Case('$%_`{|}~', database_exception),  # symbol_error
            Case('$%sss&\_`{|}~', database_exception),  # symbol_error
            Case('qwertyR158jgiop876', database_exception),  # symbol_error
        )

        for case in CASES:
            with pytest.raises(Exception) as context:
                self.db.password = case.wrong_password
                assert str(context.value) == case.actual

    def test_19_incorrect_host(self):
        wrong_host = '127.0.0'
        with pytest.raises(Exception) as context:
            self.db.host = wrong_host
        assert str(context.value) == f"'{wrong_host}' does not appear to be an IPv4 or IPv6 address"

    def test_20_incorrect_port(self):
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
                self.db.port = case.wrong_port
            assert context.value.args[0] == case.actual


if __name__ == '__main__':
    pytest.main()

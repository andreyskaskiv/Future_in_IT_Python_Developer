from string import ascii_lowercase, ascii_uppercase
import re


class Person:
    __ALPHABET_UA = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    __ALPHABET_UPPER_UA = __ALPHABET_UA.upper()
    __OLD_MIN = 16
    __OLD_MAX = 66
    __WEIGHT_MIN = 40
    __WEIGHT_MAX = 130
    __PHONE_TEMPLATE = "+3(097)555-66-77"
    __PHONE_PATTERN = r"\+3\(\d{3}\)\d{3}-\d{2}-\d{2}\b"  # "+3(097)555-66-77"
    __PASSPORT_TEMPLATE = "ВР-415141"
    __PASSPORT_PATTERN = r"^[A-Z]{2}-[0-9]{6}\b"  # 'ВР-415141'

    def __init__(self, username, old, passport, phone, weight):
        self.username = username  # call setter and verify_username
        self.old = old  # call setter and verify_old
        self.passport = passport  # call setter and verify_passport
        self.phone = phone  # call setter and verify_passport
        self.weight = weight  # call setter and verify_weight

    @classmethod
    def verify_username(cls, username):
        if type(username) != str:
            raise TypeError("ПІБ має бути рядком")

        name = username.split()
        if len(name) != 3:
            raise TypeError("Неправильний формат запису ПІБ")

        letters = ascii_lowercase + ascii_uppercase + cls.__ALPHABET_UA + cls.__ALPHABET_UPPER_UA + '-'
        for symbol in name:
            if len(symbol) < 1:
                raise TypeError("У ПІБ має бути хоча б один символ")
            if len(symbol.strip(letters)) != 0:
                raise TypeError("У ПІБ можна використовувати лише буквені символи та дефіс")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < cls.__OLD_MIN or old > cls.__OLD_MAX:
            raise TypeError(f"Вік має бути цілим числом у діапазоні [{cls.__OLD_MIN}; {cls.__OLD_MAX}]")

    @classmethod
    def verify_weight(cls, mass):
        if type(mass) != float or mass < cls.__WEIGHT_MIN:
            raise TypeError(f"Вага має бути дійсним числом від {cls.__WEIGHT_MIN} до {cls.__WEIGHT_MAX}")

    @classmethod
    def verify_passport(cls, document):
        if type(document) != str:
            raise TypeError("Паспорт має бути рядком")

        document = document.split()
        document = ''.join(document)
        match_document = re.match(cls.__PASSPORT_PATTERN, document)
        if not match_document:
            raise TypeError(f"Неправильний формат паспорта\n"
                            f"У серії можна використовувати лише великі буквені символи латинського алфавіту.\n"
                            f"У номері паспорта можна використовувати лише цифри."
                            f"Наприклад: '{cls.__PASSPORT_TEMPLATE}' ")

    @classmethod
    def verify_phone_number(cls, phone_number):
        if type(phone_number) != str:
            raise TypeError("Номер телефону має бути рядком")

        number = phone_number.split()
        number = ''.join(number)
        match_number = re.match(cls.__PHONE_PATTERN, number)
        if not match_number:
            raise TypeError(f"Неправильний формат номеру\n"
                            f"Наприклад: '{cls.__PHONE_TEMPLATE}' ")

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, name):
        self.verify_username(name)
        self.__username = name

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_passport(passport)
        self.__passport = passport

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone_number):
        self.verify_phone_number(phone_number)
        self.__phone = phone_number

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, mass):
        self.verify_weight(mass)
        self.__weight = mass


human = Person('Зеленський Володимир Олександрович', 44, 'BP-560890', '+3(097)555-66-77', 80.0)
print(human.__dict__)

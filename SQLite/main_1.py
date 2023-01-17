import random
import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor() # нужен для работы с БД, добавить ,проверить ....

sql.execute("""CREATE TABLE IF NOT EXISTS users (
                                                login TEXT,
                                                password TEXT,
                                                cash BIGINT)""")
db.commit()


def registration():
    user_login = input('Login: ')
    user_password = input('Password: ')
    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'") #выбрать столбец login в таблице users, где логин вот такой
    if sql.fetchone() is None:
        # sql.execute(f"INSERT INFO users VALUES ('{user_login}', '{user_password}', {0})")
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
        db.commit()

        print('Зарегестрирован')
    else:
        print('Такая запись уже имеется')

        for value in sql.execute("SELECT * FROM users"):
            print(value)


def delete_db(user_login):
    sql.execute(f"DELETE FROM users WHERE login = '{user_login}'")
    db.commit()
    print('Запись удалена')


def casino():
    user_login = input('Log in: ')
    number = random.randint(1, 1)

    for i in sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'"):
        balance = i[0]

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        print('Такого логина не существует, зарегестрируйтесь')
        registration()
    else:
        if number == 1:
            # обновить в таблице users добавить в столбец cash {1000} где логин == таким
            sql.execute(f"UPDATE users SET cash = {1000 + balance} WHERE login = '{user_login}'")
            db.commit()
        else:
            print('Вы проиграли!')
            delete_db(user_login)


def enter():
    for i in sql.execute("SELECT login, cash FROM users"):
        print(i)

if __name__ == '__main__':
    casino()
    enter()

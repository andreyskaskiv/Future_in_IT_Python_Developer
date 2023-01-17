cmd = ('Andrii Skaskiv', 'Python', 1987)

match cmd:
    case tuple() as book:
        print(f'class tuple:  = {book}')
    case _: #wildcard
        print(f'отрабатывает, когда все остальные не отработали ')


cmd = ('Andrii Skaskiv', 'Python', 2000)

match cmd:
    case author, title, price:  # Сразу с распаковкой
        print(f'Book: {author} {title} {price}')
    case _: #wildcard
        print(f'отрабатывает, когда все остальные не отработали ')



cmd = ('Andrii Skaskiv', 'Python', 2000, 55, 8755)

match cmd:
    case (author, title, price, *_) if len(cmd) < 6:  # Сразу с распаковкой, (), [] - не создают кортеж или список, просто для визуального восприятия
        print(f'Book: {author} {title} {price}')
    case _: #wildcard
        print(f'отрабатывает, когда все остальные не отработали ')


cmd = ('Andrii Skaskiv', 'Python', 2000, 55, 8755)

match cmd:
    case [str() as author, str() as title, int() | float() as price, *_] if len(cmd) < 6:  # С проверкой данных
        print(f'Book: {author} {title} {price}')
    case _: #wildcard
        print(f'отрабатывает, когда все остальные не отработали ')
def user_info(**kwargs):
    return ' '.join(kwargs.values())


print(user_info(Name='Вася', Surname='Пупкин', Birthday='1990', City='Питер', Email='vaskapupkin@mail.ru',
                Phone='8-800-555-35-35'))

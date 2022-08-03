from datetime import datetime as dt


def name_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('book_log.csv', 'a', encoding='UTF-8') as file:
        file.write(' {}; Имя; {}\n'.format(time, data))


def first_name_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('book_log.csv', 'a', encoding='UTF-8') as file:
        file.write(' {}; Фамилия; {}\n'.format(time, data))


def number_phone_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('book_log.csv', 'a', encoding='UTF-8') as file:
        file.write(' {}; Номер телефона; {}\n'.format(time, data))


def description_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('book_log.csv', 'a', encoding='UTF-8') as file:
        file.write(' {}; Описание; {}\n'.format(time, data))
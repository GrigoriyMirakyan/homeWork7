def name_create(data):
    with open('book_v1.txt', 'a', encoding='UTF-8') as file:
        file.write(f' Имя: {data};')
    with open('book_v2.txt', 'a', encoding='UTF-8') as file:
        file.write(f' Имя: {data};\n\n')


def first_name_create(data):
    with open('book_v1.txt', 'a', encoding='UTF-8') as file:
        file.write(f' Фамилия: {data};')
    with open('book_v2.txt', 'a', encoding='UTF-8') as file:
        file.write(f' Фамилия: {data};\n\n')


def number_phone_create(data):
    with open('book_v1.txt', 'a', encoding='UTF-8') as file:
        file.write(f' Номер телефона: {data};')
    with open('book_v2.txt', 'a', encoding='UTF-8') as file:
        file.write(f' Номер телефона: {data};\n\n')


def description_create(data):
    with open('book_v1.txt', 'a', encoding='UTF-8') as file:
        file.write(f' Описание: {data};')
    with open('book_v2.txt', 'a', encoding='UTF-8') as file:
        file.write(f' Описание: {data};\n\n\n')

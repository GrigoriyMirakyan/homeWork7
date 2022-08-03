def show_v1():
    with open('book_v1.txt', 'r', encoding='UTF-8') as file:
        content = file.read()
        print(content)

def show_v2():
    with open('book_v2.txt', 'r', encoding='UTF-8') as file:
        content = file.read()
        print(content)
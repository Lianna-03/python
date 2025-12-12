notebook = {}

def num_1():
    global notebook
    key = input("Введите заголовок:")
    value = input("Введите текст:")
    notebook[key] = value


def num_2():
    global notebook
    if not notebook:
        print("Заметок нет")
        menu()
    print("Доступные заметки:")
    for i, key in enumerate(notebook.keys(), 1):
        print(i, key)
    
    title = input("Введите название заметки:")

    if title in notebook:
        print(notebook[title])
    else:
        print("Такой заметки нет")

def num_3():
    global notebook
    if not notebook:
        print("Нет заметок")
        menu()

    print("Доступные заметки:")
    for i, key in enumerate(notebook.keys(), 1):
        print(i, key)
    
    dela = input("Введите название заметки:")
    
    if dela in notebook.keys():
        print(dela, "Был удален!!!")
        notebook.pop(dela)
    else:
        print("Такой заметки нет")

def menu():
    while True:
        print("[1] - Создать новую заметку. [2] - Показать все заметки. [3] - Удалить запись. [4] - Выход.")

        a = int(input("Выбирите действие: "))

        if a == 1:
            num_1()
        elif a == 2:
            num_2()
        elif a == 3:
            num_3()
        elif a == 4:
            print("Удачи тебе!!!")
            break
        else:
            print("Нет такой команды!!!")
            menu()

menu()

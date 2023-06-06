from functional import *
from interface import start

path = "phone_book.txt"

start()

actions = {"1": "список",
           "2": "запись",
           "3": "поиск",
           "4": "изменить",
           "5": "удалить",
           "q": "выйти"}
action = None

while action != "q":
    print("\n Что делать", *[f"{i} - {actions[i]}" for i in actions])
    action = input()
    while action not in actions:
        print("\n Что делать", *[f"{i} - {actions[i]}" for i in actions])
        action = input()
        if action not in actions:
            print("Неверные данные")
    if action != "q":
        if action == "1":
            print_records(path)
        elif action == "2":
            input_records(path)
        elif action == "3":
            find_records(path, *find_char())
        elif action == "4":
            change_records(path)
        elif action == "5":
            delete_records(path)
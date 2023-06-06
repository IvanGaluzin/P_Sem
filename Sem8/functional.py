path = "phone_book.txt"
def print_records(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(*line.split(';'), end='')

def input_records(file_name: str):
    with open(file_name, 'r+', encoding='utf-8') as data:
        record_id = 0
        for line in data:
            if line != '':
                record_id = line.split(';', 1)[0]
        print('Enter FCS thru space')
        line = f'{int(record_id) + 1};' + ';'.join(input().split()[:4]) + ';\n'
        confirm = confirmation('добавить запись')
        if confirm == 'y':
            data.write(line)

def find_char():
    print('Выбрать символ: ')
    print('0 - идентификатор, 1 - второе имя, 2 - имя, 3 - третье имя, 4 - номер, q - выход')
    char = input()
    while char not in ('0', '1', '2', '3', '4', 'q'):
        print('Неверные данные')
        print('Выбрать символ: ')
        print('0 - идентификатор, 1 - второе имя, 2 - имя, 3 - третье имя, 4 - номер, q - выход')
        char = input()
    if char != 'q':
        inp = input('Введите значение\n')
        return char, inp
    else:
        return 'q', 'q'

def find_records(file_name: str, char, condition):
    if condition != 'q':
        printed = False
        with open(file_name, 'r', encoding='utf-8') as data:
            for line in data:
                if condition == line.split(';')[int(char)]:
                    print(*line.split(';'))
                    printed = True
        if not printed:
            print("Ничего не найдено")
        return printed

def check_id_record(file_name: str, text: str):
    decision = input(f'Подтвердить {text} запись: y - да, n - нет\n')
    while decision not in ('1', 'q'):
        if decision != '2':
            print('Неверные данные')
        else:
            find_records(path, *find_char())
        decision = input(f'Подтвердить {text} запись: y - да, n - нет\n')
    if decision == '1':
        record_id = input('enter id, q - quit\n')
        while not find_records(file_name, '0', record_id) and record_id != 'q':
            record_id = input('Введите ИД, q - Выход\n')
        return record_id
    return decision

def confirmation(text: str):
    confirm = input(f"Подтвердить {text} запись: y - да, n - нет\n")
    while confirm not in ('y', 'n'):
        print('Data incorrect')
        confirm = input(f"Подтвердить {text} запись: y - да, n - нет\n")
    return confirm

def replace_record_line(file_name: str, record_id, replaced_line: str):
    replaced = ''
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            replaced += line
            if record_id == line.split(';', 1)[0]:
                replaced = replaced.replace(line, replaced_line)
    with open(file_name, 'w', encoding='utf-8') as data:
        data.write(replaced)

def change_records(file_name: str):
    record_id = check_id_record(file_name, 'изменить')
    if record_id != 'q':
        replaced_line = f'{int(record_id)};' + ';'.join(
            input('Enter FCS thru space\n').split()[:4]) + ';\n'
        confirm = confirmation('изменить')
        if confirm == 'y':
            replace_record_line(file_name, record_id, replaced_line)

def delete_records(file_name: str):
    record_id = check_id_record(file_name, 'Удалить')
    if record_id != 'q':
        confirm = confirmation('change')
        if confirm == 'y':
            replace_record_line(file_name, record_id, '')

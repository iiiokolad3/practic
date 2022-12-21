def get_name():
    name = input("Введите имя: ")
    name = name.split()
    name = ' '.join(name)
    name = name.title()
    return name

def get_number():
    number = input("Введите номер: ")
    number = number.replace(" ", "")
    number = number.replace("-", "")
    number = number.replace("(", "")
    number = number.replace(")", "")
    if number[0] == '+' and number[1] == '7' and len(number) == 12:
        for i in range(1, len(number) - 1):
            c = number[i]
            if c.isdigit() == 0:
                print("Номер введен не верно")
                return get_number()
    elif number.isdigit() == 0:
        print("Номер введен не верно")
    elif number[0] == '8' and len(number) == 11:
        number = number.replace("8", "+7", 1)
    elif number[0] == '7' and len(number) == 11:
        number = number.replace("7", "+7", 1)
    elif len(number) == 10:
        number = "+7" + number
    else:
        print("Номер введен не верно")
        return get_number()
    return number

def get_add():
    d[get_name()]: num = get_number()
    return 'Контакт добавлен'

def get_spisok():
    for fio, num in d.items():
        print(fio, num)

def get_change():
    f = get_name()
    if f in d:
        d[f] = get_number()
        return "Контакт успешно изменен"
    else:
        return "Такого контакта нет"

def get_del():
    de = get_name()
    if de in d:
        del d['f']
        return 'Контакт удален'
    else:
        return 'Такого контакта нет'

d = {}

while True:
    print('1. Добавить контакт', '2. Удалить контакт', '3. Просмотреть телефонную книгу', '4. Изменить номер телефона (по имени)', '5. Выйти', sep='\n')
    param = input('Выберите функцию: ')

    if param == '1':
        print(get_add())
    if param == '2':
        print(get_del())
    if param == '3':
        get_spisok()
    if param == '4':
        print(get_change())
    if param == '5':
        print('Спасибо за использование')
        break
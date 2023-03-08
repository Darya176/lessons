"""
Напишите список функций по требованию. Пользователь вводит имя.
Если имя заканчивается на А,Я,Г,М, то программа добавляет к имени "Гений".
Если на О,Ь,Л,Н. То добавляется "Сверхразум". Если ни на одну из этих букв то добавляется "Просто" перед именем.
"""
func = {1: lambda name: 'Гений ' + name, 2: lambda name: 'Сверхразум ' + name, 3: lambda name: 'Просто ' + name}
while True:
    name = input('Имя или off: ')
    gen = ['а', 'я', 'г', 'м']
    sverh = ['о', 'л', 'ь', 'н']
    if name == 'off':
        break
    else:
        if name[-1] in gen:
            print(func[1](name))
        elif name[-1] in sverh:
            print(func[2](name))
        else:
            print(func[3](name))
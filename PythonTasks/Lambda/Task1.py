"""
Напишите программу которая будет спрашивать пользователя ввод имени пока пользователь не введет off.
Программа должна используя lambda-функцию добавлять к каждому имени надпись "гений".
"""
a = lambda name: name + ' гений'
name = input('Имя или off: ')
if name == 'off':
    print('работа программы завершена')
else:
    print(a(name))
    while True:
        name = input('Имя или off: ')
        if name == 'off':
            break
        else:
            print(a(name))

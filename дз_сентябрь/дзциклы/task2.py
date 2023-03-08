start = input('Для старта игры введите "game": ')
amount = 3
while amount>0 and start == 'game':
    string = input('Введите число: ')
    if string == '5':
        print('Вы выиграли')
        break
    elif start == 'off':
        print('Игра завершена')
        break
    else:
        print('неверно')
        amount -=1


time = int(input('Введите время: '))
cost = int(input('Введите сумму: '))
if time<8 or time>22:
    print('Магазин закрыт')
else:
    if time>=10 and time<=12:
        print(cost/2)
    elif time>=20 and time<=22:
        print(cost/4)
    else:
        print(cost)

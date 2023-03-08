
while True:
    amount = int(input('Введите стоимость: '))

    if amount !=0:
        string = int(input('Введите процент скидки: '))
        i = amount - amount/100*string
        print(i)
    else:
        break
category = input('Введите категорию товара: ')
if category != 'Продукты':
    print('Загляните в товары для дома!')
else:
    cost = int(input('Введите цену: '))
    if cost<100:
        print('Попробуйте нашу выпечку!')
    elif cost>=100 and cost<500:
        print('Как насчет орехов в шоколаде?')
    else:
        print('Попробуйте экзотические фрукты!')

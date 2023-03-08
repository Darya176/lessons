cost1 = int(input('цена товара 1: '))
cost2 = int(input('цена товара 2: '))
cost3 = int(input('цена товара 3: '))
a = cost1+cost2+cost3
if cost1<cost2 and cost2<cost3:
    print("К оплате: ", a/2)
elif cost1>cost2 and cost2>cost3:
    print('Акция!: ', a/3)
else:
    print('К оплате:', a)
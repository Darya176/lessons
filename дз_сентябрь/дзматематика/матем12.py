a = float(input('Ширина поверхности, м: '))
b = float(input('Длина поверхности, м: '))
c = float(input('Расход краски, кв.м./л.: '))
d = float(input('Объем банки в литрах: '))
e = float(input('Процент запаса: '))
base_area = str(a*b)
if base_area[5] == '5' or base_area[5] == '6' or base_area[5]=='7' or base_area[5]=='8' or base_area[5]=='9':
    print(float(base_area[0:5:]) + 0.01)
else:
    print(base_area[0:5:])

liters = float(base_area)/c
f = float(liters*e/100)
summ = str(liters + f)

if summ[5]=='5' or summ[5]=='6' or summ[5]=='7' or summ[5]=='8' or summ[5]=='9':
    amount = float(summ[0:5:]) + 0.01
    print(amount)
else:
    amount = float(summ[0:5:])
    print(amount)
banks = str(float(summ)/d + 1)
print(banks[0:1:])
unused = str(int(banks[0:1:])*d - amount)
if unused[4]== '5' or unused[4] == '6' or unused[4] == '7' or unused[4] == '8' or unused[4] == '9':
    x = str(float(unused) + 0.01)
    print(x[0:4:])
else:
    print(unused[0:4:])


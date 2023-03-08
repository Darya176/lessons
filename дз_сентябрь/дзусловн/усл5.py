number = input('Введите число: ')
b = number[ : :-1]
if b[0] == 1 or b[0] ==3 or b[0] == 5 or b[0] == 7 or b[0] == 9:
    print('Число не делится на 6.')
else:
    a = int(len(number)) -1
    c = int(sum(range(int(number[0]), int(number[a])))) + int(b[0])
    if c%3 == 0:
        print('Число делится на 6')
    else:
        print('Число не делится на 6')





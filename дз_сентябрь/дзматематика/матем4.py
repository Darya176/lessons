a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
print(a+b+c)
if a<c and a<b:
    print(a)
elif c<a and c<b:
    print(c)
else:
    print(b)
if a>c and a>b:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)


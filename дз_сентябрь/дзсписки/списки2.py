marks = input('Оценки: ').split(', ')
a = len(marks)
list = []
b = marks.count('3')
list.append(b)
c = marks.count('4')
list.append(c)
d = marks.count('5')
list.append(d)
print('Список оценок: ', marks)
print('Список кол-ва оценок: ', list)

print((b+c+d)/a*100)
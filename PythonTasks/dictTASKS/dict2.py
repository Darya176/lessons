"""
Дана строка чисел от 0 до 9 необходимо создать словарь где в качестве ключа будет цифра,
а в качестве значения количество этих цифр в строке
"""

numbers = "0139412831055230677798"
dictionary = dict()
for i in range(0, 10):
    dictionary[i] = numbers.count(str(i))
print(dictionary)

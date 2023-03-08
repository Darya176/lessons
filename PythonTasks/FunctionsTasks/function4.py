"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""

def print_IMT(weight, height):
    index = weight / (height*height)
    return index



def print_obr():
    IMT = print_IMT(weight, height)
    if IMT <18.5:
        print('Недостаточный вес')
    elif IMT >= 18.5 and IMT <= 25:
        print('ИМТ в норме')
    else:
        print('Избыточный вес')
    return print_obr

weight = float(input('Вес, кг: '))
height = float(input('Рост, м: '))
print_obr()
"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""

def print_function(*args):
    for i in args:
        if i != "None":
            print(i)
        else:
            print('нет значения')

print_function("Tom", "None", "Bob")
"""
Напишите скрипт который выводит надпись "Привет мир" если не было передано никаких аргументов.
Если 1 из аргументов "--name" то следующий аргумент должен быть имя. В таком случае выведите надпись "Привет {Имя}"
Пример ввода: python file.py kakoitoArgument --name Oleg(Скрипт должен напечатать привет Oleg)
"""
import sys
import os

if len(sys.argv) == 1:
    print('Привет мир')
elif len(sys.argv) == 3 and sys.argv[1] == '--name':
    name = sys.argv[2]
    print('Привет', name)
else:
    script_name = os.path.basename(sys.argv[0])
    print(f'Usage: {script_name} [--name <name>]')
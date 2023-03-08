"""
Создайте программу создающую папку target внутри которой еще 10 папок имена которых цифры от 1 до 10
"""
import os

if not os.path.exists('target'):
    os.mkdir('target')

for i in range(1, 11):
    folder_name = str(i)
    folder_path = os.path.join('target', folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
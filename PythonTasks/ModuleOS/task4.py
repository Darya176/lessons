""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""
import os

if not os.path.exists('task4'):
    os.mkdir('task4')


file_path = os.path.join('task4', 'answer.txt')
with open(file_path, 'w+') as f:
    f.write('я выполнил задание')
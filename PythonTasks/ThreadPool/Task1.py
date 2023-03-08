"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off для завершения,добавьте фамилию в очередь.
Во второй функции выводится сообщение что студент из очереди отчислен с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках.
"""
import queue
import concurrent.futures
from time import *

student_queue = queue.Queue()

def input_surname():
    while True:
        surname = input()
        if surname == "off":
            break
        student_queue.put(surname)

def student_expulsion():
    while True:
        if not student_queue.empty():
            surname = student_queue.get()
            print(surname, "отчислен")
        else:
            break


student_queue.put("фамилия")

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    future1 = executor.submit(input_surname)
    future2 = executor.submit(student_expulsion)

    concurrent.futures.wait([future1, future2])

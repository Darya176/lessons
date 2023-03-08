"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""
from time import sleep
from threading import Thread

flag = False


def detonation():
    global flag
    while True:
        sleep(3)
        if not flag:
            print("\nВводите быстрее: ")


th = Thread(target=detonation, daemon=True)
th.start()

code = input("Введите код бомбы: \n")

if "123" == code:
    print("Бомба разминирована")
else:
    print("Вы взорвались")


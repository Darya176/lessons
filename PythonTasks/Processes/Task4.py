"""
Запустите фоновый процесс который следит за сроком подписки пользователя( для примера 10 секунд) если время подписки вышло выведите надпись "Ваша подписка закончилась."
и завершите работу программы. В основной программе сыграйте с пользователем в игру "угадай число".
"""
import multiprocessing
import random
import time


def subscription_timer(subscription_time):
    time.sleep(subscription_time)
    print("Срок подписки истек")
    exit()


def guess_the_number():
    print("Угадай число!")
    secret_number = random.randint(1, 10)
    attempts = 0
    while True:
        number = int(input("Введите любое число от 1 до 10: "))
        attempts += 1
        if number < secret_number:
            print("Число меньше загаданного")
        elif number > secret_number:
            print("Число больше загаданного")
        else:
            print(f"Вы угадали число использовав {attempts} попыток")
            break


if __name__ == '__main__':
    subscription_time = int(input("Срок подписки пользователя: "))

    subscription_process = multiprocessing.Process(target=subscription_timer, args=(subscription_time,))
    subscription_process.start()

    guess_the_number()

    subscription_process.join()
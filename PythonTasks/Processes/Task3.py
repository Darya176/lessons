"""
Напишите функцию которая через канал обмена возвращает количество валюты которую можно приобрести на n сумму денег при курсе 1 к 75.
Запустите функцию в отдельном процессе и отправьте в нее данные задержкой в 0.5 секунды передайте ей разное количество доступных денег.
Выводите количество валюты на экран по мере обработки данных.
"""
import multiprocessing


def currency(money, rate, conn):
    currency = money * rate
    conn.send(currency)
    conn.close()


if __name__ == '__main__':
    rate = 75

    conn1, conn2 = multiprocessing.Pipe()
    p = multiprocessing.Process(target=currency, args=(100, rate, conn2))
    p.start()

    while True:
        if conn1.poll():
            currency = conn1.recv()
            print(f'{currency} валюты можно купить за 100 денег')
            break

    p.join()
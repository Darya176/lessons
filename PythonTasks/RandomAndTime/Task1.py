"""
В быстрых шахматах на принятие решений для всех ходов игроку даётся 30 минут. Программа должна:
Предлагать ввод хода (например, E2–E4) и считать потраченное время.
После получения хода печатать оставшееся время в минутах.
Если 30 минут закончились или игрок вводит «off» — завершать работу.
Оформить в виде функции.
"""

from time import time
def chess(*args):
    stopwatch = input('ход или off: ')
    start = time()
    while stopwatch != 0:
        if stopwatch != 'off':
            end = time()
            total = end - start
            left = (1800-total)/60
            print('Оставшееся время: ', round(left, 2) )
            if total >= 1800:
                print('Время вышло')
                break
            else:
                stopwatch = input('ход или off: ')
        else:
            print('игра окончена')
            break
chess()



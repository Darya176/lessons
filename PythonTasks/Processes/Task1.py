"""
Напишите 2 функции, одна считает сумму четных чисел, вторая нечетных
Запустите функции в разных процессах со значениями от 1 до 1000000
"""
import multiprocessing

def even_numbers(start, end):
    sum = 0
    for i in range(start, end):
        if i % 2 == 0:
            sum += i
    return sum

def odd_numbers(start, end):
    sum = 0
    for i in range(start, end):
        if i % 2 != 0:
            sum += i
    return sum

if __name__ == '__main__':
    start, end = 1, 100000
    with multiprocessing.Pool(processes=2) as pool:
        sum_even = pool.apply_async(even_numbers, args=(start, end))
        sum_odd = pool.apply_async(odd_numbers, args=(start, end))
        print(f"Sum of even numbers from {start} to {end}: {sum_even.get()}")
        print(f"Sum of odd numbers from {start} to {end}: {sum_odd.get()}")
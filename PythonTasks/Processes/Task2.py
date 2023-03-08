"""
Напишите 2 функции
Первая должна принимать ширину, длинну и высоты комнаты и записывать в файл площадь комнаты из 4 стен.
Вторая должна записать в тот же файл расход краски исходя из соотношения 5л/кв.м.
"""
import multiprocessing

def room_area(width, length, height, file):
    area = 2 * height * (width + length)
    with open(file, 'a') as f:
        f.write(f"площащь комнаты: {area} sq.m\n")

def paint_consumption(width, length, height, file):
    area = 2 * height * (width + length)
    consumption = area / 5
    with open(file, 'a') as f:
        f.write(f"Paint consumption: {consumption} L\n")

if __name__ == '__main__':
    width, length, height = 1, 3, 2
    file = "area.txt"
    with multiprocessing.Pool(processes=2) as pool:
        pool.apply_async(room_area, args=(width, length, height, file))
        pool.apply_async(paint_consumption, args=(width, length, height, file))
        pool.close()
        pool.join()
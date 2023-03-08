"""
Создайте функцию которая принимает путь до файла из папки files и меняет в нем "ids" на "id".
Запустите функцию для каждого файла в отдельном потоке.
Измерьте время выполнения программы.
"""
import os
import threading
import time

def rename_ids(file_name):
    path = os.path.join("files", file_name)

    with open(path, "w+") as file:
        text = file.read()
        text = text.replace("ids", "id")
        file.seek(0)
        file.write(text)
        file.truncate()

files = os.listdir("files")

start_time = time.time()
threads = []
for file_name in files:
    thread = threading.Thread(target=rename_ids, args=(file_name,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print('время выполнения:', end_time - start_time)
"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""
with open('file.1.txt', 'r') as f:
    text1 = f.read()
with open('file2.1.txt', 'w+') as fl:
    fl.write('но у меня не получается')
    fl.seek(0)
    text2 = fl.read()
with open('file2.2.txt', 'w+') as f2:

    f2.write(text1)
    f2.write(', ')
    f2.write(text2)
    f2.seek(0)
    print(f2.read())



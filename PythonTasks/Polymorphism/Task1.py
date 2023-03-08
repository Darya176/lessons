"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""

class Man:

    def sound(self):
        print('имитирует кряканье')

    def clothes(self):
        print('человек в одежде')


class Duck:

    def sound(self):
        print('кря')

    def clothes(self):
        print('утка в одежде')



man1 = Man()
duck1 = Duck()
list = [man1, duck1]
for i in list:
    i.sound()
    i.clothes()



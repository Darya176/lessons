"""
Создайте класс Person у которого будут свойства name и age.
Добавьте метод экземпляра который выводит информацию о человеке.
Создайте метод класса который генерирует новый объект класса
который ставить возраст человека: сегодняшний год - год который передают в метод.
(подсказка: тут можно использовать метод today().year класса date из модуля datetime)
Создайте статический метод который проверяет является ли совершеннолетним человек возраст которого передается в метод.
"""
from datetime import *
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def print_info(self):
        print(self.name)

    @classmethod
    def classmethod(cls, birth_year):
        age = date.today().year - birth_year
        return age


    @staticmethod
    def staticmethod(birth_year):
        age = date.today().year - birth_year
        if age < 18:
            return 'Несовершеннолетний'
        else:
            return 'Совершеннолетний'

man = Person('name', 2005)
man.print_info()
print(man.classmethod(2005))
print(man.staticmethod(2005))


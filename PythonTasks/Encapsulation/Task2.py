"""
В классе Hero из предыдущего занятия добавьте приватное свойство rank.
Создайте геттер, сеттер и делиттер чтобы можно было получить звание героя, установить звание "Победитель арены"
в случае победы героя в битве и удалить ранк в случае поражения.
"""

class Hero:
    def __init__(self, name, health, armor, power, weapon, rank):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.__rank = rank

    def getrank(self):
        return self.__rank

    def setrank(self, newrank):
        self.__rank = newrank

    def delrank(self):
        del self.__rank

    def strike(self, enemy):
        print("Удар -> " + self.name + ' атакует ' + enemy.name + ' с силой ' + str(self.power) + ', используя ' + self.weapon)
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print(enemy.name + ' покачнулся, класс брони упал до ' + str(enemy.armor) + ', а уровень здоровья упал до ' + str(enemy.health))

    def battle(self, enemy):
        while self.health >= 0 and enemy.health >= 0:
            print(self.strike(enemy))
            if enemy.health < 0:
                print(enemy.name + ' говорит: "Ты меня победил"')
                self.setrank('Победитель арены')
                enemy.delrank()
                break
            print(enemy.strike(self))
            if self.health < 0:
                print(self.name + ' говорит: "Ты меня победил"')
                enemy.setrank('Победитель арены')
                self.delrank()
                break



knight = Hero('Ричард', 50, 25, 20, 'меч', '0')
rascal = Hero('Хелен', 20, 5, 5, 'лук', '0')
knight.battle(rascal)
try:
    print(knight.getrank())
    print(rascal.getrank())
except:
    print('ранг удален')

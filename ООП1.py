class Hero():
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print('Поприветствуйте героя:', self.name)
        print('Уровень здоровья:', self.health)
        print('Броня:', self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon)

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
                break
            print(enemy.strike(self))
            if self.health < 0:
                print(self.name + ' говорит: "Ты меня победил"')
                break

knight = Hero('Ричард', 50, 25, 20, 'меч')
knight.print_info()
rascal = Hero('Хелен', 20, 5, 5, 'лук')
rascal.print_info()
knight.battle(rascal)
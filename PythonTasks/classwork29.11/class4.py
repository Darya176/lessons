class Bus():
    def __init__(self, speed, capacity, max_speed, empty_seats):
        self.speed = speed
        self.capacity = capacity
        self.max_speed = max_speed
        self.empty_seats = empty_seats

    def Posadka(self, amount):
        if self.empty_seats >= amount:
            self.empty_seats -= amount
            print('Посадили:', amount)
        else:
            print('Посадили:', self.empty_seats)
            self.empty_seats = 0

    def Razognatsya(self, speed):
            if speed + self.speed < self.max_speed:
                print('Разогнались до', self.speed + speed)
                self.speed += speed

            else:
                print('Едем в село с мах. скоростью - ', self.max_speed)
                self.speed = self.max_speed

bus = Bus(40, 80, 200, 40)
bus.Posadka(5)
bus.Posadka(65)
bus.Razognatsya(190)

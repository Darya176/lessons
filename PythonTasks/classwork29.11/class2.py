class Rectangle():
    def __init__(self, dlina, shirina):
        self.dlina = dlina
        self.shirina = shirina

    def info(self):
        print('Дан прямоугольник с длиной ', self.dlina, 'и шириной', self.shirina)

    def perimetr(self):
        return 2*(self.dlina + self.shirina)

    def square(self):
        return self.dlina*self.shirina


rect = Rectangle(4,2)
rect.info()
print(rect.perimetr())
print(rect.square())
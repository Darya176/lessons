"""
Класс Vector3D
Экземляр класса задается тройкой координат в трехмерном пространстве (x,y,z).
Обязательно должны быть реализованы методы:
– приведение вектора к строке с выводом кооржинат (метод __str __),
– сложение векторов оператором `+` (метод __add__),
– вычитание векторов оператором `-` (метод __sub__),
– скалярное произведение оператором `*` (метод __mul__),
"""
class Vector3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def __str__(self):
        return '({}; {}; {})'.format(self.x, self.y, self.z)

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return (self.x * other.x, self.y * other.y, self.z * other.z)

v1 = Vector3D(11, 12, 3)
v2 = Vector3D(1, 2, 3)
print(v1.__str__())
print(v2.__str__())
print(v2.__add__(v1))
print(v2.__sub__(v1))
print(v2.__mul__(v1))
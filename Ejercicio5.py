import math
class rectangulo():
    def __init__(self, a, b):
        self.b = b
        self.a = a
    def calcular_area(self):
        return self.b * self.a
class circulo():
    def __init__(self,r):
        self.r = r
    def calcular_area(self):
        return math.pi * self.r ** 2
           
c = circulo(5)
r = rectangulo(4,6)
print(r.calcular_area())
print(c.calcular_area())
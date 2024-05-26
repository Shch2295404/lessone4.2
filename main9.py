# C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main9.py
# Этот фрагмент кода определяет иерархию классов для различных фигур.
# Базовым классом является класс Shape, который имеет метод area(), возвращающий 0.
# Классы Circle, Rectangle, Square, Trapezoidal и Ellipse наследуют от класса Shape
# и переопределяют метод area() для вычисления площади каждой конкретной фигуры.
# Код также включает функцию print_area(), которая принимает объект фигуры в качестве аргумента
# и печатает площадь этой фигуры. Наконец, код создает экземпляры каждого класса фигур
# и вызывает функцию print_area(), чтобы вывести площадь каждой фигуры.
class Shape():
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


class Trapezoidal(Shape):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def area(self):
        return (self.length + self.width)/2 * self.height


class Ellipse(Shape):
    def __init__(self, radius_1, radius_2):
        self.radius_1 = radius_1
        self.radius_2 = radius_2

    def area(self):
        return 3.14 * self.radius_1 * self.radius_2


def print_area(shape):
    print(f"Площадь фигуры: {shape.area()}")


c = Circle(3)
print_area(c)
r = Rectangle(4, 5)
print_area(r)
s = Square(4)
print_area(s)
t = Trapezoidal(4, 5, 7)
print_area(t)
e = Ellipse(4, 3)
print_area(e)
print(f"Площадь круга: {c.area()}")
print(f"Площадь прямоугольника: {r.area()}")
print(f"Площадь квадрата: {s.area()}")
print(f"Площадь трапеции: {t.area()}")
print(f"Площадь эллипса: {e.area()}")

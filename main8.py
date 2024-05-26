# C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main.py
# В этом примере код создает классы Dog, Cat и Cow, которые представляют животные.
# Затем код создает список объектов Animal, каждый из которых представляет отдельное животное,
# и выполняет итерации по списку, вызывая метод make_sound для каждого объекта.
# В результате программа напечатает «Гав!», «Мяу» и «Мууу» соответственно.
class Animal():
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Гав!")


class Cat(Animal):
    def make_sound(self):
        print("Мяу")


class Cow(Animal):
    def make_sound(self):
        print("Мууу")


animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.make_sound()
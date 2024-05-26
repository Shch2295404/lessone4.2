class Animal():
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Гав!")

class Cat(Animal):
    def make_sound(self):
        print("Мяу!")

class Cow(Animal):
    def make_sound(self):
        print("Муу!")


 animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.make_sound()
# C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main7.py
# Этот код определяет два класса, Dog и Cat, у которых есть метод speak,
# возвращающий строку. Функция animal_speak принимает в качестве аргумента
# объект класса Dog или Cat и вызывает на нем метод speak.
#
# Код создает экземпляры Dog и Cat, а затем вызывает animal_speak на каждом из них,
# чтобы распечатать соответствующие звуки животных.
class Dog:
    def speak(self):
        return "Гав!"

class Cat:
    def speak(self):
        return "Мяу!"

def animal_speak(animal):
    return animal.speak()


dog = Dog()
cat = Cat()

print(animal_speak(dog))
print(animal_speak(cat))
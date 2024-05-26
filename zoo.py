import pickle


# Базовый класс Animal
class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def make_sound(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


# Подклассы Bird, Mammal, Reptile
class Bird(Animal):
    def __init__(self, name, age, weight, needs_water):
        super().__init__(name, age, weight)
        self.needs_water = needs_water

    def make_sound(self):
        print(f"{self.name} says: Chirp Chirp!")


class Mammal(Animal):
    def __init__(self, name, age, weight, needs_water):
        super().__init__(name, age, weight)
        self.needs_water = needs_water

    def make_sound(self):
        print(f"{self.name} says: Roar!")


class Reptile(Animal):
    def __init__(self, name, age, weight, needs_water):
        super().__init__(name, age, weight)
        self.needs_water = needs_water

    def make_sound(self):
        print(f"{self.name} says: Hiss!")


# Полиморфизм: функция, принимающая список животных и вызывающая метод make_sound
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Классы сотрудников зоопарка
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")
        animal.eat()


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")


# Класс Zoo, использующий композицию для хранения животных и сотрудников
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} to the zoo.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Added {staff_member.name} to the zoo staff.")

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Zoo saved to {filename}.")

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
        print(f"Zoo loaded from {filename}.")
        return zoo


# Пример использования
if __name__ == "__main__":
    # Создание животных
    parrot = Bird("Parrot", 2, 0.5, True)
    lion = Mammal("Lion", 5, 190, False)
    snake = Reptile("Snake", 3, 5, True)

    # Создание сотрудников
    keeper = ZooKeeper("Alice")
    vet = Veterinarian("Bob")

    # Создание зоопарка и добавление животных и сотрудников
    zoo = Zoo()
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Демонстрация полиморфизма
    animal_sound(zoo.animals)

    # Использование сотрудников
    keeper.feed_animal(lion)
    vet.heal_animal(snake)

    # Сохранение и загрузка зоопарка
    zoo.save_to_file("zoo.pkl")
    loaded_zoo = Zoo.load_from_file("zoo.pkl")
    animal_sound(loaded_zoo.animals)

    # Сохранение и загрузка зоопарка в формате JSON
    zoo.save_to_file("zoo.json")
    loaded_zoo = Zoo.load_from_file("zoo.json")
    animal_sound(loaded_zoo.animals)

    zoo.save_to_file("zoo.txt")
    loaded_zoo = Zoo.load_from_file("zoo.txt")
    animal_sound(loaded_zoo.animals)

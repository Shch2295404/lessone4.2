import pickle


# Базовый класс Animal
class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассах")

    def eat(self):
        print(f"{self.name} ест.")

    def sleep(self):
        print(f"{self.name} спит.")

    def drink(self):
        print(f"{self.name} пьет.")

    def gogo(self):
        print(f"{self.name} бегает.")

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Вес: {self.weight}")


# Подклассы Bird, Mammal, Reptile
class Bird(Animal):
    def __init__(self, name, age, weight, needs_water):
        super().__init__(name, age, weight)
        self.needs_water = needs_water

    def make_sound(self):
        print(f"{self.name} кричит: Чирк-чирк!")


class Mammal(Animal):
    def __init__(self, name, age, weight, needs_water):
        super().__init__(name, age, weight)
        self.needs_water = needs_water

    def make_sound(self):
        print(f"{self.name} рычит: Ррррр!")


class Reptile(Animal):
    def __init__(self, name, age, weight, needs_water):
        super().__init__(name, age, weight)
        self.needs_water = needs_water

    def make_sound(self):
        print(f"{self.name} шипит: Шшшш!")


# Полиморфизм: функция, принимающая список животных и вызывающая метод make_sound
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Классы сотрудников зоопарка
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")
        animal.eat()


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")
        animal.sleep()

# Класс Zoo, использующий композицию для хранения животных и сотрудников
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено {animal.name} в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Пополнил {staff_member.name} штат сотрудников зоопарка.")

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Зоопарк сохранен в {filename}.")

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
        print(f"Зоопарк загружен из {filename}.")
        return zoo


# Пример использования
if __name__ == "__main__":
    # Создание животных
    parrot = Bird("Попугай", 2, 0.5, True)
    tiger = Mammal("Тигр", 5, 190, False)
    snake = Reptile("Удав", 3, 5, True)

    # Создание сотрудников
    keeper = ZooKeeper("Алёна")
    vet = Veterinarian("Иван")

    # Создание зоопарка и добавление животных и сотрудников
    zoo = Zoo()
    zoo.add_animal(parrot)
    zoo.add_animal(tiger)
    zoo.add_animal(snake)
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Демонстрация полиморфизма
    animal_sound(zoo.animals)

    # Использование сотрудников
    keeper.feed_animal(tiger)
    tiger.info()
    vet.heal_animal(snake)
    snake.info()
    parrot.gogo()
    parrot.info()

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

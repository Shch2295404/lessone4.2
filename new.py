# C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/new.py
# Этот код на языке Python определяет два класса: Car и ElectricCar.
# Класс Car имеет три атрибута: public_make, _protected_model и __private_year.
# Атрибут public_make доступен извне класса, а _protected_model и __private_year являются защищенным
#  и приватным атрибутами соответственно, то есть доступ к ним возможен только изнутри класса или его подклассов.
# Класс Car также имеет три метода: public_method(), protected_method() и private_method().
# Метод public_method() возвращает строку, содержащую марку и модель автомобиля,
#  а методы protected_method() и private_method() возвращают защищенную и частную модель соответственно.
# Класс ElectricCar является подклассом Car и добавляет дополнительный атрибут battery_size.
# Он также переопределяет метод get_details(), чтобы включить размер батареи в подробную информацию об электромобиле.
# Код создает экземпляр класса Car под названием my_car и печатает результат вызова метода public_method().
# Затем создается экземпляр класса ElectricCar с именем electric_car и выводится результат вызова метода get_details().
class Car(object):
    def __init__(self, make, model, year):
        self.public_make = make
        self._protected_model = model
        self.__private_year = year

    def public_method(self):
        return f"Car make: " + self.public_make + ", model: " + self._protected_model

    def protected_method(self):
        return self._protected_model

    def private_method(self):
        return self.__private_year


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size=75):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def get_details(self):
        details = f"Electric car " + self.public_make + ", model " + self._protected_model + ", year: " + str(self.private_method()) + ", battery size: " + str(self.battery_size)
        return details


my_car = Car("Toyota", "Camry", 2022)
print(my_car.public_method())
electric_car = ElectricCar("BMW", "Sport 003", 2023, 105)
print(electric_car.get_details())

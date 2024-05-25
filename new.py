class Car(object):
    def __init__(self, make, model, year):
        self.public_make = "Toyota"
        self._protected_model = "Camry"
        self.__private_year = 2022

    def public_method(self):
        return self.public_make

    def protected_method(self):
        return self._protected_model

    def private_method(self):
        return self.__private_year


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def public_method(self):
        return "Electric " + super().public_method()

    def protected_method(self):
        return "Electric " + super().protected_method()

    def private_method(self) -> str:
        return "Electric " + str(super().private_method())


car = Car("Toyota", "Camry", 2022)

print(car.public_method())
print(car.protected_method())
print(car.private_method())

electric_car = ElectricCar("Toyota", "ACDC", 2023)

print(electric_car.public_method())
print(electric_car.protected_method())
print(electric_car.private_method())

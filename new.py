class Car(object):
    def __init__(self, make, model, year):
        self.public_make = "Toyota"
        self._protected_model = "Camry"
        self.__private_year = 2022

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

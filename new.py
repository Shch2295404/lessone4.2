class Car(object):
    def __init__(self, make, model, year):
        self.public_make = "Toyota"
        self._protected_model = "Camry"
        self.__private_year = 2022

    def public_method(self):
        return print(self.public_make)

    def protected_method(self):
        return print(self._protected_model)

    def private_method(self):
        return print(self.__private_year)


car = Car("Toyota", "Camry", 2022)

print(car.public_method())
print(car.protected_method())
print(car.private_method())

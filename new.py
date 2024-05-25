class Car(object):
    def __init__(self, make, model, year):
        self.public_make = "Toyota"
        self._protected_model = "Camry"
        self.__private_year = 2022

    def public_metod(self):
        return print(self.public_make)

    def protected_metod(self):
        return print(self._protected_model)

    def private_metod(self):
        return print(self.__private_year)


car = Car("Toyota", "Camry", 2022)

print(car.public_metod())
print(car.protected_metod())
print(car.private_metod())

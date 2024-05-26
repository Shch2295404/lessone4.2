# C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main5.py
# Этот код на языке Python определяет два класса: Engine и Car.
# Класс Engine имеет два метода: start() и stop().
# Метод start() выводит на консоль сообщение 'Starting the engine...',
# а метод stop() выводит сообщение 'Stopping the engine...'.
# Класс Car имеет метод __init__, который инициализирует новый экземпляр Car с экземпляром Engine.
#  Метод start() класса Car вызывает метод start() экземпляра Engine,
# а метод stop() класса Car вызывает метод stop() экземпляра Engine.
#  Затем код создает новый экземпляр Car с именем my_Car и вызывает его методы start() и stop().
# В результате в консоли будут выведены сообщения 'Starting the engine...' и 'Stopping the engine...'.
#  В итоге этот код демонстрирует объектно-ориентированное программирование (ООП) в Python,
# где автомобиль имеет двигатель и может запускать и останавливать его.
class Engine:
    def start(self):
        print('Starting the engine...')

    def stop(self):
        print('Stopping the engine...')


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()


my_Car = Car()
my_Car.start()
my_Car.stop()
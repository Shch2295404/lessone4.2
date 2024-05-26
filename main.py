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

class Test(object):
    def __init__(self):
        self.public = "public attribute"
        self._protected = "protected attribute"
        self.__private = "private attribute"

    def get_private(self):
        return self.__private

    def set_private(self, value):
        self.__private = value


test = Test()
print(test.public)
print(test.get_private())
test.set_private("new value")
print(test.get_private())

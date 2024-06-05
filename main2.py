# C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main2.py
# Этот код Python определяет класс Test, который имеет три атрибута: public, _protected и __private.
# Метод __init__ инициализирует эти атрибуты.
# У класса также есть два метода: get_private и set_private, которые позволяют получать
# и устанавливать значение атрибута __private.
# Код создает экземпляр класса Test с именем test и выводит значения атрибутов public и __private.
# Затем он устанавливает атрибут __private в новое значение и снова выводит его на печать.
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
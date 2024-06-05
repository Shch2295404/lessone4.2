# C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main3.py
# Этот код Python определяет класс Test, который имеет три атрибута: public, _protected и __private.
# Метод __init__ инициализирует эти атрибуты.
# У класса также есть два метода: get_private и set_private, которые позволяют получать
# и устанавливать значение атрибута __private.
# Код создает экземпляр класса Test с именем test и выводит значения атрибутов public и __private.
# Затем он устанавливает атрибут __private в новое значение и снова выводит его на печать.
#
# В Python существует механизм, называемый "name mangling" (искажение имен),
# который используется для управления доступом к атрибутам классов.
# Этот механизм автоматически изменяет имена атрибутов, начинающихся с двух подчеркиваний `__`,
# чтобы сделать их менее доступными для прямого доступа из внешнего кода.
# Это помогает избежать конфликтов имен в подклассах и делает атрибуты "приватными".


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
print(test.public)                  # Доступ к публичному атрибуту
print(test._protected)              # Доступ к защищенному атрибуту
print(test.get_private())           # Доступ к приватному атрибуту через метод
test.set_private("new value")       # Изменение приватного атрибута через метод
print(test.get_private())           # Доступ к измененному приватному атрибуту через метод

# Попытка прямого доступа к приватному атрибуту (с использованием name mangling)
try:
    print(test.__private)
except AttributeError as e:
    print(e)

# Доступ к приватному атрибуту с использованием name mangling
print(test._Test__private)

# Вывод будет следующим:
# public attribute
# protected attribute
# private attribute
# new value
# 'Test' object has no attribute '__private'
# new value

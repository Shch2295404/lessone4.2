# C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main4.py
# Этот код на языке Python определяет класс Test с четырьмя методами:
# # public_func(): Это публичный метод, который печатает «This is public function».
# _protected_func():
#  Это защищенный метод (условно обозначается префиксом с одним подчеркиванием),
#  который печатает «Это защищенная функция».
# __private_func(): Это приватный метод (условно обозначается двумя префиксами подчеркивания),
#  который выводит «Это приватная функция».
# test_private(): Этот метод вызывает приватный метод __private_func().
#  Затем класс инстанцируется как объект test, и вызываются публичный и приватный методы.
#   Защищенный метод не вызывается, потому что он предназначен для внутреннего использования
#   внутри класса и не предназначен для доступа извне.
#  Примечание: В Python нет строгих требований к приватным методам.
#  Они по-прежнему доступны и могут быть вызваны, но, как правило,
#  считается хорошей практикой избегать этого, поскольку это может привести к путанице и потенциальным ошибкам.
class Test(object):
    def public_func(self):
        print("This is public function")

    def _protected_func(self):
        print("This is protected function")

    def __private_func(self):
        print("This is private function")

    def test_private(self):
        self.__private_func()


test=Test()
test.public_func()
test.test_private()
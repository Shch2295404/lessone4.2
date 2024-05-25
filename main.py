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

# lessone4.2
# наследование и инкапсуляция

C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main0.py
Этот код определяет два класса: User и Admin.
Класс User представляет простого пользователя с идентификатором, именем и уровнем доступа.
Класс Admin является подклассом класса User и представляет пользователя-администратора.
Класс Admin имеет дополнительную функциональность для добавления, удаления и редактирования пользователей.
В блоке if __name__ == «__main__»: создается несколько экземпляров User и Admin.
Затем пользователи-администраторы добавляют, удаляют и редактируют пользователей.
Код также выводит данные о добавленных и отредактированных пользователях.
Метод add_user в классе Admin проверяет, является ли добавляемый пользователь экземпляром класса User
 и имеет ли он уровень доступа 'user'. Если да, то он добавляет пользователя в атрибут users_list пользователя admin.
Если нет, то возвращается сообщение об ошибке.
Метод remove_user класса Admin ищет пользователя с указанным ID в атрибуте users_list пользователя admin
 и удаляет его, и если находит. Если он не найден, возвращается сообщение о том, что пользователь не найден.

C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main1.py
Задача оптимизировать программу
 ```python

class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.users_list = []

    def get_access_level(self):
        return self.__access_level

    def add_user(self, user):
        if isinstance(user, User) and user.get_access_level() == 'user':
            self.users_list.append(user)
            return f"User {user.get_name()} added successfully."
        else:
            return "Failed to add user. Only 'user' level employees can be added."

    def remove_user(self, user_id):
        for user in self.users_list:
            if user.get_user_id() == user_id:
                self.users_list.remove(user)
                return f"User with ID {user_id} removed successfully."
        return f"User with ID {user_id} not found."

    def edit_user(self, user_id, new_name):
        for user in self.users_list:
            if user.get_user_id() == user_id:
                user.set_name(new_name)
                return f"User with ID {user_id} renamed to {new_name}."
        return f"User with ID {user_id} not found."


# Пример использования
if __name__ == "__main__":
    # Создаем администраторов
    admin1 = Admin(1, "Admin 001")
    admin2 = Admin(2, "Admin 002")
    admin3 = Admin(3, "Admin 003")

    # Создаем несколько обычных сотрудников
    user1 = User(101, "User 001")
    user2 = User(102, "User 002")
    user3 = User(103, "User 003")
    user4 = User(104, "User 004")
    user5 = User(105, "User 005")
    user6 = User(106, "User 006")
    user7 = User(107, "User 007")
    user8 = User(108, "User 008")
    user9 = User(109, "User 009")

    # Администратор 1 добавляет сотрудников
    print(admin1.add_user(user1))
    print(admin1.add_user(user2))
    print(admin1.add_user(user3))

    # Пытаемся добавить администратора как обычного сотрудника
    print(admin1.add_user(admin1))  # Должно вернуть ошибку

    # Администратор 1 удаляет сотрудника
    print(admin1.remove_user(102))

    # Администратор 1 редактирует сотрудника
    print(admin1.edit_user(103, "User 003 Renamed"))

    # Вывод списка сотрудников у администратора 1
    for user in admin1.users_list:
        print(f"User ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

    # Администратор 2 добавляет сотрудников
    print(admin2.add_user(user4))
    print(admin2.add_user(user5))
    print(admin2.add_user(user6))

    # Пытаемся добавить администратора как обычного сотрудника
    print(admin2.add_user(admin2))  # Должно вернуть ошибку

    # Администратор 2 удаляет сотрудника
    print(admin2.remove_user(105))

    # Администратор 2 редактирует сотрудника
    print(admin2.edit_user(106, "User 006 Renamed"))

    # Вывод списка сотрудников у администратора 2
    for user in admin2.users_list:
        print(f"User ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

    # Вывод списка сотрудников у администратора 3
    for user in admin3.users_list:
        print(f"User ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")
 ```

Результат:

1. Удалены дублирующиеся методы.
2. Упрощена логика поиска и удаления пользователей.
3. Использованы свойства (property) для доступа к приватным атрибутам.

```python
class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.users_list = []

    @property
    def access_level(self):
        return self.__access_level

    def add_user(self, user):
        if isinstance(user, User) and user.access_level == 'user':
            self.users_list.append(user)
            return f"User {user.name} added successfully."
        return "Не удалось добавить 'user'. Добавлять можно только сотрудников уровня «пользователь»."

    def remove_user(self, user_id):
        user = next((u for u in self.users_list if u.user_id == user_id), None)
        if user:
            self.users_list.remove(user)
            return f"Пользователь с идентификатором {user_id} успешно удален."
        return f"Пользователь с идентификатором {user_id} не найден."

    def edit_user(self, user_id, new_name):
        user = next((u for u in self.users_list if u.user_id == user_id), None)
        if user:
            user.name = new_name
            return f"Пользователь с идентификатором {user_id} переименован в {new_name}."
        return f"Пользователь с идентификатором {user_id} не найден."


# Пример использования
if __name__ == "__main__":
    # Создаем администраторов
    admin1 = Admin(1, "Admin 001")
    admin2 = Admin(2, "Admin 002")
    admin3 = Admin(3, "Admin 003")

    # Создаем несколько обычных сотрудников
    users = [
        User(101, "User 001"),
        User(102, "User 002"),
        User(103, "User 003"),
        User(104, "User 004"),
        User(105, "User 005"),
        User(106, "User 006"),
        User(107, "User 007"),
        User(108, "User 008"),
        User(109, "User 009"),
    ]

    # Администратор 1 добавляет сотрудников
    print(admin1.add_user(users[0]))
    print(admin1.add_user(users[1]))
    print(admin1.add_user(users[2]))

    # Пытаемся добавить администратора как обычного сотрудника
print(admin1.add_user(admin1))  # Должно вернуть ошибку

    # Администратор 1 удаляет сотрудника
    print(admin1.remove_user(102))

    # Администратор 1 редактирует сотрудника
    print(admin1.edit_user(103, "User 003 Renamed"))

    # Вывод списка сотрудников у администратора 1
    for user in admin1.users_list:
        print(f"User ID: {user.user_id}, Name: {user.name}, Access Level: {user.access_level}")

    # Администратор 2 добавляет сотрудников
    print(admin2.add_user(users[3]))
    print(admin2.add_user(users[4]))
    print(admin2.add_user(users[5]))

    # Пытаемся добавить администратора как обычного сотрудника
    print(admin2.add_user(admin2))  # Должно вернуть ошибку

    # Администратор 2 удаляет сотрудника
    print(admin2.remove_user(105))

    # Администратор 2 редактирует сотрудника
    print(admin2.edit_user(106, "User 006 Renamed"))

    # Вывод списка сотрудников у администратора 2
    for user in admin2.users_list:
        print(f"User ID: {user.user_id}, Name: {user.name}, Access Level: {user.access_level}")

    # Вывод списка сотрудников у администратора 3
    for user in admin3.users_list:
        print(f"User ID: {user.user_id}, Name: {user.name}, Access Level: {user.access_level}")
```

### Объяснение изменений:
1. **Использование свойств (property)**:
    - Упрощает доступ к приватным атрибутам класса.
    - Избавляет от необходимости явно писать методы `get_` и `set_`.
  
2. **Использование генераторов**:
    - В методах `remove_user` и `edit_user` используется генератор для поиска пользователя, 
что делает код более компактным и читаемым.
  
3. **Упрощение логики**:
    - Удалены дублирующиеся методы и улучшены проверки.

Эти изменения делают код более понятным, эффективным и легким для поддержки.


C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main2.py
В Python существует механизм, называемый "name mangling" (искажение имен), 
который используется для управления доступом к атрибутам классов. 
Этот механизм автоматически изменяет имена атрибутов, начинающихся с двух подчеркиваний `__`, 
чтобы сделать их менее доступными для прямого доступа из внешнего кода. 
Это помогает избежать конфликтов имен в подклассах и делает атрибуты "приватными".

Давайте посмотрим на ваш фрагмент кода и увидим, как работает name mangling:

```python
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
```

Вывод будет следующим:

```
public attribute
protected attribute
private attribute
new value
'Test' object has no attribute '__private'
new value
```

Объяснение:
1. Атрибут `public` доступен напрямую, так как он является публичным.
2. Атрибут `_protected` также доступен напрямую, так как он является защищенным и просто служит индикатором для разработчиков, что это внутренний атрибут.
3. Атрибут `__private` не доступен напрямую, так как он подвергается name mangling. Попытка доступа к нему через `test.__private` вызывает ошибку `AttributeError`.
4. Однако, мы можем получить доступ к приватному атрибуту `__private` через методы `get_private` и `set_private`.
5. Также, используя name mangling, мы можем получить доступ к приватному атрибуту через `test._Test__private`.

Name mangling автоматически изменяет имя атрибута `__private` на `_Test__private`, чтобы предотвратить его случайный доступ или конфликт имен в подклассах.


C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main4.py
Этот код на языке Python определяет класс Test с четырьмя методами:
 public_func(): Это публичный метод, который печатает «This is public function».
 _protected_func():
Это защищенный метод (условно обозначается префиксом с одним подчеркиванием),
  который печатает «Это защищенная функция».
 __private_func(): Это приватный метод (условно обозначается двумя префиксами подчеркивания),
  который выводит «Это приватная функция».
 test_private(): Этот метод вызывает приватный метод __private_func().
Затем класс инстанцируется как объект test, и вызываются публичный и приватный методы.
Защищенный метод не вызывается, потому что он предназначен для внутреннего использования
 внутри класса и не предназначен для доступа извне.
Примечание: В Python нет строгих требований к приватным методам.
Они по-прежнему доступны и могут быть вызваны, но, как правило,
 считается хорошей практикой избегать этого, поскольку это может привести к путанице и потенциальным ошибкам.

C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main5.py
Этот код на языке Python определяет два класса: Engine и Car.
Класс Engine имеет два метода: start() и stop().
Метод start() выводит на консоль сообщение 'Starting the engine...',
 а метод stop() выводит сообщение 'Stopping the engine...'.
Класс Car имеет метод __init__, который инициализирует новый экземпляр Car с экземпляром Engine.
Метод start() класса Car вызывает метод start() экземпляра Engine,
 а метод stop() класса Car вызывает метод stop() экземпляра Engine.
Затем код создает новый экземпляр Car с именем my_Car и вызывает его методы start() и stop().
В результате в консоли будут выведены сообщения 'Starting the engine...' и 'Stopping the engine...'.
В итоге этот код демонстрирует объектно-ориентированное программирование (ООП) в Python,
 где автомобиль имеет двигатель и может запускать и останавливать его.

C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main6.py
Этот код на языке Python определяет два класса: Teacher и School.#
Класс Teacher имеет метод teach(),
 который печатает «Преподаватель учит» (что в переводе на русский означает «Учитель учит»).
Класс School имеет метод __init__(),
 который принимает в качестве аргумента объект new_teacher и присваивает его атрибуту teacher.
У него также есть метод start_lesson(), который вызывает метод teach() объекта teacher.
Затем код создает объект my_teacher класса Teacher и объект my_school класса School,
 передавая my_teacher в качестве аргумента конструктору School.
Затем он печатает объекты my_teacher и my_school и вызывает метод start_lesson() для my_school,
 который, в свою очередь, вызывает метод teach() для my_teacher.

C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main7.py
Этот код определяет два класса, Dog и Cat, у которых есть метод speak,
 возвращающий строку. Функция animal_speak принимает в качестве аргумента
 объект класса Dog или Cat и вызывает на нем метод speak.
Код создает экземпляры Dog и Cat, а затем вызывает animal_speak на каждом из них,
 чтобы распечатать соответствующие звуки животных.

C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main8.py
В этом примере код создает классы Dog, Cat и Cow, которые представляют животные.
Затем код создает список объектов Animal, каждый из которых представляет отдельное животное,
 и выполняет итерации по списку, вызывая метод make_sound для каждого объекта.
В результате программа напечатает «Гав!», «Мяу» и «Мууу» соответственно.

C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main9.py
Этот фрагмент кода определяет иерархию классов для различных фигур.
 Базовым классом является класс Shape, который имеет метод area(), возвращающий 0.
Классы Circle, Rectangle, Square, Trapezoidal и Ellipse наследуют от класса Shape
 и переопределяют метод area() для вычисления площади каждой конкретной фигуры.
Код также включает функцию print_area(), которая принимает объект фигуры в качестве аргумента
 и печатает площадь этой фигуры. Наконец, код создает экземпляры каждого класса фигур
 и вызывает функцию print_area(), чтобы вывести площадь каждой фигуры.

C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/main10.py
В этом фрагменте кода определены два класса: Author и Book.
Класс Author имеет метод __init__, который принимает в качестве параметров имя и национальность
 и присваивает их переменным экземпляра self.name и self.nationality, соответственно.
Класс Book также имеет метод __init__, который принимает в качестве параметров title и author
 и присваивает их переменным экземпляра self.title и self.author, соответственно.
Класс Book также имеет метод get_info_book, который выводит название, имя и национальность книги.
В фрагменте кода создается экземпляр класса Author с именем 'George R. R. Martin'
 и национальностью 'American'. Затем создается экземпляр класса Book с названием 'Игра Престолов'
 и ранее созданным экземпляром Author в качестве автора.
На экземпляре Book вызывается метод get_info_book, который выводит название, имя и национальность книги.
Наконец, имя и национальность автора и название книги выводятся отдельно.

C:/Users/Щетинин Д Б/Documents/GitHub/lessone4.2/new.py
Этот код на языке Python определяет два класса: Car и ElectricCar.
Класс Car имеет три атрибута: public_make, _protected_model и __private_year. 
Атрибут public_make доступен извне класса, а _protected_model и __private_year являются защищенным 
 и приватным атрибутами соответственно, то есть доступ к ним возможен только изнутри класса или его подклассов.
Класс Car также имеет три метода: public_method(), protected_method() и private_method(). 
Метод public_method() возвращает строку, содержащую марку и модель автомобиля, 
 а методы protected_method() и private_method() возвращают защищенную и частную модель соответственно.
Класс ElectricCar является подклассом Car и добавляет дополнительный атрибут battery_size. 
Он также переопределяет метод get_details(), чтобы включить размер батареи в подробную информацию об электромобиле.
Код создает экземпляр класса Car под названием my_car и печатает результат вызова метода public_method(). 
Затем создается экземпляр класса ElectricCar с именем electric_car и выводится результат вызова метода get_details().

zoo.py
Этот фрагмент кода определяет симулятор зоопарка на Python. 
Он включает в себя классы для животных, смотрителей зоопарка и ветеринаров, 
 а также класс Zoo, который управляет животными и персоналом. 
Код демонстрирует полиморфизм, поскольку функция animal_sound может принимать список животных 
 и вызывать их метод make_sound. 
Зоопарк можно сохранять и загружать из файлов различных форматов, включая pickle, JSON и текст.


# Инструмент Mangling критерии использования по принципам объектно-ориентированного программирования языка Python

В объектно-ориентированном программировании на языке Python существует концепция манглинга (name mangling), 
 которая используется для создания "частных" атрибутов в классах. 
Манглинг имен — это механизм, который изменяет имена атрибутов, чтобы сделать их менее доступными из внешнего кода 
 и избежать конфликтов имен в подклассах. Это достигается путем добавления префикса `_ClassName` к имени атрибута.

Вот основные критерии и правила использования манглинга имен в Python:

1. **Двойное подчеркивание перед именем**:
   Если вы хотите сделать атрибут "частным" (то есть, недоступным напрямую из вне класса), 
    вы должны использовать двойное подчеркивание перед его именем:
   ```python
   class MyClass:
       def __init__(self):
           self.__private_attr = 42
   ```

2. **Изменение имени**:
   Python автоматически изменяет имя атрибута, добавляя к нему префикс `_ClassName`, 
    чтобы сделать его менее доступным:
   ```python
   obj = MyClass()
   print(obj.__dict__)  # {'_MyClass__private_attr': 42}
   ```

3. **Доступ к манглированным атрибутам**:
   Хотя манглинг имен делает атрибуты менее доступными, это не делает их полностью недоступными. 
   Вы все еще можете получить доступ к таким атрибутам, используя их измененные имена:
   ```python
   print(obj._MyClass__private_attr)  # 42
   ```

4. **Использование в наследовании**:
   Манглинг имен помогает избежать конфликтов имен в подклассах. 
   Например:
   ```python
   class Base:
       def __init__(self):
           self.__hidden = "Base"

   class Derived(Base):
       def __init__(self):
           super().__init__()
           self.__hidden = "Derived"

   obj = Derived()
   print(obj.__dict__)  # {'_Base__hidden': 'Base', '_Derived__hidden': 'Derived'}
   ```

5. **Не путать с одиночным подчеркиванием**:
   Одиночное подчеркивание (например, `_attr`) используется для обозначения "защищенных" атрибутов, 
    которые не должны использоваться вне класса и его подклассов, 
     но это всего лишь соглашение и не обеспечивает никакой реальной защиты:
   ```python
   class MyClass:
       def __init__(self):
           self._protected_attr = "Protected"
   ```

6. **Не использовать манглинг без необходимости**:
   Манглинг имен используется редко и только тогда, когда это действительно необходимо для предотвращения конфликтов имен 
    или для обеспечения скрытия реализации. 
   В большинстве случаев достаточно использовать одиночное подчеркивание.

Пример использования манглинга имен:

```python
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Приватный атрибут

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # 150
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'
print(account._BankAccount__balance)  # 150 (доступ через манглированное имя)
```
Следуя этим критериям, вы сможете эффективно использовать манглинг имен в Python 
 для управления доступом к атрибутам и предотвращения конфликтов имен.

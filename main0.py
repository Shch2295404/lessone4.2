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


# Наследуем от User
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
        return "Failed to add user. Only 'user' level employees can be added."

    def remove_user(self, user_id):
        user = next((u for u in self.users_list if u.user_id == user_id), None)
        if user:
            self.users_list.remove(user)
            return f"User with ID {user_id} removed successfully."
        return f"User with ID {user_id} not found."

    def edit_user(self, user_id, new_name):
        user = next((u for u in self.users_list if u.user_id == user_id), None)
        if user:
            user.name = new_name
            return f"User with ID {user_id} renamed to {new_name}."
        return f"User with ID {user_id} not found."


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

# Администратор 3 добавляет сотрудников
print(admin3.add_user(users[6]))
print(admin3.add_user(users[7]))
print(admin3.add_user(users[8]))

# Пытаемся добавить администратора как обычного сотрудника
print(admin3.add_user(admin3))  # Должно вернуть ошибку

# Администратор 3 удаляет сотрудника
print(admin3.remove_user(108))

# Администратор 3 редактирует сотрудника
print(admin3.edit_user(109, "User 006 Renamed"))

# Вывод списка сотрудников у администратора 3
for user in admin3.users_list:
    print(f"User ID: {user.user_id}, Name: {user.name}, Access Level: {user.access_level}")

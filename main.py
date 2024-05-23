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
    user5 = User(103, "User 005")

    # Администратор добавляет сотрудников
    print(admin1.add_user(user1))
    print(admin1.add_user(user2))
    print(admin1.add_user(user3))

    # Пытаемся добавить администратора как обычного сотрудника
    print(admin1.add_user(admin1))  # Должно вернуть ошибку

    # Администратор удаляет сотрудника
    print(admin1.remove_user(102))

    # Администратор редактирует сотрудника
    print(admin1.edit_user(103, "User 003 Renamed"))

    # Вывод списка сотрудников у администратора
    for user in admin1.users_list:
        print(f"User ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

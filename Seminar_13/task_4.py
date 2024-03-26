"""
Доработаем задачи 3 и 4. Создайте класс Project, содержащий атрибуты – список пользователей проекта и админ проекта.
 Класс имеет следующие методы:
Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
Метод входа в систему – требует указать имя и id пользователя. Далее метод создает пользователя и проверяет есть ли он
 в списке пользователей проекта. Если в списке его нет, то вызывается исключение доступа. Если пользователь присутствует
  в списке пользователей проекта, то пользователь, который входит - получает его уровень доступа и становится
администратором.
Метод добавление пользователя в список пользователей. Если уровень пользователя меньше, чем уровень админа,
 вызывайте исключение уровня доступа.
* метод удаления пользователя из списка пользователей проекта
* метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера
"""
from MyExceptions import AccessError
from task_3 import User
import json
from pathlib import Path


class Project:
    @classmethod
    def get_users_list(cls, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            my_dict = json.load(f, object_hook=lambda d: {int(k) if k.isdigit() else k: v for k, v in d.items()})
        users_list = []
        for level, users in my_dict.items():
            for user_id, name in users.items():
                user = User(name, user_id, level)
                users_list.append(user)
        return Project(users_list)

    def __init__(self, users_list=None):
        if users_list is None:
            self.users_list = []
        self.users_list = users_list
        self.admin = None

    def login(self):
        print('Введите свои персональные данные: ')
        user_to_check = User(input('Введите Ваше имя: '), int(input('Введите Id: ')))
        if user_to_check not in self.users_list:
            raise AccessError(user_to_check.name, user_to_check.u_id)
        for user in self.users_list:
            if user == user_to_check:
                self.admin = user
                print(f'{user_to_check} successfully logged in!')
                break


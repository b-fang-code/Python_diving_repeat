"""
Создайте класс с базовым исключением и дочерние классы-исключения:
ошибка уровня, ошибка доступа.
Вспомните задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный идентификатор
 и уровень доступа (от 1 до 7).
Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
Реализуйте магический метод проверки на равенство пользователей
"""

class User:
    def __init__(self, name, user_id, level):
        self.level = level
        self.name = name
        self.u_id = user_id

    def __eq__(self, other):
        return self.name == other.name and self.u_id == other.id

    def __repr__(self):
        return f'User {self.name=}, {self.u_id=}, {self.level=}'
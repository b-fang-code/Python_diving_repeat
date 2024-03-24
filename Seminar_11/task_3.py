"""
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста и для пользователя.
"""


class Archive:
    """Класс Archive, который хранит пару число и строку, ранее созданные экземпляры сохраняются в list-архив"""
    _instance = None

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_list = []
        else:
            cls._instance.archive_list.append((cls._instance.number, cls._instance.string))
        return cls._instance

    def __init__(self, number, string):
        self.string = string
        self.number = number

    def __str__(self):
        return f'Numb: {self.number}, Word: {self.string}, Archive: {self.archive_list}'

    def __repr__(self):
        return f'{type(self).__name__}({self.number}, "{self.string}")'


if __name__ == '__main__':
    arch_1 = Archive(32, 'Строка')
    print(arch_1)
    arch_2 = Archive(11, 'Слово')
    print(arch_2)
    arch_3 = Archive(43, 'Word')
    print(arch_3)
    print(repr(arch_3))
    print(Archive.__doc__)

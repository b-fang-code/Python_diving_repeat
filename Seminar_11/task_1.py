"""
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания (time.time)
"""
import time


class MyString(str):

    def __init__(self, value, name):
        self.name = name
        self.value = value

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.value = value
        instance.name = name
        instance.start_time = time.time()
        return instance

    def __str__(self):
        return f'Value: {self.value}, Name: {self.name}, created: {self.start_time}'


if __name__ == '__main__':
    my_str = MyString('3', 'First')
    print(my_str)

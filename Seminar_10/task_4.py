"""
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания. Используйте импорт класса в новый файл.
У сотрудника должен быть:
шестизначный идентификационный номер
уровень доступа, вычисляемый как остаток от деления суммы цифр id на семь
"""

from task_3 import Person


class Employee(Person):
    def __init__(self, id_, *args, **kwargs):
        self.id_ = id_
        self.level = sum(int(i) for i in str(self.id_)) % 7
        super().__init__(*args, **kwargs)


if __name__ == '__main__':
    emp_1 = Employee(998877, 'Vasiliev', 'Pavel', 'Andreevich', 36)
    print(emp_1.full_name())
    print(f'{emp_1.level = }')

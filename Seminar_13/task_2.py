"""
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и значение по умолчанию.
При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
"""


def get_value(my_dict, key, value='key not found'):
    try:
        return my_dict[key]
    except KeyError:
        return value


dict_ = {1: 'One', 2: "Two", 3: 'Three'}
val = get_value(dict_, 6)
print(val)

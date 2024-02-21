'''
Создайте вручную кортеж содержащий элементы разных типов.
Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
'''
import pprint

tup = ((5, 6), 'text', -18.5, True, 11, {1, 2}, [7, 8], 2.0 + 1j, b'\x01\x01\x01', {1: 'one', 2: 'two'}, 0.5, False)

dic = {}

for el in tup:
    el_type = str(type(el))
    if el_type not in dic.keys():
        dic[el_type] = [el]
    else:
        dic[el_type].append(el)
print(dic)
 
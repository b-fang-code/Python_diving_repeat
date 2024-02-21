'''
Создайте вручную список с повторяющимися элементами.
Удалите из него все элементы, которые встречаются дважды.
'''

# lst = [1, 2, 3, 4, 5, 1, 2, 3, 3, 5, 6, 7, 9]
lst = [12, 12, 11, 11, 13, 14, 18, 17, 18]
# new_lst = []                           1 способ
#
# for i in lst:
#     if lst.count(i) != 2:
#         new_lst.append(i)
# print(new_lst)


for num in lst:                           # 2 способ
    if lst.count(num) ==2:
        for _ in range(2):
            lst.remove(num)
print(lst)
"""
Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла,
возвращайтесь в его начало.
"""


def unit_files(file_nums, file_names, new_file):
    with(
        open(new_file, 'w', encoding='utf-8') as u,
        open(file_nums, 'r', encoding='utf-8') as f1,
        open(file_names, 'r', encoding='utf-8') as f2
    ):
        lst_prod = [int(line.split('|')[0]) * float(line.split('|')[1]) for line in f1]
        for num, line_2 in zip(lst_prod, f2):
            if num < 0:
                u.write(f'{line_2.lower().strip()}|{abs(num)}\n')
            else:
                u.write(f'{str(line_2).upper().strip()}|{int(num)}\n')


if __name__ == '__main__':
    unit_files('pairs.txt', 'names.txt', 'union.txt')

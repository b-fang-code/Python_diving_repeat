from random import randint, uniform

START, END = -1000, 1000


def fill_file(file_name, lines_num):
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(lines_num):
            f.write(f'{randint(START, END)}|{uniform(START, END)}\n')

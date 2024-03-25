"""
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
"""
import json

class Factorial:
    def __init__(self, k, file_name):
        self.k = k
        self.res = []
        self.file = None
        self.file_name = file_name

    def __call__(self, n):
        factorial = self._factorial(n)
        self.res.append({n: factorial})
        self.res = self.res[-self.k:]
        return factorial

    def _factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self._factorial(n - 1)

    def get_last(self):
        return self.res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file = open(f'{self.file_name}', 'w', encoding='utf-8')
        json.dump(self.res, self.file)
        self.file.close()


if __name__ == '__main__':
    with Factorial(5, 'task_2.json') as f:
        f1 = f(5)
        f2 = f(6)
        print(f.get_last())

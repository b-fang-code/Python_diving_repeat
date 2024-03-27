"""
Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""
import unittest
from task_1 import delete_literal


class TestDeleteLiteral(unittest.TestCase):
    def test_1(self):
        self.assertEqual(delete_literal('ljasfl dsfgds df'), 'ljasfl dsfgds df')

    def test_2(self):
        self.assertEqual(delete_literal('ljAsfl dsfgds df'), 'ljasfl dsfgds df')

    def test_3(self):
        self.assertEqual(delete_literal('ljasfl dsfgds df-'), 'ljasfl dsfgds df')

    def test_4(self):
        self.assertEqual(delete_literal('ljasfl dsfgds dfабв'), 'ljasfl dsfgds df')

    def test_5(self):
        self.assertEqual(delete_literal('ljasfАвыl длоdsфЫВFGDSыа -04df32-'), 'ljasfl dsfgds df')


if __name__ == '__main__':
    unittest.main(verbosity=2)
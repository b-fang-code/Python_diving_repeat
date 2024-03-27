"""
Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""

from task_2 import delete_literal


def test_1():
    assert delete_literal('ljasfl dsfgds df') == 'ljasfl dsfgds df'


def test_2():
    assert delete_literal('ljAsfl dsfgds df') == 'ljasfl dsfgds df'


def test_3():
    assert delete_literal('ljasfl dsfgds df-') == 'ljasfl dsfgds df'


def test_4():
    assert delete_literal('ljasfl dsfgds dfабв') == 'ljasfl dsfgds df'


def test_5():
    assert delete_literal('ljasfАвыl длоdsфЫВFGDSыа -04df32-') == 'ljasfl dsfgds df'

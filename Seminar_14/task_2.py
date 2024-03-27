"""
Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""

import string
import doctest


def delete_literal(text):
    """
    >>> delete_literal('ljasfl dsfgds df')
    'ljasfl dsfgds df'
    >>> delete_literal('ljAsfl dsfgds df')
    'ljasfl dsfgds df'
    >>> delete_literal('ljasfl dsfgds df-')
    'ljasfl dsfgds df'
    >>> delete_literal('ljasfl dsfgds dfабв')
    'ljasfl dsfgds df'
    >>> delete_literal('ljasfАвыl длоdsфЫВFGDSыа -04df32-')
    'ljasfl dsfgds df'
    """
    return ''.join(i for i in text if i in string.ascii_letters or i == ' ').lower()


if __name__ == '__main__':
    doctest.testmod(verbose=True)

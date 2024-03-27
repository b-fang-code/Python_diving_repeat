"""
Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""
import string


def delete_literal(text):
    return ''.join(i for i in text if i in string.ascii_letters or i == ' ').lower()


if __name__ == '__main__':
    test_text = 'ljasfАвыl длоdsфЫВFGDSыа -04df32-'
    print(delete_literal(test_text))

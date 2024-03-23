"""
Создайте три (или более) отдельных классов животных.Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.

"""


class Creature:
    def __init__(self, name):
        self.name = name


class Bird(Creature):
    def __init__(self, wingspan, name):
        super().__init__(name)
        self.wing = wingspan

    def get_special_info(self):
        return f'Длина крыла {self.wing / 2}'


class Fish(Creature):
    def __init__(self, deep_water, name):
        super().__init__(name)
        self.deep_water = deep_water

    def get_special_info(self):
        if self.deep_water < 10:
            return 'Мелководная'
        elif 10 < self.deep_water < 100:
            return 'Средневодная'
        else:
            return 'Глубоководная'


class Mammal(Creature):
    def __init__(self, weight, name):
        self.weight = weight
        super().__init__(name)

    def get_special_info(self):
        if self.weight < 10:
            return 'Мелкое млекопитающее'
        elif 10 < self.weight < 100:
            return 'Среднее млекопитающее'
        else:
            return 'Крупное млекопитающее'


if __name__ == '__main__':
    bird1 = Bird(42, 'Cорока')
    bird2 = Bird(94, 'Орел')
    fish1 = Fish(99, 'Акула')
    fish2 = Fish(140, 'Удильщик')
    mammal1 = Mammal(300, 'Слон')
    mammal2 = Mammal(2, 'Мышь')
    print(bird1.name, bird1.get_special_info())
    print(bird2.name, bird2.get_special_info())
    print(fish1.name, fish1.get_special_info())
    print(fish2.name, fish2.get_special_info())
    print(mammal1.name, mammal1.get_special_info())
    print(mammal2.name, mammal2.get_special_info())

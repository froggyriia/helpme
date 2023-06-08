# при наследовании классов все методы и атрибуты переходят наследникам
class Ingredient:
    country = "Russia"

    def __init__(self, weight: float, callorage: int):
        self._weight = weight
        self._callorage = callorage

    def get_weight(self):
        return self._weight

    def get_callorage(self):
        return self._callorage

    def prepare(self):
        pass


class Bread(Ingredient):

    def prepare(self):
        print('Bread sliced')
        pass


class Tomato(Ingredient):

    def prepare(self):
        print('Tomato salted')
        self._weight += 0.08
        self._callorage += 1.1


class Potato(Ingredient):
    def prepare(self):
        print('Potato fried')
        self._weight *= 0.8
        self._callorage *= 1.5


class Berries(Ingredient):
    def __init__(self, count: int, weight: float, callorage: int):
        self._count = count
        super().__init__(weight, callorage)  # вызываем нужные атрибуты из класса родителя


def make_dinner(ingredients):
    callorage = 0
    for ingredient in ingredients:
        ingredient.prepare()
        callorage += ingredient.get_callorage()
    print(f'Dinner was made, total callorage is {callorage}')


potato, tomato, bread = Potato(0.3, 500), Tomato(0.4, 200), Bread(0.1, 100)
ingredients = [potato, tomato, bread]
# print(isinstance(potato, Ingredient)) # проверка является ли potato Ingredient/ принадлежит ли

make_dinner(ingredients)

Ingredient.country = 'USA'  # изменeние переменной у ВСЕХ наследуемых классов
tomato.country = "Zimbabwe"  # изменение переменной ТОЛЬКО у класса Tomato

from random import choice


class Human:
    GENOM_COUNT = 46

    def __init__(self, name: str, status: str = ''):
        self.name = name
        self.status = status

        # self.__class__.GENOM_COUNT  # доступ к GENOM_COUNT

    def say(self, msg: str):
        print(f'{self.name} {self.status} said: {msg}')

    def description(self):
        return f'{self.name} {self.status}'

    @classmethod
    def change_genom_count(cls):  # метод класса может быть вызван как из классов так и из объектов
        cls.GENOM_COUNT += 1  # способ изменнения перменных доступных всему классу (через методы класса)

    @staticmethod  # staticmethod может быть вызван и из класса и из объектов но не имеет к ним доступа
    def create_new_name():
        return choice(('a', 'b', 'c'))




me = Human(name='riia', status='student')
print(me.description())

print(f"genom count before {Human.GENOM_COUNT}")
Human.change_genom_count()
print(f"genom count after {Human.GENOM_COUNT}")
me.change_genom_count()
print(f"genom count after {Human.GENOM_COUNT}")

print(me.create_new_name())

me.say('vme')
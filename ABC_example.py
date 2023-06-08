from abc import ABC, abstractmethod  # Abstract Base Class
from math import pi


class Shape(ABC):  # делаем Shape абстрактным базовым классом, чтобы нельзя было создать объект этого класса

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width: float, length: float):
        super().__init__()
        self._length = length
        self._width = width

    def area(self):
        return self._width * self._length

    def perimeter(self):
        return self._width * 2 + self._length * 2

    #нет особого смысла писать отдельный класс для квадрата, его можно определить и просто методом
    def get_square(self, length: float):
        return Rectangle(length, length)


class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)


class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__()
        self._radius = radius

    def area(self):
        return self._radius ** 2 * pi

    def perimeter(self):
        return 2 * pi * self._radius


the_rectangle1 = Rectangle(4.0, 5.0)
the_rectangle2 = Rectangle(4.0, 4.0)
the_circle = Circle(1.0)
the_square = Square(4.0)
print(the_square.area(), the_rectangle1.area(), the_rectangle2.area())
print(the_circle.area(), the_circle.perimeter())
a = Rectangle(1, 2)
print(a.area())  # 2
print(a.perimeter())  # 5 так то 6 ильяс лох
b = Square(3)
print(b.area())  # 9
print(b.perimeter())  # 12

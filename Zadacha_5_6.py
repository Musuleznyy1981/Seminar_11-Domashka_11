# Максим Мусулезный Задача 5,6
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

# Задача 5


class Rectangle:

    def __init__(self, side_a: int = 1, side_b: int | None = None):
        self._side_a = side_a
        self._side_b = side_b if side_b else side_a

    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)


    def get_area(self):
        return self._side_a * self._side_b

    def __add__(self, other):
        return Rectangle(self._side_a + other._side_a, self._side_b + other._side_b)

    def __sub__(self, other):
        return Rectangle(abs(self._side_a - other._side_a), abs(self._side_b - other._side_b))

    def __str__(self):
        return f"прямоугольник со сторонами: {self._side_a}   {self._side_b} и периметром: {self.get_perimeter()}"


if __name__ == '__main__':
    rect1 = Rectangle(4,6)
    rect2 = Rectangle(2,3)
    rect3 = rect1 + rect2
    print(rect3)

    rect4 = rect1 - rect2
    print(rect4)


# Задача 6
# Доработайте прошлую задачу 3 .
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения



class Rectangle:

    def __init__(self, side_a: int = 1, side_b: int | None = None):
        self._side_a = side_a
        self._side_b = side_b if side_b else side_a

    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)


    def get_area(self):
        return self._side_a * self._side_b

    def __add__(self, other):
        return Rectangle(self._side_a + other._side_a, self._side_b + other._side_b)

    def __sub__(self, other):
        return Rectangle(abs(self._side_a - other._side_a), abs(self._side_b - other._side_b))

    def __lt__(self, other):                            #метод меньше
        return self.get_area() < other.get_area()

    def __eq__(self, other):                            #метод равно
        return self.get_area() == other.get_area()

    def __le__(self, other):                            #метод меньше или равно
        return self.get_area() <= other.get_area()

    def __str__(self):
        return f"прямоугольник со сторонами: {self._side_a}   {self._side_b} и периметром: {self.get_perimeter()}"


if __name__ == '__main__':
    rect1 = Rectangle(2,3)
    rect2 = Rectangle(2,3)
    rect3 = rect1 + rect2
    print(rect3)

    rect5 = Rectangle(2,2)
    rect6 = Rectangle(3, 3)
    print(rect1 < rect2)
    print(rect1 > rect2)
    print(rect1 <= rect2)
    print(rect1 >= rect2)
    print(rect1 == rect2)
    print(rect1 != rect2)
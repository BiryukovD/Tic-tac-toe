# Создайте класс одной из геометрических фигур (например, прямоугольника),
# где в конструкторе задаются атрибуты:  начальные координаты x, y, width и height (или другие в зависимости от выбранной фигуры).
#
# Создайте метод, который возвращает атрибуты прямоугольника как строку
# (постарайтесь применить магический метод __str__). Для объекта прямоугольника со значениями атрибута x = 5, y = 10,
# width = 50, height = 100 метод должен вернуть строку Rectangle : 5, 10, 50, 100.
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def get_area(self):
        return self.height*self.width

    def __str__(self):
        return f'{self.x} {self.y} {self.width} {self.height}'

obj = Rectangle(2, 3, 40, 50)
print(obj.get_area())

class Box:
    def __init__(self):
        self.shapes = []

    def put_inside(self, shape):
        self.shapes.append(shape)

    def desc(self):
        print(f"Следующие фигуры в коробке: ")
        for shape in self.shapes:
            shape.desc()


class Shape:
    name = None

    def __init__(self, color):
        self.color = color
        self.box = None

    def desc(self):
        print(f"Один {self.color} {self.name}")


class Square(Shape):
    name = "квадрат"

    def __init__(self, color, size):
        self.a = size
        super().__init__(color)


class Circle(Shape):
    name = "круг"

    def __init__(self, color, size):
        self.size = size
        super().__init__(color)


class Triangle(Shape):
    name = "треугольник"

    def __init__(self, color, size):
        self.size = size
        super().__init__(color)


b1 = Box()
shape1 = Square("пурпурный", 11)
shape2 = Circle("бирюзовый", 4)
shape3 = Triangle("оранжевый", 10)

b1.put_inside(shape3)
b1.put_inside(shape2)
b1.put_inside(shape1)

b1.desc()
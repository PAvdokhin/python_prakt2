class Figure:
    def __init__(self):
        self.color = "white"

    def change_color(self, color):
        self.color = color
    def print_characteristics(self):
        pass


class Oval(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def change_color(self, color):
        self.color = color

    def characteristics(self):
        print(f'Oval: color - {self.color}, length - {self.length}, width - {self.width}')


class Square(Figure):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def change_color(self, color):
        self.color = color
    def characteristics(self):
        print(f'Square: color - {self.color}, length - {self.length}')


oval_1 = Oval(10, 15)
oval_1.characteristics()
oval_1.change_color("red")
oval_1.characteristics()

square_1 = Square(15)
square_1.characteristics()
square_1.change_color("black")
square_1.characteristics()
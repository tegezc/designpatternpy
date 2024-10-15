from abc import ABC, abstractmethod

# Interface untuk elemen
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Implementasi elemen konkret
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        visitor.visit_rectangle(self)

# Interface untuk visitor
class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass

# Implementasi visitor konkret
class AreaCalculator(ShapeVisitor):
    def visit_circle(self, circle):
        return 3.14 * circle.radius**2

    def visit_rectangle(self, rectangle):
        return rectangle.width * rectangle.height

# Penggunaan
circle = Circle(5)
rectangle = Rectangle(4, 6)

calculator = AreaCalculator()
print(circle.accept(calculator))  # Output: 78.5
print(rectangle.accept(calculator))  # Output: 24

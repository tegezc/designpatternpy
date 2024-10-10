class OldShape:
    def draw(self, x, y):
        print(f"Drawing old shape at ({x}, {y})")

class NewShape:
    def draw(self, point):
        print(f"Drawing new shape at ({point.x}, {point.y})")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class ShapeAdapter:
    def __init__(self, new_shape):
        self.new_shape = new_shape

    def draw(self, x, y):
        point = Point(x, y)
        self.new_shape.draw(point)

old_shape = OldShape()
new_shape = NewShape()
adapter = ShapeAdapter(new_shape)

old_shape.draw(10, 20)  # Output: Drawing old shape at (10, 20)
adapter.draw(30, 40)  # Output: Drawing new shape at (30, 40)

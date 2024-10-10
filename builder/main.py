"""
Builder patter
"""

class Car:
    def __init__(self, wheels, engine, color):
        self.wheels = wheels
        self.engine = engine
        self.color = color

    def __str__(self):
        return f"Car with {self.wheels} wheels, {self.engine} engine, and {self.color} color"

class CarBuilder:
    def __init__(self):
        self.car = Car(0, None, None)

    def set_wheels(self, wheels):
        self.car.wheels = wheels
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def build(self):
        return self.car

# Penggunaan
car = CarBuilder() \
    .set_wheels(4) \
    .set_engine("V8") \
    .set_color("red") \
    .build()

print(car)

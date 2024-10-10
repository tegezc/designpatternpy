"""
Prototype Pattern
"""

import copy

class Prototype:
    def clone(self):
        raise NotImplementedError('Subclass must implement abstract method')

class Car(Prototype):
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

# Membuat objek mobil pertama
car1 = Car("Toyota Camry", "Silver")

# Membuat objek mobil kedua dengan mengkloning
car2 = car1.clone()
car2.color = "Black"

print(car1.model, car1.color)  # Output: Toyota Camry Silver
print(car2.model, car2.color)  # Output: Toyota Camry Black

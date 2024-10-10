"""
Abstract factory demo
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    abstract class
    """
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

class SportCar(Car):
    def start(self):
        print("Sport car started")

class SedanCar(Car):
    def start(self):
        print("Sedan car started")

class SportMotorcycle(Motorcycle):
    def start(self):
        print("Sport motorcycle started")

class BebekMotorcycle(Motorcycle):
    def start(self):
        print("Bebek motorcycle started")

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_motorcycle(self):
        pass

class SportVehicleFactory(VehicleFactory):
    def create_car(self):
        return SportCar()

    def create_motorcycle(self):
        return SportMotorcycle()

class SedanVehicleFactory(VehicleFactory):
    def create_car(self):
        return SedanCar()

    def create_motorcycle(self):
        return BebekMotorcycle()

# Penggunaan
sport_factory = SportVehicleFactory()
sport_car = sport_factory.create_car()
sport_motorcycle = sport_factory.create_motorcycle()

sport_car.start()  # Output: Sport car started
sport_motorcycle.start()  # Output: Sport motorcycle started

sedan_factory = SedanVehicleFactory()
sedan_car = sedan_factory.create_car()
bebek_motorcycle = sedan_factory.create_motorcycle()

sedan_car.start()  # Output: Sedan car started
bebek_motorcycle.start()  # Output: Bebek motorcycle started

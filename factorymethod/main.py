"""
factory method pattern
"""

from enum import Enum


class VehicleType(Enum):
    """
    enum untuk factory method vehicle
    """
    CAR = 1
    MOTORCYCLE = 2
    TRUCK = 3


class Vehicle:
    """
    factory method
    """

    def __init__(self, name):
        self.name = name

    def start_engine(self):
        """
        method create
        """
        print(f"Starting {self.name} engine")


class Car(Vehicle):
    """
    factory method
    """


class Motorcycle(Vehicle):
    """
    factory method
    """


class VehicleFactory:
    """
    factory method
    """

    def create_vehicle(self, vehicle_type):
        """
        method create
        """
        if vehicle_type == VehicleType.CAR:
            return Car("Car")
        if vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle("Motorcycle")

        raise ValueError("Invalid vehicle type")


# Menggunakan factory
factory = VehicleFactory()
car = factory.create_vehicle(VehicleType.CAR)
motorcycle = factory.create_vehicle(VehicleType.MOTORCYCLE)

car.start_engine()
motorcycle.start_engine()

#============ implementasi style lainnya
class VehicleFactory1:
    def create_vehicle(self):
        pass

class CarFactory(VehicleFactory1):
    def create_vehicle(self):
        return Car("Car")

class MotorcycleFactory(VehicleFactory1):
    def create_vehicle(self):
        return Motorcycle("Motorcycle")

# Menggunakan factory method
car_factory = CarFactory()
car = car_factory.create_vehicle()

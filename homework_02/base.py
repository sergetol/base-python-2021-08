from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight: float = 0, fuel: float = 0, fuel_consumption: float = 0):
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        super().__init__()

    def start(self):
        if not self.started:
            if self.fuel <= 0:
                raise LowFuelError
            self.started = True

    def move(self, distance: float):
        fuel_rest = self.fuel - self.fuel_consumption * distance
        if fuel_rest < 0:
            raise NotEnoughFuel
        self.fuel = fuel_rest

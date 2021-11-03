"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(
        self,
        weight: float = 0,
        fuel: float = 0,
        fuel_consumption: float = 0,
        max_cargo: float = 0,
    ):
        self.max_cargo = max_cargo
        self.cargo = 0
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)

    def load_cargo(self, cargo: float):
        new_cargo = self.cargo + cargo
        if new_cargo > self.max_cargo:
            raise CargoOverload
        self.cargo = new_cargo

    def remove_all_cargo(self) -> float:
        current_cargo = self.cargo
        self.cargo = 0
        return current_cargo

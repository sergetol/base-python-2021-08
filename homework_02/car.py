"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    def __init__(
        self,
        weight: float = 0,
        fuel: float = 0,
        fuel_consumption: float = 0,
    ):
        self.engine = None
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)

    def set_engine(self, engine: Engine):
        self.engine = engine

"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine
from homework_02.exceptions import MyException


class Car(Vehicle):
    def __init__(
        self,
        weight: float = 0,
        fuel: float = 0,
        fuel_consumption: float = 0,
        engine: Engine = None,
    ):
        self.engine = engine
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)

    @property
    def engine(self) -> Engine:
        return self._engine

    @engine.setter
    def engine(self, engine: Engine):
        if engine is None:
            self._engine = Engine()
            return
        if not isinstance(engine, Engine):
            raise MyException(
                f"Can not set {self.__class__.__name__}'s 'engine' property (Engine object) with value: {engine}"
            )
        self._engine = engine

    def set_engine(self, engine: Engine = None):
        self.engine = engine

    def __str__(self) -> str:
        return f"{super().__str__()}, engine={self.engine}"

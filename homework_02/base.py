from abc import ABC
from homework_02.exceptions import MyException, LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight: float = 0, fuel: float = 0, fuel_consumption: float = 0):
        self._started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        super().__init__()

    @staticmethod
    def is_value_valid(value) -> bool:
        return (isinstance(value, float) or isinstance(value, int)) and value >= 0

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, weight: float):
        if not self.is_value_valid(weight):
            raise MyException(
                f"Can not set {self.__class__.__name__}'s 'weight' property (float, >=0) with value: {weight}"
            )
        self._weight = weight

    @property
    def fuel(self) -> float:
        return self._fuel

    @fuel.setter
    def fuel(self, fuel: float):
        if not self.is_value_valid(fuel):
            raise MyException(
                f"Can not set {self.__class__.__name__}'s 'fuel' property (float, >=0) with value: {fuel}"
            )
        if fuel == 0:
            self.stop()
        self._fuel = fuel

    @property
    def fuel_consumption(self) -> float:
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, fuel_consumption: float):
        if not self.is_value_valid(fuel_consumption):
            raise MyException(
                f"Can not set {self.__class__.__name__}'s 'fuel_consumption' property (float, >=0)"
                + f" with value: {fuel_consumption}"
            )
        self._fuel_consumption = fuel_consumption

    @property
    def started(self) -> bool:
        return self._started

    def start(self):
        if not self.started:
            if self.fuel > 0 or self.fuel_consumption == 0:
                self._started = True
            else:
                raise LowFuelError(
                    f"Can not start {self.__class__.__name__}: fuel = {self.fuel}"
                )

    def stop(self):
        if self.started:
            self._started = False

    def move(self, distance: float):
        if not self.is_value_valid(distance):
            raise MyException(f"Wrong distance (float, >=0) value: {distance}")
        fuel_rest = self.fuel - self.fuel_consumption * distance
        try:
            self.start()
            self.fuel = fuel_rest
            # self.stop()
        except MyException:
            raise NotEnoughFuel(
                f"Not enough fuel to move {self.__class__.__name__}:"
                + f" distance = {distance}, fuel = {self.fuel}, enough_fuel = {self.fuel - fuel_rest}"
            ) from None

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}:"
            + f" weight={self.weight}, fuel={self.fuel}, fuel_consumption={self.fuel_consumption}, started={self.started}"
        )

    def __repr__(self) -> str:
        return f"<{self.__str__()}>"

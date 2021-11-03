"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import MyException, CargoOverload


class Plane(Vehicle):
    def __init__(
        self,
        weight: float = 0,
        fuel: float = 0,
        fuel_consumption: float = 0,
        max_cargo: float = 0,
        cargo: float = 0,
    ):
        self.max_cargo = max_cargo
        self.cargo = cargo
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)

    @property
    def max_cargo(self) -> float:
        return self._max_cargo

    @max_cargo.setter
    def max_cargo(self, max_cargo: float):
        if not self.is_value_valid(max_cargo):
            raise MyException(
                f"Can not set {self.__class__.__name__}'s 'max_cargo' property (float, >=0) with value: {max_cargo}"
            )
        self._max_cargo = max_cargo

    @property
    def cargo(self) -> float:
        return self._cargo

    @cargo.setter
    def cargo(self, cargo: float):
        if not self.is_value_valid(cargo):
            raise MyException(
                f"Can not set {self.__class__.__name__}'s 'cargo' property (float, >=0) with value: {cargo}"
            )
        if cargo > self.max_cargo:
            raise CargoOverload(
                f"Can not set {self.__class__.__name__}'s 'cargo' property. New 'cargo' value will exceed max cargo:"
                + f" cargo = {cargo}, max_cargo = {self.max_cargo}"
            )
        self._cargo = cargo

    def load_cargo(self, cargo: float = 0):
        if not self.is_value_valid(cargo):
            raise MyException(f"Wrong cargo (float, >=0) value: {cargo}")
        try:
            self.cargo += cargo
        except MyException:
            raise CargoOverload(
                f"Can not load cargo: {cargo}. Total cargo will exceed {self.__class__.__name__}'s max cargo:"
                + f" current cargo = {self.cargo}, max_cargo = {self.max_cargo}"
            ) from None

    def remove_all_cargo(self) -> float:
        current_cargo = self.cargo
        self.cargo = 0
        return current_cargo

    def __str__(self) -> str:
        return f"{super().__str__()}, max_cargo={self.max_cargo}, cargo={self.cargo}"

"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class MyException(BaseException):
    pass


class LowFuelError(MyException):
    def __init__(self, msg: str = "Low Fuel Exception"):
        super().__init__(msg)


class NotEnoughFuel(MyException):
    def __init__(self, msg: str = "Not Enough Fuel Exception"):
        super().__init__(msg)


class CargoOverload(MyException):
    def __init__(self, msg: str = "Cargo Overload Exception"):
        super().__init__(msg)

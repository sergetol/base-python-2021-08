"""
create dataclass `Engine`
"""
from dataclasses import dataclass
from homework_02.exceptions import MyException


@dataclass
class Engine:
    volume: float = 0
    pistons: int = 0

    def __setattr__(self, name: str, value):
        if name == "volume":
            if not (
                (isinstance(value, float) or isinstance(value, int)) and value >= 0
            ):
                raise MyException(
                    f"Wrong {self.__class__.__name__}'s 'volume' property (float, >=0) value: {value}"
                )
        elif name == "pistons":
            if not (isinstance(value, int) and value >= 0):
                raise MyException(
                    f"Wrong {self.__class__.__name__}'s 'pistons' property (int, >=0) value: {value}"
                )
        super().__setattr__(name, value)

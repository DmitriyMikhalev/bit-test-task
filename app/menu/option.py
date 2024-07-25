from abc import ABCMeta
from typing import Callable, Any


class BaseOption(metaclass=ABCMeta):
    def __init__(self, description: str) -> None:
        self._description = description

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return self._description


class MenuOption(BaseOption):
    pass


class FunctionalMenuOption(BaseOption):
    def __init__(self, description: str, callback: Callable) -> None:
        super().__init__(description)

        self._callback = callback

    def execute(self, *args, **kwargs) -> Any:
        return self._callback(*args, **kwargs)

from abc import ABCMeta
from typing import Iterable

from .option import BaseOption


class BaseMenu(metaclass=ABCMeta):
    def __init__(self, options: Iterable[BaseOption]) -> None:
        self._options: dict[int, BaseOption] = {
            idx: option for idx, option in enumerate(options, start=1)
        }

    def show(self) -> None:
        print(str(self))

    def __repr__(self) -> str:
        return self.__class__.__name__

    def __len__(self) -> int:
        return len(self._options)

    def __str__(self) -> str:
        return "\n".join(f"{i}. {opt}" for (i, opt) in self._options.items())


class FunctionalMenu(BaseMenu):
    def __init__(self, options: Iterable[BaseOption]) -> None:
        super().__init__(options)

    def execute(self, option: int) -> None:
        return self._options[option].execute()


class Menu(BaseMenu):
    def __init__(
        self,
        options: Iterable[BaseOption],
        submenues: Iterable[BaseMenu] = []
    ) -> None:
        super().__init__(options)

        self._submenues: dict[int, BaseMenu] = {
            i: val for i, val in enumerate(submenues, start=1)
        }

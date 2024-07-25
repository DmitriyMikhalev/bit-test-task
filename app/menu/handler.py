import sys

from .utils import clear_console, read_int
from .menu import BaseMenu, Menu


class MenuHandler:
    def __init__(self, root_menu: BaseMenu):
        self._root_menu = root_menu
        self._chain = [root_menu]

    def execute(self, option: int):
        if option == 0:
            if self.is_current_root:
                print("Завершение работы программы.")
                sys.exit(0)
            else:
                self._chain.pop()
        elif isinstance(self.current_menu, Menu):
            self._chain.append(self.current_menu._submenues[option])
        else:
            return self.current_menu.execute(option)

    @property
    def current_menu(self):
        return self._chain[-1]

    @property
    def is_current_root(self):
        return self.current_menu is self._root_menu

    def __len__(self):
        return len(self.current_menu)

    def read_option(self):
        msg = "Выберите опцию (0 - {}): ".format("назад" if not self.is_current_root else "выход")
        return read_int(
            message=msg,
            error_message="Ошибка, повторите ввод: ",
            max_value=len(self.current_menu)
        )

    def poll(self):
        while True:
            self.current_menu.show()
            self.execute(option=self.read_option())

            clear_console()

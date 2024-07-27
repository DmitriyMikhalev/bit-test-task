from typing import Callable
from functools import wraps

from pydantic import ValidationError


def callback(msg: str | None = "\nОперация успешно завершена.\n") -> Callable:
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def wrapped() -> Callable:
            try:
                func()
            except ValidationError as e:
                print(e)
                print("\nВведенные данные некорректны, отмена операции.\n")
            except Exception as e:
                print(e)
                print("\nПроизошла непредвиденная ошибка, отмена операции.\n")
            else:
                print(msg)
        return wrapped
    return wrapper

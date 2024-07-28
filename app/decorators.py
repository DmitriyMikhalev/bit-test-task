from typing import Callable
from functools import wraps
import logging

from pydantic import ValidationError


logger = logging.getLogger("logger")


def callback(msg: str = "\nОперация успешно завершена.\n") -> Callable:
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def wrapped() -> None:
            try:
                func()
            except ValidationError as e:
                logger.error(e)
                print("\nВведенные данные некорректны, отмена операции.\n")
            except Exception as e:
                logger.error(e)
                print("\nПроизошла непредвиденная ошибка, отмена операции.\n")
            else:
                print(msg)
        return wrapped
    return wrapper

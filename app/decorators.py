from pydantic import ValidationError


def callback(func):
    def wrapped():
        try:
            func()
        except ValidationError as e:
            print(e)
            print("\nВведенные данные некорректны, отмена операции.\n")
        except Exception as e:
            print(e)
            print("\nПроизошла непредвиденная ошибка, отмена операции.\n")
        else:
            print("\nОперация успешно завершена.\n")
    return wrapped

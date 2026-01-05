from typing import Any, Callable


def log(filename: None | str = None) -> Callable:
    def wrapper(func: Callable) -> Callable:
        def inner(*args: tuple, **kwargs: dict) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"Функция выполнена успешно {func.__name__}, {result}"
            except Exception as e:
                result = None
                message = f"Ошибка: {e}, {func.__name__}. Аргументы: {args} {kwargs}"
            if filename is None:
                print(message)
            else:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(message + "\n")
            return result

        return inner

    return wrapper

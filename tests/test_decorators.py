from src.decorators import log

@log()
def plus(a, b):
    return a + b

def test_plus(capsys):
    plus(1, 2)
    captured = capsys.readouterr()
    assert captured.out == 'Функция выполнена успешно plus, 3\n'

def test_exception(capsys):
    plus(1, "apple")
    captured = capsys.readouterr()
    assert captured.out == "Ошибка: unsupported operand type(s) for +: 'int' and 'str', plus. Аргументы: (1, 'apple') {}\n"


@log("log.txt")
def plus_(a, b):
    return a + b

def test_plus_():
    plus_(1, 2)
    with open("log.txt", "r", encoding="utf-8") as f:
        log_reading = f.readlines()
        assert log_reading[-1] == "Функция выполнена успешно plus_, 3\n"

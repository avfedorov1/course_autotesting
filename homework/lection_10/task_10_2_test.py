# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного.
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_1_positive():
    assert all_division(10, 5) == 2


@pytest.mark.smoke
def test_2_positive():
    assert all_division(1000, 5, 4, 25, -1) == -2


def test_3_negative():
    with pytest.raises(AssertionError):
        assert all_division(125, 5) == 22


def test_4_string():
    try:
        all_division(2, 'abc')
    except TypeError:
        print(' Одним из аргументов передана строка', end='')


def test_5_string():
    try:
        all_division('2', 55)
    except TypeError:
        print(' Одним из аргументов передана строка', end='')


def test_6_delete_zero():
    with pytest.raises(ZeroDivisionError):
        assert all_division(5, 0)


def test_7_delete_zero():
    try:
        all_division(5, 0) == 0
    except ZeroDivisionError as err:
        assert str(err) == 'division by zero'


import datetime

import pytest


@pytest.fixture(scope='class')
def print_time_start_end():
    start = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'Время начала выполнения всех тестов: {start}')
    yield
    end = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'Время окончания выполнения всех тестов: {end}')


@pytest.fixture()
def print_execution_time():
    start = datetime.datetime.now()
    yield
    end = datetime.datetime.now()
    print(f'Время выполнения теста: {end - start}')

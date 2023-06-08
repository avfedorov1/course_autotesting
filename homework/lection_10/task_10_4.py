# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import time

import pytest


@pytest.mark.usefixtures('print_time_start_end')
class TestMy:

    def test_1(self):
        print(' Первый тест - ОК')
        time.sleep(1)

    def test_2(self):
        print(' Второй тест - ОК')
        time.sleep(1)

    def test_3(self, print_execution_time):
        print(' Третий тест - ОК')
        time.sleep(1)

    def test_4(self):
        print(' Четвертый тест - ОК')
        time.sleep(1)


a = TestMy()

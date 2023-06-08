# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a, b', [
    pytest.param(10, 5, marks=pytest.mark.smoke('smoke')),
    pytest.param(1000, 500, marks=pytest.mark.skip('bad test'))], ids=['smoke', 'bad test'])
def test_1_positive(a, b):
    assert all_division(a, b) == 2

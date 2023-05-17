# Напишите функцию to_roman, которая преобразуют арабское число (val) в римское (roman_str).
#
# Современные римские цифры записываются, выражая каждую цифру отдельно,
# начиная с самой левой цифры и пропуская цифру со значением нуля.
# Римскими цифрами 1990 отображается: 1000=М, 900=СМ, 90=ХС; в результате MCMXC.
# 2023 записывается как 2000=MM, 20=XX, 3=III; или MMXXIII.
# В 1666 используется каждый римский символ в порядке убывания: MDCLXVI.
#
# Например (Ввод --> Вывод) :
# 2008 --> MMVIII


def to_roman(val):
    """
    Функция преобразования арабских цифр в римские.
    :param val: Число
    :return: Строка
    """
    # Здесь нужно написать код
    str_val = str(val)
    lst = []
    list_val = list(str_val)
    # Задаем пустые переменные для начала
    thousands = ''
    hundreds = ''
    dozens = ''
    units = ''
    # Формируем список тысяч, сотен, десятков, единиц
    for i in range(len(list_val)):
        x = int(list_val[i]) * (10 ** (len(list_val) - i - 1))
        lst.append(str(x))
    # Присваиваем переменным значения, подходящие под условия
    for i in lst:
        if len(i) == 4:
            thousands = 'M' * int(i[0])
        if len(i) == 3:
            if int(i[0]) == 9:
                hundreds = 'CM'
            elif int(i[0]) == 8:
                hundreds = 'DCCC'
            elif int(i[0]) == 7:
                hundreds = 'DCC'
            elif int(i[0]) == 6:
                hundreds = 'DC'
            elif int(i[0]) == 5:
                hundreds = 'D'
            elif int(i[0]) == 4:
                hundreds = 'CD'
            else:
                hundreds = 'C' * int(i[0])
        if len(i) == 2:
            if int(i[0]) == 9:
                dozens = 'XC'
            elif int(i[0]) == 8:
                dozens = 'LXXX'
            elif int(i[0]) == 7:
                dozens = 'LXX'
            elif int(i[0]) == 6:
                dozens = 'LX'
            elif int(i[0]) == 5:
                dozens = 'L'
            elif int(i[0]) == 4:
                dozens = 'XL'
            else:
                dozens = 'X' * int(i[0])
        if len(i) == 1:
            if int(i[0]) == 9:
                units = 'IX'
            elif int(i[0]) == 8:
                units = 'VIII'
            elif int(i[0]) == 7:
                units = 'VII'
            elif int(i[0]) == 6:
                units = 'VI'
            elif int(i[0]) == 5:
                units = 'V'
            elif int(i[0]) == 4:
                units = 'IV'
            else:
                units = 'I' * int(i[0])
    roman_str = thousands + hundreds + dozens + units
    return roman_str

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [1133, 2224, 1938, 1817, 2505, 391, 3743, 1634, 699, 1666, 1494, 1444]

test_data = [
    "MCXXXIII", "MMCCXXIV", "MCMXXXVIII", "MDCCCXVII", "MMDV", "CCCXCI", 'MMMDCCXLIII', 'MDCXXXIV', 'DCXCIX', 'MDCLXVI',
    'MCDXCIV', 'MCDXLIV']


for i, d in enumerate(data):
    assert to_roman(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')

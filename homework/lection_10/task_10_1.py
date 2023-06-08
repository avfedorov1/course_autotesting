# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


# Здесь пишем код

# Тренировочка

# def generate_random_name():
#     letters = string.ascii_lowercase
#     rand_string = ''.join(random.choice(letters) for i in range(random_len()))
#     rand_string2 = ''.join(random.choice(letters) for i in range(random_len()))
#     return f'Случайная строка из {len(rand_string)} симв: {rand_string}\n' \
#            f'Случайная строка из {len(rand_string2)} симв: {rand_string2}\n' \
#            f'Итоговая строка: {rand_string} {rand_string2}'

def generate_random_name():
    letters = string.ascii_lowercase
    while True:
        rand_string = ''.join(random.choice(letters) for i in range(random_len()))
        rand_string2 = ''.join(random.choice(letters) for i in range(random_len()))
        yield rand_string + ' ' + rand_string2


def random_len():
    len_str = random.randint(1, 15)
    return len_str


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

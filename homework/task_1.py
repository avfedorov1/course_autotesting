"""
Ссылка на текст к вебинару 1:
https://n.sbis.ru/shared/disk/a5a77817-d8a4-40d3-87d6-972201a7c8e3_74872955-fd7a-4cfc-85a8-5a35249698ad

Задание
1. Установите python 3.11 и PyCharm (лучше 2022.2.3)
2. Запишите в различные переменные свои:
  Фамилию и имя
  Стаж работы в Тензоре
  Должность
3. Используя print() и эти переменные, распечатайте небольшое резюме о себе.
4. Не забывайте про PEP8.
"""

name, surname = 'Антон', 'Федоров'
work_experience_year = 3
work_experience_month = 11
post = 'тестировщик'

print('Всем привет! Меня зовут', name, surname + '.', 'В компании Тензор я работаю',
      str(work_experience_year) + ' года', 'и', str(work_experience_month) + ' месяцев', 'на должности', post + '.')
print()
print(f"Меня зовут {name} {surname}. Мой трудовой стаж в Тензоре равен {work_experience_year} года и "
      f"{work_experience_month} месяцев.\nРаботаю в Тензоре в текущий момент на должности {post}")


# Напишите класс PersonInfo
# Экземпляр класса создается из следующих атрибутов:
# 1. Строка - "Имя Фамилия"
# 2. Число - возраст сотрудника
# 3. Подразделения от головного до того, где работает сотрудник.
# Реализуйте методы класса:
# 1. short_name, который возвращает строку Фамилия И.
# 2. path_deps, возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
# 3. new_salary, Директор решил проиндексировать зарплаты, и новая зарплата теперь вычисляет по формуле:
# 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
# (регистр имеет значение "А" и "а" - разные буквы)
# Например (Ввод --> Вывод) :
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').short_name() --> 'Шленский А.'
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').path_deps() -->
#            'Разработка --> УК --> Автотесты'
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').new_salary() --> 385056 т.к.
# т.к. буква "т" встречается 4 раза, "а" 3 раза, 'о' 2 раза, остальные по одной. Сумма трёх самых частых букв 4+3+2 = 9.
# 1337*32*9 = 385056

# Здесь пишем код
class PersonInfo:

    def __init__(self, name: str, age: int, office: str, *args):
        # Обязательные атрибуты класса
        self.name = name
        self.age = age
        self.office = [office]
        self.division = [*args]
        self.path = [office]

    def short_name(self):
        """
        Метод преобразования полного имени и фамилии в сокращенное: Фамилия И
        :return: строка Фамилия И.
        """
        name = self.name.split()
        name_finish = name[-1] + ' ' + name[0][0] + '.'
        return name_finish

    def path_deps(self):
        """
        Метод, который возвращает полный путь от головного до конечного подразделения.
        :return: Полный путь от головного до конечного подразделения.
        """
        for x in self.division:
            self.path.append("-->")
            self.path.append(x)
        path = ' '.join(self.path)
        return path

    def new_salary(self):
        """
        Метод подсчета новой зарплаты по формуле: 1337*Возраст*суммарное кол-во вхождений трех наиболее часто
        встречающихся букв из списка подразделений.
        :return: сумма - число
        """
        my_str = self.office + self.division
        my_str = ''.join(my_str)
        count_finish = {}
        max_numbers = []
        for letter in my_str:
            count = dict.fromkeys([letter], my_str.count(letter))
            count_finish.update(count)
        for values in count_finish.values():
            max_numbers.append(values)
        max_numbers.sort()
        num = max_numbers[-1] + max_numbers[-2] + max_numbers[-3]
        return 1337 * self.age * num

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
fourth_person = PersonInfo('Иван Иванов', 26, 'Разработка')
second_person = PersonInfo('Пётр Валерьев', 47, 'Разработка', 'УК')
third_person = PersonInfo('Макар Артуров', 51, 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')

data = [first_person.short_name,
        second_person.short_name,
        third_person.short_name,
        fourth_person.short_name,

        first_person.path_deps,
        second_person.path_deps,
        third_person.path_deps,
        fourth_person.path_deps,

        first_person.new_salary,
        second_person.new_salary,
        third_person.new_salary,
        fourth_person.new_salary
        ]


test_data = ['Шленский А.', 'Валерьев П.', 'Артуров М.', 'Иванов И.',

             'Разработка --> УК --> Автотесты',
             'Разработка --> УК',
             'Разработка --> УК --> Нефункциональное тестирование --> Автотестирование',
             'Разработка',
             385056, 314195, 1227366, 173810]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')

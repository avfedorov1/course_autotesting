# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

# Здесь пишем код

with open('test_file/task1_data.txt', encoding='utf-8') as f:
    list_row = f.readlines()  # Формируем списки строк, по которым будем итерироваться
lst = ''  # Создаем пустую строку, куда будем записывать в цикле все, кроме цифр.
for line in list_row:  # Итерируемся по каждой строчке файла
    # Вариант №1: Заменяем цифры -> удаляем (слишком много кода)
    # line = line.replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '')\
    #     .replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '')
    # Вариант №2: Более оптимизированный
    for letter in line:
        if letter.isdigit():
            continue
        else:
            lst += letter  # Полученный результат добавляем в файл
# Создаем/открываем текстовый файл и записываем в него сформированную строку
with open('test_file/task1_answer.txt', mode='w', encoding='utf-8') as file_finish:
    file_finish.write(lst)


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')

# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt
from pathlib import Path

# Здесь пишем код
work_dir = Path.cwd()

f = open('test_file/task1_data.txt', encoding='utf-8')
list_row = f.readlines()  # Формируем списки строк, по которым будем итерироваться
# Создаем новый текстовый файл
file_finish = open('test_file/task1_answer.txt', mode='w', encoding='utf-8')
try:
    # Итерируемся по каждой строчке файла
    for line in list_row:
        # Заменяем цифры -> удаляем
        line = line.replace('0', '')
        line = line.replace('1', '')
        line = line.replace('2', '')
        line = line.replace('3', '')
        line = line.replace('4', '')
        line = line.replace('5', '')
        line = line.replace('6', '')
        line = line.replace('7', '')
        line = line.replace('8', '')
        line = line.replace('9', '')
        # Полученный результат добавляем в файл
        file_finish.write(line)
finally:
    # Закрываем файлы, с которыми работали
    f.close()
    file_finish.close()

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')

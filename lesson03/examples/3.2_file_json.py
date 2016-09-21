import os
import json

DIR = 'files'
python_data = [{"name": 'Петр', 'age': 10}, {"name": 'Александр', 'age': 8}]

# Записываем объект Python в файл в виде JSON
with open(os.path.join(DIR, 'save_json_data.json'), 'w', encoding='UTF-8', ) as f:
    json.dump(python_data, f, ensure_ascii=False)
    # ensure_ascii=False - чтобы некирилические символы не были преобразованы к unicode-последовательности

# Читаем JSON из файла и преобразуем к типу Python
with open(os.path.join(DIR, 'save_json_data.json'), 'r', encoding='UTF-8') as f:
    read_data = json.load(f)

print(read_data)
print(read_data[0])

# Плюсы: Легко читаемая и редактируемая информация в файле
#        JSON можно передавать различным программам на других языках
# Минусы: К JSON можно преобразовать далеко не все стандартные объекты python

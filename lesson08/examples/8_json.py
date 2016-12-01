# -*- coding: utf-8 -*-
import json

data = [{'a':'A', 'b':(2, 4), 'c':3.0 }]
print('DATA:', data)

# Создание JSON из объекта
data_string = json.dumps(data)
print('JSON:', data_string)

# Создание объекта из JSON
data2 = json.loads(data_string)
print('LOAD:', data2)

# Сортировка
print('SORTED:', json.dumps(data, sort_keys=True))

# Форматирование с отступами
print('INDENT:', json.dumps(data, sort_keys=True, indent=4))

# Плотная упаковка
print('COMPRESSED:', json.dumps(data, separators=(',',':')))

# Формат JSON подразумевает, что ключами словаря являются строки
# Если у вас есть другие ключи — то вызовется исключение TypeError.
# Чтобы обойти это нужно использовать skipkeys

data = [ { 'a':'A', 'b':(2, 4), 'c':3.0, ('d',):'D tuple' } ]
print (json.dumps(data, skipkeys=True))












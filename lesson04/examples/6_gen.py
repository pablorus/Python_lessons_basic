# ========================================
# Генераторы списков, словарей и множеств
# ========================================
import random

# Заполняем список произвольными целыми числами
lst = []
for el in range(10):
    lst.append(random.randint(-10, 10))
print('lst = ', lst)

# То же самое, но с помощью генератора списка.
# Компактнее код и выполняется быстрее
lst_g = [random.randint(-10, 10) for _ in range(10)]
print('lst_g = ', lst_g)

# Отбрасываем все отрицательные элементы списка
only_positive = [el for el in lst_g if el >= 0]
print('only_positive = ', only_positive)

# Создаем словарь с помощью генератора словаря
keys = "abcdefg"
values = range(10)
dict_g = {key: value for key, value in zip(keys, values)}  # Подробнее о zip() в следующем примере
print('dict_g = ', dict_g)

# Попроще пример создания словаря генератором
dict2_g = {el: el+4 for el in [1, 4, 6, 8]}
print('dict2_g =', dict2_g)

# Генератор множества
set_g = {value for value in ['a', 'b', 'g', 'a', 1, 0, -10]}
print('set_g =', set_g)
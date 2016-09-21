# ==========================================
#   Реализация матриц вложенными списками
# ==========================================
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("matrix = ", matrix)

# Красиво выводим на экран
print("matrix = ")
for line in matrix:
    print(line)

# Работать с элементами матрицы по индексам в python некорректно
print("*************WHILE***************")
i = 0
while len(matrix) > i:
    line = matrix[i]
    j = 0
    while len(line) > j:
        print("matrix[{}][{}] = {}".format(i, j, matrix[i][j]))
        j += 1
    i += 1
#
# # Все можно сделать гораздо проще и элегантнее
# # Результат один, а код гораздо проще пишется, читается и компактнее
print("*************FOR IN ***************")
for i, line in enumerate(matrix):
    for j, el in enumerate(line):
        print("matrix[{}][{}] = {}".format(i, j, matrix[i][j]))
#
# # Пример транспонирования (поворота) матрицы
print("rotate_matrix = ", list(map(list, zip(*matrix))))
# # Да, вот так все просто-сложно :-)

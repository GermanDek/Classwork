matrix = [[-446, 281, -80],
         [465, 432, -122],
          [13, 'error', 8]]


for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        if isinstance(element, str):
            matrix[i][j] = len(element) * len(element)

# Выводим исправленную матрицу
print("Исправленная матрица:")
for row in matrix:
    print(row)

total_sum = sum([sum(row) for row in matrix])
print("Сумма всех элементов матрицы:", total_sum)
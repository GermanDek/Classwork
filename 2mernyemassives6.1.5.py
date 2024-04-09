matrix = [
    [2, 5, 7],
    [1, 9, 4],
    [6, 3, 8]
]

diagonal_sum = sum([matrix[i][-(i+1)] for i in range(len(matrix))])

print("Сумма чисел по диагонали справа налево:", diagonal_sum)
arr = list(map(int, input("Введите 20 элементов массива через пробел: ").split()))

# Формирование массива номеров нулевых элементов
zero_indices = [index for index, elem in enumerate(arr) if elem == 0]

print("Номера нулевых элементов в массиве:", zero_indices)

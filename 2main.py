arr = list(map(int, input("Введите 15 элементов массива через пробел: ").split()))

# Нахождение номеров всех нулевых элементов
zero_indices = [i for i, x in enumerate(arr) if x == 0]
print("Номера всех нулевых элементов массива:", zero_indices)

# Нахождение номера последнего положительного элемента
last_positive_index = -1
for i, x in enumerate(arr):
    if x > 0:
        last_positive_index = i

print("Номер последнего положительного элемента:", last_positive_index)
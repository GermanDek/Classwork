
arr1 = list(map(int, input("Введите 10 элементов первого массива через пробел: ").split()))

# Ввод второго массива из 10 элементов
arr2 = list(map(int, input("Введите 10 элементов второго массива через пробел: ").split()))

# Проверка на равенство
if arr1 == arr2:
    print("Массивы равны")
else:
    print("Массивы не равны")

# Проверка на неравенство
if arr1 != arr2:
    print("Массивы не равны")
else:
    print("Массивы равны")
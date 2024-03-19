arr = list(map(int, input("Введите 17 элементов массива через пробел: ").split()))
sum_before_negative = 0
for i, x in enumerate(arr):
    if x < 0:
        break
    sum_before_negative += x

print("Сумма всех элементов до первого отрицательного:", sum_before_negative)
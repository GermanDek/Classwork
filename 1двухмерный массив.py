matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("matrix:")
for row in matrix:
    print(row)
print("нечетные числа matrix")
for row in matrix:
    for num in row:
        if num % 2!=0:
            print(num, end="")
print()
count_even = sum(1 for row in matrix for num in row if num %2 == 0)
print("Кол-во четных:",count_even)
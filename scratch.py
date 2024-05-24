def sum(start, end):
    if start > end:
        start, end = end, start
    total = 0
    for num in range(start, end + 1):
        total += num
    return total
result = sum(5, 10)
print(result)

result = sum(10, 5)
print(result)
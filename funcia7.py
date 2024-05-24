def custom_filter(input_list):
    sum_of_sevens = sum([x for x in input_list if isinstance(x, int) and x % 7 == 0])
    print("сумма:", sum_of_sevens)
    return sum_of_sevens < 83

print(custom_filter([7, 10.5, 'txt', 14, 2, 56]))
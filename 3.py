def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return "YES"
    else:
        return "NO"

year = int(input())
result = is_leap_year(year)
print(result)

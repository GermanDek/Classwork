def is_triangle_exist(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return "YES"
    else:
        return "NO"

a = int(input())
b = int(input())
c = int(input())

result = is_triangle_exist(a, b, c)
print(result)

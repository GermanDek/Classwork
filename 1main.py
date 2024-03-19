import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def triangle_area(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    
    s = (a + b + c) / 2
    
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area

# Ввод координат с клавиатуры
x1, y1 = map(float, input("Введите координаты первой вершины через пробел: ").split())
x2, y2 = map(float, input("Введите координаты второй вершины через пробел: ").split())
x3, y3 = map(float, input("Введите координаты третьей вершины через пробел: ").split())

result = triangle_area(x1, y1, x2, y2, x3, y3)
print(f"Площадь треугольника: {result}")
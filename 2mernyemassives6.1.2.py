word_numb = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]

num_input = input("Введите число от 0 до 9: ")

if num_input.isdigit() and 0 <= int(num_input) <= 9:
    num = int(num_input)
    for i in range(num + 1):
        print(word_numb[i])
else:
    print("Введите число от 0 до 9.")
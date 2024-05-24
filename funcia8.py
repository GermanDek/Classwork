def square(x, y):
    top_line = " " + " _ " * x
    middle_line = "|"
    for i in range(1, y + 1):
        middle_line += " {} |".format(i)
    bottom_line = " " + "-" * (x * 3)

    print(top_line)
    for _ in range(y):
        print(middle_line)
    print(bottom_line)

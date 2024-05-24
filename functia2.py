def punct(txt):
    count = 0
    for char in txt:
        if char in "!?.,()":
            count += 1
    return count

input_str = ('(Как дела?)')
result = punct(input_str)
print(result)



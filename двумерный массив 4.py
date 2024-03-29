random_elements = [['toy', 'bee', 'cheese', 'ear'],
                   [False, 'word', '0110110', 10],
                   ['happiness', '(」°ロ°)」', 'luck', None],
                   ['car', '<- code ->', 4.7, True]]

for index, sublist in enumerate(random_elements):
    for i, element in enumerate(sublist):
        if i % 2 == 1:
            print(f"Индекс: {index}, Элемент: {element}")
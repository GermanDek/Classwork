fruits = [['Banana', 'apple'], ['apricot', 'Avocado'], ['lime', 'lemon'], ['Mango', 'grapes']]
for row in fruits:
    for element in row:
        if element[0].isupper():
            print(element)
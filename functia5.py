def Constructor(total_pieces, total_figures, total_cars, total_trees):
    sets_from_pieces = total_pieces // 72
    sets_from_figures = total_figures // 4
    sets_from_cars = total_cars // 2
    sets_from_trees = total_trees // 7

    return min(sets_from_pieces,
sets_from_figures, sets_from_cars,
sets_from_trees)
print(Constructor(144, 8, 4, 14))
print(Constructor(10000, 16, 6, 2))
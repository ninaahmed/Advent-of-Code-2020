def part_one():
    x_coord = 0
    y_coord = 0

    path = []
    f = open("../InputFiles/day3.txt", "r")
    for line in f:
        path += [line]

    tree_count = 0
    while y_coord < len(path):
        if path[y_coord][x_coord] == '#':
            tree_count += 1

        x_coord = (x_coord + 3) % (len(path[0]) - 1)
        y_coord += 1

    print(tree_count)


def part_two():
    path = []
    f = open("../InputFiles/day3.txt", "r")
    for line in f:
        path += [line]

    tree_mult = 1
    directions = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    for dir in directions:
        x_coord = 0
        y_coord = 0
        tree_count = 0
        while y_coord < len(path):
            if path[y_coord][x_coord] == '#':
                tree_count += 1

            x_coord = (x_coord + dir[0]) % (len(path[0]) - 1)
            y_coord += dir[1]

        tree_mult *= tree_count

    print(tree_mult)

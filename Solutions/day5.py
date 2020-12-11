def get_bin_value(half_size, halves, string):
    value = 0
    for c in string:
        value += half_size * halves[c]
        half_size /= 2
    return value


def both_parts():
    f = open("../InputFiles/day5.txt", "r")

    halves = {"F": 0, "B": 1, "L": 0, "R": 1}

    max_id = -1
    ids = set()
    all_ids = set()

    for i in range(8, (126 * 8 + 8)):
        ids.add(i)
        all_ids.add(i)

    for line in f:
        half_size = 64
        row = get_bin_value(half_size, halves, line[0:len(line)-4])

        half_size = 4
        column = get_bin_value(half_size, halves, line[len(line)-4:len(line)-1])

        seat_id = int(row * 8 + column)
        # max_id = max(max_id, seat_id)
        if ids.__contains__(seat_id):
            ids.remove(seat_id)

    # print(max_id)
    for seat in ids:
        if not ids.__contains__(seat - 1) and not ids.__contains__(seat + 1):
            print(seat)

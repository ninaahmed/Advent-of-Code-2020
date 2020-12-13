def part_one():
    f = open("../InputFiles/day10.txt", "r")
    jolts = [int(line) for line in f]
    jolts.sort()

    one_count = 0
    three_count = 1
    curr_jolt = 0

    for j in jolts:
        if j - curr_jolt == 1:
            one_count += 1
        elif j - curr_jolt == 3:
            three_count += 1
        curr_jolt = j

    print(one_count * three_count)


def dp_part_two(jolts):
    jolts.reverse()
    jolts += [0]

    count = {jolts[0]: 1}
    for i in range(1, len(jolts)):
        combos = count[jolts[i-1]]
        if i >= 2 and jolts[i - 2] - jolts[i] <= 3:
            combos += count[jolts[i-2]]
        if i >= 3 and jolts[i - 3] - jolts[i] <= 3:
            combos += count[jolts[i-3]]
        count[jolts[i]] = combos

    print(count[jolts[-1]])


def part_two():
    f = open("../InputFiles/day10.txt", "r")
    jolts = [int(line) for line in f]
    jolts.sort()

    dp_part_two(jolts)

import re


def part_one():
    f = open("../InputFiles/day2.txt", "r")

    valid_count = 0
    for password in f:
        match = re.search(r'(\d+)-(\d+) (.): (.*)', password)
        min = int(match.group(1))
        max = int(match.group(2))
        char = match.group(3)
        passw = match.group(4)

        num_matches = re.findall(char, passw)
        if min <= len(num_matches) <= max:
            valid_count += 1

    print(valid_count)


def part_two():
    f = open("../InputFiles/day2.txt", "r")

    valid_count = 0
    for password in f:
        match = re.search(r'(\d+)-(\d+) (.): (.*)', password)
        pos1 = int(match.group(1))
        pos2 = int(match.group(2))
        char = match.group(3)
        passw = match.group(4)

        char_count = 0
        if passw[pos1 - 1] == char:
            char_count += 1
        if passw[pos2 - 1] == char:
            char_count += 1

        if char_count == 1:
            valid_count += 1

    print(valid_count)

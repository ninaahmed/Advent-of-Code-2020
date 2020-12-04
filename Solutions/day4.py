import re


def part_one():
    f = open("../InputFiles/day4.txt", "r")

    file_lines = list(f)

    num_valid = 0

    index = 0
    req_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    while index < len(file_lines):
        keyset = set()
        while index < len(file_lines) and file_lines[index] != "\n":
            for data in file_lines[index].split(" "):
                keyset.update([data[0:3]])
            index += 1

        if req_fields.issubset(keyset):
            num_valid += 1

        index += 1

    print(num_valid)


def check_hgt(val):
    if val[len(val) - 2:] == "cm":
        num = int(val[0:len(val) - 2])
        return 150 <= num <= 193
    if val[len(val) - 2:] == "in":
        num = int(val[0:len(val) - 2])
        return 59 <= num <= 76
    return False


def check_hcl(val):
    return re.match(r"#[0-9|a-f]{6}", val) is not None and len(val) == 7


def check_pid(val):
    return re.match(r"\d{9}", val) and len(val) == 9


def part_two():
    f = open("../InputFiles/day4.txt", "r")

    file_lines = list(f)

    num_valid = 0

    index = 0
    req_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    while index < len(file_lines):
        keyset = set()
        vals = {}
        while index < len(file_lines) and file_lines[index] != "\n":
            for data in file_lines[index].split(" "):
                keyset.update([data[0:3]])
                string = data[4:].replace("\n", "")
                vals[data[0:3]] = string
            index += 1

        if req_fields.issubset(keyset) and \
                1920 <= int(vals["byr"]) <= 2002 and \
                2010 <= int(vals["iyr"]) <= 2020 and \
                2020 <= int(vals["eyr"]) <= 2030 and \
                check_hgt(vals["hgt"]) and \
                check_hcl(vals["hcl"]) and \
                eye_colors.__contains__(vals["ecl"]) and \
                check_pid(vals["pid"]):
            num_valid += 1

        index += 1

    print(num_valid)

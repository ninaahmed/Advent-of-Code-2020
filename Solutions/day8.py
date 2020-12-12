import re


def run_program(inst):
    acc = 0
    i = 0
    visited = set()

    while i not in visited and i < len(inst):
        visited.add(i)
        line = inst[i]
        match = re.match(r'(.{3}) (\+|-)(\d+)', line)
        op = match.group(1)

        if op == "nop":
            i += 1
        elif op == "acc":
            if match.group(2) == '+':
                acc += int(match.group(3))
            else:
                acc -= int(match.group(3))
            i += 1
        else:
            if match.group(2) == '+':
                i += int(match.group(3))
            else:
                i -= int(match.group(3))

    return acc, i >= len(inst) - 1


def part_one():
    f = open("../InputFiles/day8.txt", "r")

    inst = [line for line in f]
    print(run_program(inst))


def part_two():
    f = open("../InputFiles/day8.txt", "r")

    inst = [line for line in f]
    for i in range(0, len(inst)):
        if inst[i][0:3] != "acc":
            before = inst[i]

            if inst[i][0:3] == "jmp":
                inst[i] = inst[i].replace("jmp", "nop")
            elif inst[i][0:3] == "nop":
                inst[i] = inst[i].replace("nop", "jmp")

            exits = run_program(inst)
            inst[i] = before

            if exits[1]:
                print(exits[0])
                break


if __name__ == "__main__":
    part_two()


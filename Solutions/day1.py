def part2():
    for num1 in numbers:
        for num2 in numbers:
            if num1 != num2:
                diff = 2020 - (num1 + num2)
                if numbers.__contains__(diff):
                    print(num1 * num2 * diff)
                    return


if __name__ == "__main__":
    f = open("../InputFiles/day1-1.txt", "r")

    numbers = set()
    for num_string in f:
        num = int(num_string)
        other_num = 2020 - num
        if numbers.__contains__(other_num):
            print(num * other_num)
        numbers.add(num)

    part2()

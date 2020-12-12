def has_sum(last_arr, sum_num):
    num_set = set()

    for val in last_arr:
        num_set.add(val)

    for val in num_set:
        diff = sum_num - val
        if diff != val and diff in num_set:
            return True

    return False


def part_one():
    f = open("../InputFiles/day9.txt", "r")

    file_it = iter(f)

    last = []
    for i in range(0, 25):
        last += [int(next(file_it))]

    i = 0
    for num in file_it:
        if not has_sum(last, int(num)):
            print(num)
            break

        last[i] = int(num)
        i = (i + 1) % 25


def part_two():
    f = open("../InputFiles/day9.txt", "r")
    tgt_sum = 675280050

    values = [int(line) for line in f]
    value_it = iter(values)

    curr_sum = next(value_it)
    first_index = 0
    last_index = 0
    for num in value_it:
        if curr_sum == tgt_sum:
            smallest = tgt_sum
            largest = 0

            for i in range(first_index, last_index + 1):
                smallest = min(smallest, values[i])
                largest = max(largest, values[i])

            print(smallest + largest)
            break

        last_index += 1
        curr_sum += num

        while curr_sum > tgt_sum:
            curr_sum -= values[first_index]
            first_index += 1

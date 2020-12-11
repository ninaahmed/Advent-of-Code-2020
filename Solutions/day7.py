import re


def part_one():
    f = open("../InputFiles/day7.txt", "r")

    bags = {}
    bag_queue = []
    bag_set = set()

    count = 0

    for line in f:
        match = re.match("(.*) bags contain (.*)", line)
        bag_color = match.group(1)
        con_bags = match.group(2).split(", ")

        for bag in con_bags:
            if bag == "no other bags.":
                break
            bag_match = re.search(r'(\d+) (.*) bag(s?)(\.?)', bag)
            color = bag_match.group(2)

            if color not in bags:
                temp_set = set()
                bags[color] = temp_set

            bags[color].add(bag_color)

            if color == "shiny gold":
                bag_queue += [bag_color]
                bag_set.add(bag_color)

    while len(bag_queue) != 0:
        count += 1
        color = bag_queue[0]
        bag_queue.pop(0)

        if color in bags:
            for b in bags[color]:
                if not bag_set.__contains__(b):
                    bag_queue += [b]
                    bag_set.add(b)

    print(count)


def get_size(bags, bag_count, color):
    if len(bags[color]) == 0:
        return 1

    c = 1
    for i in range(0, len(bags[color])):
        c += bag_count[color][i] * get_size(bags, bag_count, bags[color][i])

    return c


def part_two():
    f = open("../InputFiles/day7.txt", "r")

    bags = {}
    bag_count = {}

    for line in f:
        match = re.match("(.*) bags contain (.*)", line)
        bag_color = match.group(1)
        con_bags = match.group(2).split(", ")

        bag_c = []
        temp_list = []
        for bag in con_bags:
            if bag == "no other bags.":
                break
            bag_match = re.search(r'(\d+) (.*) bag(s?)(\.?)', bag)
            bag_c += [int(bag_match.group(1))]
            temp_list += [bag_match.group(2)]

        bags[bag_color] = temp_list
        bag_count[bag_color] = bag_c

    print(get_size(bags, bag_count, "shiny gold") - 1)


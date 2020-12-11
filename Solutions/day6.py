def partone():
    f = open("../InputFiles/day6.txt", "r")
    file_it = iter(f)

    count = 0

    for groups in file_it:
        blank_line = False
        questions = set()
        print(groups[0:len(groups)-1])
        for c in groups[0:len(groups)-1]:
            questions.add(c)

        for line in file_it:
            if line == "\n":
                break
            print(line[0:len(line)-1])
            for c in line[0:len(line)-1]:
                questions.add(c)

        count += len(questions)

    print(count)


if __name__ == "__main__":
    f = open("../InputFiles/day6.txt", "r")
    file_it = iter(f)

    count = 0

    for groups in file_it:
        blank_line = False
        questions = set()
        for c in groups[0:len(groups)-1]:
            questions.add(c)

        for line in file_it:
            if line == "\n":
                break
            temp_set = set()
            for c in line[0:len(line)-1]:
                temp_set.add(c)

            questions.intersection_update(temp_set)

        count += len(questions)

    print(count)


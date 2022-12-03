if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    # print(ord('a') - 96)
    # print(ord('L') - 38)

    print(len(lines) % 3)

    total = 0
    group = 0
    while group < len(lines):
        common_set = set(lines[group]) & set(lines[group+1]) & set(lines[group+2])
        common = [x for x in common_set if x.isalpha()][0]

        if common.islower():
            total += (ord(common) - 96)
        elif common.isupper():
            total += (ord(common) - 38)
        group += 3

    print(total)



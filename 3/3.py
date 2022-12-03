if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    # print(ord('a') -96 )
    # print(ord('L') - 38)

    total = 0
    for items in lines:
        first_item = items[:len(items)//2]
        second_item = items[len(items)//2:]

        common_set = set(first_item) & set(second_item)
        common = common_set.pop()

        if common.islower():
            total += (ord(common) - 96)
        elif common.isupper():
            total += (ord(common) - 38)

    print(total)



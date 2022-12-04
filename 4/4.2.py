if __name__ == "__main__":
    file = open("input.txt")
    test_file = open("test_input.txt")
    lines = file.readlines()

    overlap = 0
    for pairs in lines:
        list_pairs = pairs.strip().split(',')

        # list_pairs = ['2-4', '3-7'] --> first = [2, 3, 4] second = [3, 4, 5, 6, 7]
        first = [x for x in range(int(list_pairs[0].split('-')[0]), int(list_pairs[0].split('-')[1]) + 1)]
        second = [x for x in range(int(list_pairs[1].split('-')[0]), int(list_pairs[1].split('-')[1]) + 1)]

        if any(s in first for s in second) or any(f in second for f in first):
            overlap += 1

    print(overlap)

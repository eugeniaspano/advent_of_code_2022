
def main():
    file = open("input.txt")
    test_file = open("test_input.txt")
    lines = file.readlines()

    X = 1
    cycle = 1
    cycles_of_interest = [20, 60, 100, 140, 180, 220]
    signal_strength = 0

    for command in lines:
        if len(cycles_of_interest) == 0:
            break
        if command.strip() == 'noop':
            cycle += 1
            if cycle > cycles_of_interest[0]:
                signal_strength += cycles_of_interest[0] * X
                print(X, cycles_of_interest[0])
                del cycles_of_interest[0]
        else:
            cycle += 2
            if cycle > cycles_of_interest[0]:
                signal_strength += cycles_of_interest[0] * X
                print(X, cycles_of_interest[0])
                del cycles_of_interest[0]
            X += int(command.strip().split(' ')[1])

    print(signal_strength)


if __name__ == "__main__":
    main()


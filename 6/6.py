if __name__ == "__main__":
    file = open("input.txt")
    test_file = open("test_input.txt")
    input = file.read()

    list_input = [x for x in input.strip()]

    sequence_length = 4

    for i in range(len(input)-sequence_length):
        sequence = list_input[i: i+sequence_length]
        if len(sequence) == len(set(sequence)):
            print(i+sequence_length, sequence)
            break





import re
from pprint import pprint

if __name__ == "__main__":
    file = open("input.txt")
    test_file = open("test_input.txt")
    lines = file.readlines()

    for i, line in enumerate(lines):
        if line == '\n':
            setup = lines[:i]
            moves = lines[i+1:]

    stacks = {}
    n_stacks = int(setup[-1].split()[-1])

    for setup_line in setup[:-1]:
        crate_positions = [match.start() for match in re.finditer('\[', setup_line)]
        for crate_pos in crate_positions:
            stack_num = int(crate_pos/4 + 1)
            crate = setup_line[crate_pos+1]

            if stack_num not in stacks:
                stacks[stack_num] = list()
            stacks[stack_num].append(crate)

    for stack_num, stack in stacks.items():
        stacks[stack_num] = list(reversed(stack))

    # pprint(stacks)

    for move in moves:
        (quantity, from_crate, to_crate) = [match.group() for match in re.finditer('\d+', move)]
        quantity = int(quantity)
        from_crate = int(from_crate)
        to_crate = int(to_crate)

        stacks[to_crate].extend(list(stacks[from_crate][-quantity:]))
        stacks[from_crate] = stacks[from_crate][:-quantity]

        # pprint(stacks)

    # pprint(stacks)

    solution = ''

    for n in range(1, n_stacks+1):
        solution += stacks[n][-1]
    print(solution)

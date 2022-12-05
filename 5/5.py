
import re
from pprint import pprint


def parse_setup_into_stacks(setup):
    stacks = {}

    for setup_line in setup[:-1]:
        crate_positions = [match.start() for match in re.finditer(r'\[', setup_line)]
        for crate_pos in crate_positions:
            stack_num = int(crate_pos / 4 + 1)
            crate = setup_line[crate_pos + 1]

            if stack_num not in stacks:
                stacks[stack_num] = list()
            stacks[stack_num].append(crate)
    for stack_num, stack in stacks.items():
        stacks[stack_num] = list(reversed(stack))

    return stacks


def move_crates(moves, stacks):
    for move in moves:
        (quantity, from_crate, to_crate) = [match.group() for match in re.finditer(r'\d+', move)]
        quantity = int(quantity)
        from_crate = int(from_crate)
        to_crate = int(to_crate)

        stacks[to_crate].extend(list(reversed(stacks[from_crate][-quantity:])))
        stacks[from_crate] = stacks[from_crate][:-quantity]
        # pprint(stacks)

    return stacks


def main():
    file = open("input.txt")
    test_file = open("test_input.txt")
    content = file.read()

    setup, moves = [section.splitlines() for section in content.split('\n\n')]
    stacks = parse_setup_into_stacks(setup)
    rearranged_stacks = move_crates(moves, stacks)

    solution = ''
    for n in range(1, len(rearranged_stacks) + 1):
        solution += rearranged_stacks[n][-1]
    print(solution)


if __name__ == "__main__":
    main()





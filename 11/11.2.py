import math
from collections import defaultdict
from pprint import pprint


def default_zero():
    return 0


def default_empty_list():
    return []


def default_empty_dict_of_lists():
    return defaultdict(default_empty_list)


def compute_new_worry(initial_worry, worries, dividends):
    C = math.prod(dividends)

    if worries[0] == '+':
        if worries[1].isdigit():
            return int(initial_worry) + int(worries[1]) % C
        else:
            return (int(initial_worry) + int(initial_worry)) % C
    elif worries[0] == '*':
        if worries[1].isdigit():
            return int(initial_worry) * int(worries[1]) % C
        else:
            return int(initial_worry) * int(initial_worry) % C
    else:
        print(f'ERROR: operator not recognized - {worries[0]}')
        exit(1)


def main():
    file = open("input.txt")
    test_file = open("test_input.txt")
    content = file.read()

    monkeys_start = content.split('\n\n')
    monkeys = defaultdict(default_empty_dict_of_lists)
    items_inspected = [0 for _ in range(len(monkeys_start))]

    for block in monkeys_start:
        lines = block.split('\n')
        m_id = lines[0].rstrip().strip().split(' ')[1].split(':')[0]
        items = [num.rstrip().strip() for num in lines[1].split(':')[1].split(',')]
        worry = [x.rstrip().strip() for x in lines[2].split('= old ')[1].split(' ')]
        throwing = list()
        throwing.append(lines[3].split('divisible by ')[1].strip())
        throwing.append(lines[4].split('monkey ')[1].strip())
        throwing.append(lines[5].split('monkey ')[1].strip())

        monkeys[m_id]['items'] = items
        monkeys[m_id]['worry'] = worry
        monkeys[m_id]['throwing'] = throwing

    # pprint(monkeys)

    dividends = []
    for m in monkeys:
        dividends.append(int(monkeys[m]['throwing'][0]))

    for round in range(10000):
        for m in monkeys:
            for i, item in enumerate(monkeys[m]['items']):
                new_worry = compute_new_worry(item, monkeys[m]['worry'], dividends)
                items_inspected[int(m)] += 1
                if new_worry % int(monkeys[m]['throwing'][0]) == 0:
                    new_m = monkeys[m]['throwing'][1]
                    monkeys[new_m]['items'].append(new_worry)
                else:
                    new_m = monkeys[m]['throwing'][2]
                    monkeys[new_m]['items'].append(new_worry)
            monkeys[m]['items'] = list()

    sorted_items_inspected = sorted(items_inspected, reverse=True)

    solution = sorted_items_inspected[0]*sorted_items_inspected[1]
    print(solution)


if __name__ == "__main__":
    main()
